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
        entry = json.loads(pickle.loads(body))
        if (self.posts.find_one({"email" : entry["email"]) != None):
            ch.basic_publish(exchange='', routing_key=properties.reply_to,
                                properties=pika.BasicProperties(correlation_id = properties.correlation_id),
                                body = pickle.dumps(json.dumps({"reply" : "Already Registered"})))
        else:
            entry.update({"payment" : 0})
            self.posts.insert_one(entry)
            ch.basic_publish(exchange='', routing_key=properties.reply_to,
                                properties=pika.BasicProperties(correlation_id = properties.correlation_id),
                                body = pickle.dumps(json.dumps({"reply":"Registered"})))

    def pay(self, ch, method, properties, body):
        entry = json.loads(pickle.loads(body))
        qu = self.posts.find_one({"email" : entry["email"]})
        if qu == None:

        else:
            cur = qu["payment"]
            for i in range(len(entry["list"])):
                cur += 1
            posts.update_one({"email" : entry["email"]}, {"$set" : {"payment" : cur}})
            print ('Pay')
            ch.basic_publish(exchange='', routing_key=properties.reply_to,
                                properties=pika.BasicProperties(correlation_id = properties.correlation_id),
                                body = pickle.dumps('Payment received'))

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
        self.db = self.client.accdb
        self.coll = self.db.accounts
        self.posts= self.db.posts

        vhost = '/'
        mbservip = sys.argv[1]
        creds = pika.PlainCredentials ('guest', 'guest')
        params = pika.ConnectionParameters (virtual_host = vhost, credentials = creds, host=mbservip)
        self.connection = pika.BlockingConnection (params)
        self.channel = self.connection.channel()
#        self.channel.exchange_declare (exchange = 'smartgroceries', type='direct')
        result = self.channel.queue_declare (queue='accounts', exclusive=True)
        self.qname = result.method.queue

#        self.channel.queue_bind (exchange='smartgroceries', queue=qname, routing_keys='accounts')

        self.channel.basic_consume (self.callback, queue=self.qname, no_ack=True)
        self.channel.start_consuming()


q = Accounts()
