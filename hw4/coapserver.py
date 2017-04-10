#!/usr/local/bin/python3

import aiocoap
import asyncio
import aiocoap.resource as resource
import pickle
import sys
import mcpi.minecraft as minecraft
import mcpi.block as block

# Global Variable for Minecraft Connection
mc = minecraft.Minecraft.create()

# Global Variable for determining if row has been completed 
row_complete = 0

        
class LocationResource (resource.Resource):

    token_id = 0
    x = 0;
    def __init__(self):
        super(LocationResource, self).__init__()
        self.content = (0,0,0,0,0)

    async def render_get (self, request):
        temp = tuple(mc.player.getPos())
        self.content = (temp[0], temp[1], temp[2], self.token_id, self.x)
        g = pickle.dumps (self.content)
        return aiocoap.Message(payload=g)

    async def render_post (self, request):
        p = pickle.loads (request.payload)
        print ('POST: {}'.format (p))
        
        if self.token_id >= 2:
            self.token_id = 0
        else:
            self.token_id += 1
        self.x += 1
        if (self.x <= 10):
            self.content = (1 + self.content[0],self.content[1], self.content[2], self.token_id, self.x)
            mc.setBlock(self.content[0], self.content[1], self.content[2], block.DIRT.id)
            mc.player.setPos(self.content[0], self.content[1], self.content[2])
            mc.postToChat('Block placed at ' + str(self.content[0]) + ' ' + str(self.content[1]) + ' ' + str(self.content[2]))
            print ('Content: {}'.format(self.content))
            payload = pickle.dumps ('POST request received to place block at {}'.format (p))
            return aiocoap.Message (payload=payload)
        else:
            self.x = 0
            self.content = (self.content[0], 1 + self.content[1], self.content[2], self.token_id, self.content[4])
            mc.setBlock(self.content[0], self.content[1], self.content[2], block.DIRT.id)
            mc.player.setPos(self.content[0], self.content[1], self.content[2])
            mc.postToChat('Block placed at ' + str(self.content[0]) + ' ' + str(self.content[1]) + ' ' + str(self.content[2]))
            print ('Content: {}'.format(self.content))
            payload = pickle.dumps ('POST request received to place block at {}'.format (p))
            return aiocoap.Message (payload=payload)

def main ():

    root = resource.Site()
    root.add_resource (('location',), LocationResource())

    asyncio.Task (aiocoap.Context.create_server_context(root))
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()#!/usr/local/bin/python3

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
        temp = tuple(mc.player.getPos())
        self.content = (temp[0], temp[1], temp[2], self.token_id)
        g = pickle.dumps (self.content)
        return aiocoap.Message(payload=g)

    async def render_post (self, request):
        p = pickle.loads (request.payload)
        print ('POST: {}'.format (p))

        if self.token_id > 2:
            self.token_id = 0
        else:
            self.token_id += 1

        self.content = (self.content[0],self.content[1],1+self.content[2],self.token_id)
        mc.setBlock(self.content[0],self.content[1], self.content[2], block.DIRT.id)
        mc.postToChat(self.content[0])
        print ('Content: {}'.format(self.content))
        payload = pickle.dumps ('POST request received to place block at {}'.format (p))
        return aiocoap.Message (payload=payload)

def main ():

    root = resource.Site()
    root.add_resource (('location',), LocationResource())

    asyncio.Task (aiocoap.Context.create_server_context(root))
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()#!/usr/local/bin/python3

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
        self.content = (tuple(mc.player.getPos()), self.token_id)
        g = pickle.dumps (self.content)
        return aiocoap.Message(payload=g)

    async def render_post (self, request):
        p = pickle.loads (request.payload)
        print ('POST: {}'.format (p))

        if self.token_id > 2:
            self.token_id = 0
        else:
            self.token_id += 1

        
        mc.setBlock(self.content[0], self.content[1], 1+self.content[2], block.DIRT.id)
        mc.postToChat('Block placed at ' + ' '.join(map(str, (self.content))))
        self.content = (self.content[0], self.content[1], 1+self.content[2], self.token_id)
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
