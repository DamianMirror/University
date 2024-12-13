from rest_framework.authentication import BaseAuthentication
from .models import User

class SessionAuthentication(BaseAuthentication):
    def authenticate(self, request):
        id = request.session.get('id')
        if not id:
            return None  # Authentication failed

        try:
            user = User.objects.get(id=id)
            return (user, None)  # (authenticated user, authentication method)
        except User.DoesNotExist:
            return None

