import os
import json
import logging
logging.basicConfig(level=logging.DEBUG)

from dotenv import load_dotenv
load_dotenv()

import openai
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initialization
app = App( token=os.environ.get("SLACK_BOT_TOKEN") )
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORGANIZATION")

# Setup OpenAI
var_model = "gpt-3.5-turbo"
var_temp = 0.2
var_max_tokens = 256

def ask_openai(question):
    response = openai.ChatCompletion.create(
        model = var_model,
        messages = [
            {
                "role" : "user",
                "content" : question
            }
        ],
        temperature = var_temp,
        max_tokens = var_max_tokens
    )
    return response.choices[0]['message']['content']

# Events
@app.event("app_mention")
def bot_is_mentioned(body, say, logger):
    try:
        logger.info(body)
        question=""
        for e in body['event']['blocks'][0]['elements'][0]['elements']:
            if(e['type']=='text'):
                question = e['text']
        response = ask_openai(question)
        say(response)
    except Exception as e:
        logger.error(f"Error response: {e}")


@app.event("app_home_opened")
def handle_app_home_opened_events(client, event, logger):
    try:
        with open('static/home.json') as f:
            home_page = json.load(f)
            client.views_publish(
                user_id = event["user"],
                view = home_page
            )
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()