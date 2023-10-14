# gooddata-nlq-slackbot


## Installation

### Create a Slack App

Follow instructions from [here](https://github.com/slack-samples/bolt-python-starter-template/tree/main) to set up a Slack app in your workspace. If you don't have one, you can create it for free.

Here are the steps:
- Open https://api.slack.com/apps/new and choose "From an app manifest"
- Choose the workspace you want to install the application to
- Copy the contents of manifest.json into the text box that says *Paste your manifest code here* (within the JSON tab) and click Next
- Review the configuration and click Create
- Click Install to Workspace and Allow on the screen that follows. You'll then be redirected to the App Configuration dashboard.

### Set up local env

Step 1. Clone this repository

Step 2. Upade the .envfile

- [Here](https://github.com/slack-samples/bolt-python-starter-template/tree/main#environment-variables) here are instructions how to get the Slack tokens

Step 3. Now install dependencies and start the slackbot.

```
pip install --upgrade pip
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 app.py
```