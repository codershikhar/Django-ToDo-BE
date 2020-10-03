from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TodoListSerializer, TaskSerializer
from .models import TodoList, Task
from rest_framework import status
import traceback


class ToDoViewSet(APIView):
    authentication_classes = []

    def get(self, request):
        try:
            pageCount = int(request.GET.get('pageCount', 10))
            pageNumber = int(request.GET.get('pageNumber', 1))
            todo_lists = TodoList.objects.all()[pageNumber*pageCount: (pageNumber+1)*pageCount]
            count = TodoList.objects.count()
            serializer = TodoListSerializer(todo_lists, many=True)
            return Response({'data': serializer.data, 'count': count}, status=status.HTTP_200_OK)
        except:
            traceback.print_exc()
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = TodoListSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            traceback.print_exc()
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            id = int(request.GET.get('id', None))
            if id is None:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            todo_list = TodoList.objects.filter(id=id).first()
            if todo_list is None:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            todo_list.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            traceback.print_exc()
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskViewSet(APIView):
    authentication_classes = []

    def get(self, request):
        try:
            todo_id = request.GET.get('id', '')
            tasks = Task.objects.filter(todoList_id=todo_id).all()
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        except:
            traceback.print_exc()
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                todo_list = TodoList.objects.filter(id=serializer.data['todoList']).first()
                todo_list.total += 1
                todo_list.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            traceback.print_exc()
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            id = int(request.GET.get('id', None))
            print('id', id)
            if id is None:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            task = Task.objects.filter(id=id).first()
            if task:
                todo_list = TodoList.objects.filter(id=task.todoList.id).first()
                todo_list.total -= 1
                if task.completed is True:
                    todo_list.completed -= 1
                task.delete()
                todo_list.save()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            traceback.print_exc()
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskComplete(APIView):
    authentication_classes = []

    def post(self, request):
        try:
            task_id = request.GET.get('id', '')
            task = Task.objects.filter(id=task_id).first()
            if task:
                todo_list = TodoList.objects.filter(id=task.todoList_id).first()
                if task.completed is False:
                    task.completed = True
                    todo_list.completed += 1
                else:
                    task.completed = False
                    todo_list.completed -= 1
                task.save()
                todo_list.save()
                return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)
            else:
                return Response("Task id invalid", status=status.HTTP_400_BAD_REQUEST)
        except:
            traceback.print_exc()
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
