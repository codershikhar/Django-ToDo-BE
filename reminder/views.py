import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ReminderSerializer
from .models import Reminder
from rest_framework import status
import traceback
from django.views.decorators.csrf import csrf_exempt


class ListReminders(APIView):
    authentication_classes = []

    def get(self, request):
        try:
            reminders = Reminder.objects.filter(dateTime__gte=datetime.datetime.now()).order_by('dateTime').all()
            serializer = ReminderSerializer(reminders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            traceback.print_exc()
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @csrf_exempt
    def post(self, request):
        try:
            print('request.data', request.data)
            serializer = ReminderSerializer(data=request.data)
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
            reminders = Reminder.objects.filter(id=id).first()
            if reminders:
                reminders.delete()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            traceback.print_exc()
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
