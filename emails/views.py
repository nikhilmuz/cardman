import json
import requests
import importlib
import base64
import mailparser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from banks.models import Bank
from cardman import request_parsers
from .models import RegisteredEmail


def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


class InboundEmailView(APIView):
    authentication_classes = []
    permission_classes = []
    parser_classes = [request_parsers.PlainTextParser]

    @staticmethod
    def post(request):
        try:
            event = json.loads(request.data)

            if event.get('Type', '') == 'SubscriptionConfirmation':
                url = event.get('SubscribeURL', 'https://example.com')
                requests.get(url)
                return Response({"success": True}, status=status.HTTP_200_OK)

            if event.get('notificationType', '') != 'Received':
                return Response({"success": True}, status=status.HTTP_200_OK)

            user = RegisteredEmail.objects.get(email=event.get('mail', {}).get('source', '').lower()).user
            base64_message = event.get('content', '')
            decoded_bytes = base64.b64decode(base64_message)
            mail = mailparser.parse_from_bytes(decoded_bytes)
            decoded_message = mail.text_plain[0]

            for bank in Bank.objects.all():
                if bank.alert_email in decoded_message.lower():
                    parser = getattr(
                        importlib.import_module('emails.email_parsers.' + bank.cc_transaction_email_parser),
                        bank.cc_transaction_email_parser
                    )
                    parser.parse(strip_non_ascii(decoded_message).replace('\r\n', '').replace('=', '').replace('>', ''),
                                 user, bank)
                    return Response({"success": True}, status=status.HTTP_200_OK)

            return Response({"success": True}, status=status.HTTP_200_OK)
        except Exception as e:
            pass
        return Response({"success": True}, status=status.HTTP_200_OK)
