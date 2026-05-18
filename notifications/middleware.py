# from urllib.parse import parse_qs #"token"="abc123" to {"token": ["abc123"]}
# from channels.middleware import BaseMiddleware #base class for custom Channels middleware.
# from channels.db import database_sync_to_async #converts normal Django DB operations into async-safe operations.

# from django.contrib.auth.models import AnonymousUser
# from django.contrib.auth import get_user_model
# from rest_framework_simplejwt.tokens import AccessToken

# User=get_user_model()

# @database_sync_to_async #this decorator converts the synchronous DB function into an async-compatible function.
# def get_user(user_id):
#     try: 
#         return User.objects.id(id=user_id)
#     except User.DoesNotExist:
#         return AnonymousUser()
    
# class JwtAuthMiddleware(BaseMiddleware):#Creates a middleware for WebSocket authentication.
#     async def __call__(self, scope, receive, send): #runs whenever websocket connection is created
#         # scope → connection information (similar to django request)
#         # receive → receives messages
#         # send → sends messages

#         query_string=parse_qs(
#             scope["query_string"].decode()
#         )
#         token=query_string.get("token")
#         if token:
#             try:
#                 accesstoken=AccessToken(token[0])
#                 # token[0] because parse_qs returns lists.
#                 # Validates JWT signature and expiration.
#                 # Decodes payload.
#                 user=await get_user(
#                     accesstoken("user_id")
#                 )
#                 scope("user")=user #store so that self.scope["user"] can be acessed on websockets
#             except Exception as e:

#                 print("JWT ERROR:", e)

#                 scope["user"] = AnonymousUser()

#         else:
#                 scope["user"] = AnonymousUser()
#         return await super().__call__(
#             scope,
#             receive,
#             send
#         )   

        

    



from urllib.parse import parse_qs

from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async

from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()


@database_sync_to_async
def get_user(user_id):

    try:
        return User.objects.get(id=user_id)

    except User.DoesNotExist:
        return AnonymousUser()


class JWTAuthMiddleware(BaseMiddleware):

    async def __call__(self, scope, receive, send):

        query_string = parse_qs(
            scope["query_string"].decode()
        )

        token = query_string.get("token")

        if token:

            try:

                access_token = AccessToken(token[0])

                user = await get_user(
                    access_token["user_id"]
                )

                scope["user"] = user

            except Exception as e:

                print("JWT ERROR:", e)

                scope["user"] = AnonymousUser()

        else:
            scope["user"] = AnonymousUser()

        return await super().__call__(
            scope,
            receive,
            send
        )   
    



