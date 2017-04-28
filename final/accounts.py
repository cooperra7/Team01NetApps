from pymongo import MongoClient
import pika
import sys
import json
import getopt
import pickle
import json

class Accounts(object):
    def register(self, ch, method, properties, body):
        print('Register')
        ch.basic_publish(exchange='', routing_key=properties.reply_to,
                                properties=pika.BasicProperties(correlation_id = properties.correlation_id),
                                body = pickle.dumps('Registered'))

    def pay(self, ch, method, properties, body):
        print ('Pay')

    def callback (self, ch, method, properties, body):
        mess = pickle.loads (body)
        obj = json.loads(mess)
        if (obj['type'] == "register"):
            self.register(ch, method, properties, body)
        elif (obj['type'] == "pay"):
            self.pay(ch, method, properties, body)
        else:
            print ('Not Valid')

    def __init__(self):
        self.client = MongoClient ('localhost', 27017)
        self.db = self.client.accounts

        vhost = '/'
        mbservip = 'localhost'
        creds = pika.PlainCredentials ('guest', 'guest')
        params = pika.ConnectionParameters (virtual_host = vhost, credentials = creds, host=mbservip)
        self.connection = pika.BlockingConnection (params)
        self.channel = self.connection.channel()
#        self.channel.exchange_declare (exchange = 'smartgroceries', type='direct')
        result = self.channel.queue_declare (queue='rpc_queue', exclusive=True)
        self.qname = result.method.queue

#        self.channel.queue_bind (exchange='smartgroceries', queue=qname, routing_keys='accounts')

        self.channel.basic_consume (self.callback, queue=self.qname, no_ack=True)
        self.channel.start_consuming()


q = Accounts()
