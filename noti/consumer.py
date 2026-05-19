import json

from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync


class SynchronusConsumer(SyncConsumer):

    def websocket_connect(self, event):

        print("Tapai sanga hat milayo", event)
        print("Channel Layer:", self.channel_layer)
        print("Channel Name:", self.channel_name)

        async_to_sync(self.channel_layer.group_add)(
            'sangathan',
            self.channel_name
        )

        self.send({
            'type': 'websocket.accept'
        })

        # send own channel name to frontend
        self.send({
            'type': 'websocket.send',
            'text': json.dumps({
                'type': 'connection',
                'channel_name': self.channel_name
            })
        })


    def websocket_receive(self, event):

        print("Message received:", event['text'])

        data = json.loads(event['text'])

        message = data['msg']

        async_to_sync(self.channel_layer.group_send)(
            'sangathan',
            {
                'type': 'chat.message',
                'message': message,
                'sender_channel_name': self.channel_name
            }
        )


    def chat_message(self, event):

        print("Event:", event)

        self.send({
            'type': 'websocket.send',
            'text': json.dumps({
                'msg': event['message'],
                'sender_channel_name': event['sender_channel_name']
            })
        })


    def websocket_disconnect(self, event):

        print("Disconnected", event)

        async_to_sync(self.channel_layer.group_discard)(
            'sangathan',
            self.channel_name
        )

        raise StopConsumer()
    
class AsynchronusConsumer(AsyncConsumer):

    async def websocket_connect(self, event):

        print("Tapai sanga hat milayo", event)
        print("Channel Layer:", self.channel_layer)
        print("Channel Name:", self.channel_name)

        await self.channel_layer.group_add(
            'sangathan',
            self.channel_name
        )

        await self.send({
            'type': 'websocket.accept'
        })

        # send own channel name to frontend
        await self.send({
            'type': 'websocket.send',
            'text': json.dumps({
                'type': 'connection',
                'channel_name': self.channel_name
            })
        })


    async def websocket_receive(self, event):

        print("Message received:", event['text'])

        data = json.loads(event['text'])

        message = data['msg']

        await self.channel_layer.group_send(
            'sangathan',
            {
                'type': 'chat.message',
                'message': message,
                'sender_channel_name': self.channel_name
            }
        )


    async def chat_message(self, event):

        print("Event:", event)

        await self.send({
            'type': 'websocket.send',
            'text': json.dumps({
                'msg': event['message'],
                'sender_channel_name': event['sender_channel_name']
            })
        })


    async def websocket_disconnect(self, event):

        print("Disconnected", event)

        await self.channel_layer.group_discard(
            'sangathan',
            self.channel_name
        )

        raise StopConsumer()
    












# #chat app with default group names
# from channels.consumer import AsyncConsumer,SyncConsumer
# from channels.exceptions import StopConsumer
# from asgiref.sync import async_to_sync

# class SynchronusConsumer(SyncConsumer):
#     def websocket_connect(self,event):
#         print("Tapai sanga hat mian vayo",event)
#         print("channel layer",self.channel_layer)#get default from settings.py
#         print("channel_name",self.channel_name)
#         #adding channel to a new or existing  group
#         async_to_sync(self.channel_layer.group_add)('sangathan',#group name
#                                             self.channel_name)
#                                             #group name ,when message is sent then all the channel in group sangathan gets it
#                                               #group_add is asynchronus function

#         self.send({
#             'type':'websocket.accept',
#             'text':'yoho aayo'
#         })
    
#     def websocket_receive(self,event):
#         print("tapaile pathaunu vayeko message prapta vayo",event['text'])
#         print("type of message sent from client",type(event['text']))
#         async_to_sync(self.channel_layer.group_send)('sangathan',{
#             'type':'chat.message',
#             'message':event['text']
#         })
#     def chat_message(self,event):
#         print('Event....',event)
#         print('Actual data ...',event['message'])
#         self.send({ #to send message to the group  
#             'type':'websocket.send',
#             'text':event['message']
#         }
#         )
        

    
     

#     def websocket_disconnect(self,event):
#         print("Milan vayepaxi bixod nischaye nai hunxa aile ko lagi bixod vayo",event)
#         print("channel layer",self.channel_layer)#get default from settings.py
#         print("channel_name",self.channel_name)
#         async_to_sync(self.channel_layer.group_discard)('programmers',
#                                                         self.channel_name)
#         raise StopConsumer

# class AsynchronusConsumer(AsyncConsumer):
#     async def websocket_connect(self,event):
#         print("Tapai sanga hat mian vayo",event)
#         print("channel layer",self.channel_layer)#get default from settings.py
#         print("channel_name",self.channel_name)
#         #adding channel to a new or existing  group
#         await self.channel_layer.group_add('sangathan',#group name
#                                             self.channel_name)
#                                             #group name ,when message is sent then all the channel in group sangathan gets it
#                                               #group_add is asynchronus function

#         await self.send({
#             'type':'websocket.accept',
#             'text':'yoho aayo'
#         })
    
#     async def websocket_receive(self,event):
#         print("tapaile pathaunu vayeko message prapta vayo",event['text'])
#         print("type of message sent from client",type(event['text']))
#         await self.channel_layer.group_send('sangathan',{
#             'type':'chat.message',
#             'message':event['text']
#         })
#     async def chat_message(self,event):
#         print('Event....',event)
#         print('Actual data ...',event['message'])
#         await self.send({ #to send message to the group  
#             'type':'websocket.send',
#             'text':event['message']
#         }
#         )

#     async def websocket_disconnect(self,event):
#         print("Milan vayepaxi bixod nischaye nai hunxa aile ko lagi bixod vayo",event)
#         print("channel layer",self.channel_layer)#get default from settings.py
#         print("channel_name",self.channel_name)
#         await self.channel_layer.group_discard('programmers',
#                                         self.channel_name)
#         raise StopConsumer
    
# from channels.consumer import SyncConsumer, AsyncConsumer
# from channels.exceptions import StopConsumer
# from time import sleep
# import asyncio,json

# class AsynchronusConsumer(AsyncConsumer): # all at a time
#     async def websocket_connect(self,event):
#         print("handshake is performed ")
#         await self.send({
#             'type':'websocket.accept'
#         })

#     async def websocket_receive(self,event):
#         print("tapaile pathaunu vayeko message prapta vayo ",event['text'])
#         for i in range(50):
#             await self.send({
#                 'type':'websocket.send',
#                 'text':json.dumps({"count":i})
#             })
#             await asyncio.sleep(1) #delay message sending from server by 1 sec


#     async def websocket_disconnect(self,event):
#         print("Harka is out of samparka")
#         raise StopConsumer()


# class SynchronusConsumer(SyncConsumer): #one after another
#     #this handler is called when client initally opens a connection and about to finish handshake
#     def websocket_connect(self,event):
#         print("websocket connection is established",event)#get default channel layer from a project
#         print("Channel layer",self.channel_layer)#get channel Name
#         print('channel name',self.channel_name)
#         #add a channel layer to new or existing group
#         self.send({
#             'type':'websocket.accept'
#         })

#     #this handler is called when client sends message
#     def websocket_receive(self,event):
#         print("tapaile pathaunu vayeko message prapta vayo",event)
#         for i in range (50):
#             self.send({
#                 'type':'websocket.send',
#                 'text':str(i)
#             })
#             sleep(10)
    
        
#     #called when connection is lost either from server or client side
#     def websocket_disconnect(self,event):
#         print("tapai sanga samparka tuteko xa hasta dhanyabad",event)
#         raise StopConsumer()