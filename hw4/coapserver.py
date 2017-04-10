#!/usr/local/bin/python3

import aiocoap
import asyncio
import aiocoap.resource as resource
import pickle
import sys
import mcpi.minecraft as minecraft
import mcpi.block as block

#Global Variable for Minecraft Connection
mc = minecraft.Minecraft.create()
        
class LocationResource (resource.Resource):

    token_id = 0

    def __init__(self):
        super(LocationResource, self).__init__()
        self.content = (0,0,0,0)


    async def render_get (self, request):
        self.content = tuple(mc.player.getPos())
        g = pickle.dumps (self.content)
        return aiocoap.Message(payload=g)

    async def render_post (self, request):
        p = pickle.loads (request.payload)
        print ('POST: {}'.format (p))

        if self.token_id > 3:
            self.token_id = 0
        else:
            self.token_id += 1

        self.content = (0,0,1+self.content[2],self.token_id)
        mc.setBlock(self.content ,block.DIRT.id)
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
