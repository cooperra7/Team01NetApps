#!/usr/local/bin/python3

import aiocoap
import asyncio
import aiocoap.resource as resource
import pickle

class LocationResource (resource.Resource):

    def __init__(self):
        super(LocationResource, self).__init__()
        self.content = (0,0,0)

    async def render_get (self, request):
        g = pickle.dumps (self.content)
        return aiocoap.Message(payload=g)

    async def render_post (self, request):
        p = pickle.loads (request.payload)
        print ('POST: {}'.format (p))
        self.content = (0,0,1+self.content[2])
        print ('Content: {}'.format(self.content))
        payload = pickle.dumps ('POST request received to place block at {}'.format (p))
        return aiocoap.Message (payload=payload)

def main ():
    root = resource.Site()
    root.add_resource (('location',), LocationResource())

    asyncio.Task (aiocoap.Context.create_server_context(root))
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()
