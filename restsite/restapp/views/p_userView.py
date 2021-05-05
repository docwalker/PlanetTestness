from restapp.models.p_user import P_User
from restapp.models.p_group import P_Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


from restapp.models.p_user import P_User
from restapp.serializers.p_userSerializer import P_UserSerializer


class P_UserView(APIView):

    #queryset = P_User.objects.all()
    #serializer_class = P_UserSerializer

    def get(self, request, userid=None, format=None):

        if userid==None:
            return Response("No User Created", status=200)
        try:
            user = P_User.objects.get(userid=userid)
        except P_User.DoesNotExist:
            raise Http404("No User exists with userid: {0}".format(userid))
        
        serializer = P_UserSerializer(user)
        return Response(serializer.data, status = 200)
    
    def post(self, request, format=None):
        #because I disabled the verifier for uniqueness for the put, I need to check here.  Really need to refactor a bunch of the view logic into the serializer for round 2
        unique = True
        try:
            P_User.objects.get(userid=request.data["userid"])
            unique = False
        except P_User.DoesNotExist:
            unique = True
        if not unique:
            return Response("userid {0} already exists".format(request.data["userid"]), status = 400)

        serializer = P_UserSerializer(data=request.data)
        if serializer.is_valid() and unique:
            user = serializer.save()
            
            try:
                to_add = request.data["groups"]
                for group_name in to_add:
                    try:
                        group = P_Group.objects.get(name=group_name)
                    except P_Group.DoesNotExist as dne:
                        continue
                    user.groups.add(group)
            except KeyError as e:
                return Response(str(e), status =400)
            user.save()    
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status = 400)

    def delete(self, request, userid, format=None):
        try:
            user = P_User.objects.get(userid=userid)
        except P_User.DoesNotExist:
            raise Http404("No User exists with userid: {0}".format(userid))

        user.delete()
        return Response("user: {0} deleted".format(userid), status = 200)

    def put(self, request, userid, format=None):
        request.data["userid"] = userid
        serializer = P_UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = P_User.objects.get(userid=userid)
            except P_User.DoesNotExist:
                raise Http404("No User exists with userid: {0}".format(userid))
            user = P_User.objects.get(userid=userid)
            user.first_name = request.data["first_name"]
            user.last_name = request.data["last_name"]
            
            #clear the list
            user.groups.clear()
            #re-add everything, PUTS do that, PATCHES are partial, we should expect this.
            #this is more of a job for a serializer; thin views thick serializers was the mantra discovered
            try:
                to_add = request.data["groups"]
                for group_name in to_add:
                    try:
                        group = P_Group.objects.get(name=group_name)
                    except P_Group.DoesNotExist as dne:
                        continue
                    user.groups.add(group)
            except Exception as e:
                return Response(str(e) + "\ngroups likely not in request.data", status =400) 
                
            user.save()
            return Response("user: {0} updated successfully".format(request.data["userid"], status=200))
        
        return Response(serializer.errors, status = 400)

    def patch(self, request, format=None):
        return Response("", status=501)
