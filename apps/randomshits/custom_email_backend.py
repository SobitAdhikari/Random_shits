# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model

# User = get_user_model()


# class EmailOrPhoneBackend(ModelBackend):

#     def authenticate(self, request, username=None, password=None, **kwargs):
#         # username here can be email OR phone
#         try:
#             user = User.objects.get(email=username)
#         except User.DoesNotExist:
#             try:
#                 user = User.objects.get(phone_number=username)
#             except User.DoesNotExist:
#                 return None

#         if user.check_password(password):
#             return user

#         return None