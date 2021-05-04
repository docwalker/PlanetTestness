from restapp.models.p_group import P_Group
from rest_framework import viewsets
from restapp.serializers.p_groupSerializer import P_GroupSerializer

class P_GroupViewSet(viewsets.ModelViewSet):
    
    queryset = P_Group.objects.all()
    serializer_class = P_GroupSerializer
