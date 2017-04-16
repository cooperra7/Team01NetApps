import pymongo
import pika
import sys
import json
import getopt

# Need name, payment method, info for payment method, token, amount paid/items bought

# { "name" : string, "token" : int, "payment" : { "type" : string, "value" : int }, "amount" : int }


