from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .schema import inter_schema

class LoginView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None, *args, **kwargs):
        password = request.GET.get('password')
        try:
            user_instanse = User.objects.get(username=username, password=password)
            result = {'token': Token.objects.get_or_create(user=user_instanse)[0].key}
        except:
            result = {'error': 'login data not correct'}
        print(result)
        return Response(result)


class TokenAuthorizationTest(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request, format=None, *args, **kwargs):
        query = """
        query{
            allUsers(){
                id
            }
        }
        """

        result = inter_schema.execute(query, {}, {"user": request.user})
        return Response(result.to_dict())

