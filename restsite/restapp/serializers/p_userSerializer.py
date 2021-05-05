from restapp.models.p_user import P_User
from rest_framework import serializers

class P_UserSerializer(serializers.ModelSerializer):
    userid = serializers.CharField(max_length=512)
    class Meta:
        model = P_User
        fields = ['first_name', 'last_name', 'userid', 'groups']

