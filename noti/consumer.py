from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio,json

class AsynchronusConsumer(AsyncConsumer): # all at a time
    async def websocket_connect(self,event):
        print("handshake is performed ")
        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self,event):
        print("tapaile pathaunu vayeko message prapta vayo ",event['text'])
        for i in range(50):
            await self.send({
                'type':'websocket.send',
                'text':json.dumps({"count":i})
            })
            await asyncio.sleep(1) #delay message sending from server by 1 sec


    async def websocket_disconnect(self,event):
        print("Harka is out of samparka")
        raise StopConsumer()


class SynchronusConsumer(SyncConsumer): #one after another
    #this handler is called when client initally opens a connection and about to finish handshake
    def websocket_connect(self,event):
        print("websocket connection is established",event)#get default channel layer from a project
        print("Channel layer",self.channel_layer)#get channel Name
        print('channel name',self.channel_name)
        #add a channel layer to new or existing group
        self.send({
            'type':'websocket.accept'
        })

    #this handler is called when client sends message
    def websocket_receive(self,event):
        print("tapaile pathaunu vayeko message prapta vayo",event)
        for i in range (50):
            self.send({
                'type':'websocket.send',
                'text':str(i)
            })
            sleep(10)
    
        
    #called when connection is lost either from server or client side
    def websocket_disconnect(self,event):
        print("tapai sanga samparka tuteko xa hasta dhanyabad",event)
        raise StopConsumer()