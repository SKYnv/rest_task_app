from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

class MyCustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get("user")

        # if not username: # no username passed in request headers
        #     return None # authentication did not succeed

        try:
            user = User.objects.get(username='admin') # get the user
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist

        return (user, None) # authentication successful