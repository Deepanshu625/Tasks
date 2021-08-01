from django.shortcuts import render
from django.contrib.auth.models import User
from todo.models import TODO
from todo.serializers import TodoSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views import View
import io
from rest_framework.parsers import JSONParser
from django.views.decorators import csrf


class TodoAllView(View):

    def get(self, request):
        print("User:", request.user)
        username = request.GET.get("username", "")
        user = User.objects.filter(username=username).first()

        todo_object = TODO.objects.filter(user=user)
        serialized_data = TodoSerializer(todo_object, many=True)
        json_renderer = JSONRenderer().render(serialized_data.data)
        return HttpResponse(json_renderer)


class TodoView(View):

    def get(self, request):
        username = request.GET.get("username", "")
        user = User.objects.filter(username=username).first()

        pk = request.GET.get("id")
        todo_object = TODO.objects.get(id=pk)
        serialized_data = TodoSerializer(todo_object)
        json_renderer = JSONRenderer().render(serialized_data.data)
        return HttpResponse(json_renderer)


    def post(self, request):
        username = request.GET.get("username", "")
        user = User.objects.filter(username=username).first()

        json_data = request.body
        stream = io.BytesIO(json_data)
        request_data = JSONParser().parse(stream)
        data = {
            "title": request_data.get("title"),
            "details": request_data.get("details"),
            "favorite": request_data.get("bookmark"),
            "user": user,
        }

        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            json_data = JSONRenderer().render({
                "status": True,
                "message": "Successfully Created."
            })

            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render({
                "status": False,
                "message": "Failed."
            })
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request):
        username = request.GET.get("username", "")
        user = User.objects.filter(username=username).first()

        json_data = request.body
        stream = io.BytesIO(json_data)
        request_data = JSONParser().parse(stream)
        pk = request_data.get("id", "")

        obj = TODO.objects.filter(id=pk, user=user).first()
        if not obj:
            return HttpResponse("Todo didn't exist.")

        data = {
            "title": request_data.get("title", obj.title),
            "details": request_data.get("details", obj.details),
            "favorite": request_data.get("bookmark", obj.favorite)
        }

        serializer = TodoSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return HttpResponse('updated successfully')

    def delete(self, request):
        username = request.GET.get("username", "")
        user = User.objects.filter(username=username).first()

        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        pk = python_data.get('id')
        obj = TODO.objects.get(id=pk, user=user)
        obj.delete()
        return HttpResponse('deleted'+ str(pk))
