import Recommend_using_TFIDF as tfidf
import random
from logging import INFO
from typing import Dict

from dialogflow_fulfillment import WebhookClient
from flask import Flask, request, render_template,jsonify
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
    parameters=req['queryResult']['parameters']
    # if query_result.get('action') == 'Greeting':
    #     ### Perform set of executable code
    #     ### if required
    #     ### ...

    #     fulfillmentText = "Hi, my name is Jay"
    #     return {
    #             "fulfillmentText": fulfillmentText,
    #             "source": "webhookdata"
    #         }

    if  query_result.get('action') == 'recommend.genre':
        ### Perform set of executable code
        ### if required
        ### ...

        if parameters['Genre'][0]:
            input_text=''
            input_text= parameters['Genre'][0]
            book = tfidf.recommend_book(input_text)
            booktitle=book['Title']
            fulfillmentText= "Sure! Based on your interest in {genre}, I would recommend {title}. ".format(genre=parameters['Genre'][0], title=booktitle)
        else:
            fulfillmentText = "Sorry, I don't understand what you mean."

        return {
                "fulfillmentText": fulfillmentText,
                "source": "webhookdata",

                }
    elif query_result.get('action') == 'common':
        ### Perform set of executable code
        ### if required
        ### ...
        if parameters['Description'][0]:
            input_text=''
            input_text= parameters['Genre'][0]+parameters['Description'][0]
            print(input_text)
            book = tfidf.recommend_book(input_text)
            booktitle=book['Title']
            # authors=book['authors']
            print(booktitle)
            #Call algorithm
            responses = [
    "Considering your interests, we recommend you take a look at {title}. They should be a great fit!",
    "We've found some books that you might like: {title}. Give them a try and see if they meet your expectations!",
    "Sure! Based on your interest in , I would recommend {title}.",
    "Our recommendations for you are {title}. These books align well with your described preferences.",
    "We think you'll enjoy the following books: {title}. They match the criteria you've provided.",
    "After analyzing your preferences, we believe you'll find {title} to be excellent choices for your next read.",
    "Here are some books we think you'll love: {title}. They cater to the interests you've described.",
    "We've curated a list of books for you based on your interests: {title}. Happy reading!",
    "Taking into account your preferences, we'd like to recommend {title}. We hope they'll captivate your attention!"

]           
            random.shuffle(responses)
            fulfillmentText=responses[0].format(genre=parameters['Genre'][0], title=booktitle)
            
            # fulfillmentText= "Sure! Based on your interest in {genre}, I would recommend {title}. What would you like to do next? Do you want to check its publication date, review rating score, or discover similar books we recommend?".format(genre=parameters['Genre'][0], title=booktitle)
        else:
            fulfillmentText = "Sorry, I don't understand what you mean."

        return {
                "fulfillmentText": fulfillmentText,
                "source": "webhookdata",

                }
    else:
        return {
                "fulfillmentText": fulfillmentText,
                "source": "webhookdata"
            }

# run the app
if __name__ == '__main__':
    app.run(debug=True)
