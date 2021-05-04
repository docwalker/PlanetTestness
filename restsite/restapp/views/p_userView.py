from restapp.models.p_user import P_User
from rest_framework import viewsets
from restapp.serializers.p_userSerializer import P_UserSerializer


class P_UserViewSet(viewsets.ModelViewSet):

    queryset = P_User.objects.all()
    serializer_class = P_UserSerializer


