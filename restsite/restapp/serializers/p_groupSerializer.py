from restapp.models.p_group import P_Group
from rest_framework import serializers

class P_GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = P_Group
        fields = ['name']
