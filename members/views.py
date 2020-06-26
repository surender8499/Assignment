from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Members
from .serializers import MembersSerializer


class memberList(APIView):

    def get(self, request):
        Members1 = Members.objects.all()
        serializer = MembersSerializer(Members1, many=True)
        return Response(serializer.data)

    def post(self):
        pass