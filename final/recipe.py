from pymongo import MongoClient
import pika
import sys
import json
import getopt
import pickle
import json
import requests

class Recipe(object):

    def recipe(self, ch, method, properties, body):
        print('Recipe')
	temp = json.loads(body)
        ingredients = temp['item']
	
        number = '10'

        response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients?",
            headers={
                "X-Mashape-Key": "1nMwLi8qDomshJNqUsfRJSDTcZHCp1ZopPPjsnaY7yCIdfAnVX",
                "Accept": "application/json"
            },
            params={
                'ingredients': ingredients,
                'number': number,
                'fillIngredients': 'true',
                'limitLicense': 'true',
                'ranking': '1'
            }
            )
        ch.basic_publish(exchange='', routing_key=properties.reply_to,
                         properties=pika.BasicProperties(correlation_id=properties.correlation_id),
                         body=pickle.dumps(response.json()))

    def callback (self, ch, method, properties, body):
        mess = pickle.loads (body)
        obj = json.loads(mess)
        if (obj['type'] == "recipe"):
            self.recipe(ch, method, properties, body)
        else:
            print ('Not Valid')

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.accounts

        vhost = '/'
        mbservip = sys.argv[1]
        creds = pika.PlainCredentials('guest', 'guest')
        params = pika.ConnectionParameters(virtual_host=vhost, credentials=creds, host=mbservip)
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        #        self.channel.exchange_declare (exchange = 'smartgroceries', type='direct')
        result = self.channel.queue_declare(queue='recipe', exclusive=True)
        self.qname = result.method.queue

        #        self.channel.queue_bind (exchange='smartgroceries', queue=qname, routing_keys='accounts')

        self.channel.basic_consume(self.callback, queue=self.qname, no_ack=True)
        self.channel.start_consuming()

q = Recipe()
