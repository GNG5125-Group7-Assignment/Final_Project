from logging import INFO
from typing import Dict

from dialogflow_fulfillment import WebhookClient
from flask import Flask, request, render_template
from flask.logging import create_logger

# Create Flask app and enable info level logging
# import flask dependencies
from flask import Flask, request

# initialize the flask app
app = Flask(__name__)

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = ''
    booktitle=''
    query_result = req.get('queryResult')
    parameters=query_result.get('parameters')
    if query_result.get('action') == 'Greeting':
        ### Perform set of executable code
        ### if required
        ### ...

        fulfillmentText = "Hi, my name is Jay"
        return {
                "fulfillmentText": fulfillmentText,
                "source": "webhookdata"
            }

    elif  query_result.get('action') == 'recommend.genre':
        ### Perform set of executable code
        ### if required
        ### ...

        if parameters.get('Genre')[0]=='science':
            booktitle = "A science book"
            fulfillmentText= "Sure! Based on your interest in {genre}, I would recommend {title}. What would you like to do next? Do you want to check its publication date, review rating score, or discover similar books we recommend?".format(genre=parameters['Genre'][0], title=booktitle)
        else:
            fulfillmentText = "Sorry, I don't understand what you mean."

        return {
                "fulfillmentText": fulfillmentText,
                "source": "webhookdata",

                }

# run the app
if __name__ == '__main__':
    app.run(debug=True)
