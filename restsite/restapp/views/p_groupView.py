from restapp.models.p_group import P_Group
from restapp.models.p_user import P_User
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from restapp.serializers.p_groupSerializer import P_GroupSerializer

class P_GroupView(APIView):
    
    def get(self, request, name=None, format=None):
        if name == None:
            return Response("No Group Created", status=200)
        try:
            group = P_Group.objects.get(name=name)
        except P_Group.DoesNotExist:
            raise Http404("No Group exists with name: {0}".format(name))

        ret = { "users" : [] }
        users_in_group = P_User.objects.filter(groups__name=name)
        for u in users_in_group:
            ret["users"].append(u.userid)

        return Response(ret, status=200)

    def post(self, request, format=None):
        serializer = P_GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status = 400)

    def put(self, request, name, format=None):
        try:
            
            try:
                group = P_Group.objects.get(name=name)
            except P_Group.DoesNotExist:
                raise Http404("No Group exists with name: {0}".format(name))
            
            users_list = request.data["users"]
            #remove all current users in this group
            users_in_group = P_User.objects.filter(groups__name=name)
            for u in users_in_group:
                u.groups.remove(group)

            #add all the new users for this group
            for userid in users_list:
                try:
                    user = P_User.objects.get(userid=userid)
                except P_User.DoesNotExist as dne:
                    #silently fail these butter fingers
                    continue
                user.groups.add(group)
                user.save()
            return Response("Successfully updated group {0}".format(name), status = 200)
        except KeyError as e:
            return Response("request body needs to have a list of userid's named 'users'", status =400)


    def delete(self, request, name,  format=None):
        try:
            group = P_Group.objects.get(name=name)
        except P_Group.DoesNotExist:
            raise Http404("No Group exists with name: {0}".format(name))
        group.delete()
        return Response("group: {0} deleted".format(name))

    def patch(self, request, format=None):
        return Response("", status=501)

