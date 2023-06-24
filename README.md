# Cardman API

A one-stop solution for managing all your Credit Card needs with an option to realtime track your Credit Card transactions.

## Features

- Realtime transaction tracking based on alert email auto-forward rules on your mailbox
- Consolidated card balances

## Getting started

- Step 1: Create a Railway.app account and project

  - Visit the Railway.app website (https://railway.app/) and sign up for an account if you don't have one already.
  - Create a new project in Railway.app by connecting your Git repository containing this Django project.

- Step 2: Set up environment variables in Railway.app

  - In your Railway.app project, navigate to the "Environment Variables" section.
  - Click on the "Add Variable" button.
  - Set the variable name as SNS_ENDPOINT_SECRET and provide a random secure UUID as the value. You can generate a UUID using an online UUID generator or use a programming language to generate one.
  - Click on the "Add Variable" button again.
  - Set the variable name as ENDPOINT_URI_WITH_SCHEMA and provide your app URL with the appropriate schema (HTTP or HTTPS).
  - Example: https://your-domain.com or http://your-domain.com
  - Save the environment variables.

- Step 3: Deploy your Django project on Railway.app

  - Once your environment variables are set, click the "Deploy" button in Railway.app to deploy your Django project.
  - Railway.app will automatically build and deploy your project based on this Git repository's configuration.
  - That's it! Your Django project will be deployed on Railway.app, and the environment variables SNS_ENDPOINT_SECRET and ENDPOINT_URI_WITH_SCHEMA will be set. You can now use these variables to configure the SNS integration and use the provided endpoint URL.

- Step 4: Set up an AWS account

  - Create an AWS account if you don't have one already.
  - Go to the AWS Management Console and navigate the Simple Email Service (SES) dashboard.
  - Follow the instructions to verify your email domain
  - Forward your MX Entry to AWS SES

- Step 5: Configure SNS to handle email receiving

  - Go to the AWS Management Console and navigate to the SNS dashboard.
  - Click on "Create topic" to create a new topic.
  - Provide a name for the topic and click "Create topic" to create it.
  - Select the newly created topic from the list and click "Create subscription".
  - Choose the protocol as HTTPS/HTTP.
  - In the "Endpoint" field, enter the endpoint URL of your Django app where you want to receive the email payload, for example, https://your-domain.com/emails/inbound/SNS_ENDPOINT_SECRET/ (replace your-domain.com and SNS_ENDPOINT_SECRET with your actual values).

- Step 6: Configure Django user:
  - Clone this repository and change database credentials to one from the railway app
  - Run `python manage.py createsuperuser` to create a user
  - Navigate to https://your-domain.com/admin and log in using the credentials generated.
  - Add a bank with an alert email used to receive emails (in lowercase) and parser name, i.e. `AxisCCParser` for Axis Bank.
  - Add a registered email used to forward emails to the server.

## Usage

Navigate to `/cards` to view all the cards info
Navigate to `/cards/add` to add a card
Navigate to `/transactions` to view all the transactions info
Navigate to `/transactions/add` to add a transaction
Navigate to `/banks` to view all the bank info

## Additional information

Feel free to open a PR with new parsers in `/emails/email_parsers`
This is still a work in progress. Any feedback and bug reports are welcomed.
