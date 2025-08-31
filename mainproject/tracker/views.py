
from django.shortcuts import redirect, render
from .models import landing, tracker, tags, mquotes  # Import models from the tracker app
from django.http import HttpResponse
from .serializers import LandingSerializer, TrackerSerializer, TagsSerializer, MQuotesSerializer  # Import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date
from django.db.models import Count  # Import Count for aggregation
# Create your views here.
name=''
@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':      
        serializer = LandingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def login_view(request):
    print("Login view called")
    print(f"Request data: {request.data}")
    if request.method == 'POST':
        username = request.data.get('name')
        password = request.data.get('password')
        user = landing.objects.get(name=username, password=password)
        if user is not None:
            global name
            name = username
            return Response({'message': 'Login successful'}, status=200)
        else:
            return Response({'message': 'Invalid username or password'}, status=401)

@api_view(['POST'])
def addproblem_view(request):
    if request.method == 'POST':
        serializer = TrackerSerializer(data=request.data)
        print(request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def tags_view(request):
    if request.method == 'GET':
        row = tags.objects.all()
        serializer = TagsSerializer(row, many=True)
        return Response(list(serializer.data))

@api_view(['GET'])
def dashboard_view(request):
    if request.method == 'GET':
        row1 = tracker.objects.filter(user_id=name).order_by('-timestamp')[:5].values('user_id', 'activity', 'timestamp', 'status', 'tag','platform')
        row2 = tracker.objects.filter(user_id=name).values('status').annotate(count=Count('status'))
        row3 = tracker.objects.filter(user_id=name).values('tag').annotate(count=Count('tag'))
        
        
    easy = next((item['count'] for item in row2 if item['status'] == 'Easy'), 0)
    medium = next((item['count'] for item in row2 if item['status'] == 'Medium'), 0)
    hard = next((item['count'] for item in row2 if item['status'] == 'Hard'), 0)

    return Response({
        "easy": easy,
        "medium": medium, 
        "hard": hard,
        "activity": list(row1), 
        "tags": list(row3)
    }, status=200)

@api_view(['GET'])
def user_activity_view(request):
    if request.method == 'GET':
        activities = tracker.objects.filter(user=name).order_by('-timestamp').values('activity', 'timestamp', 'platform', 'link', 'description', 'status','tag')
        return Response({"activities": list(activities)}, status=200)

@api_view(['GET'])
def mquotes_view(request):
    if request.method == 'GET':
        a = date.today().day
        print(f"Today's date: {a}")
        quotes = mquotes.objects.filter(id=a).values('quote')
        return Response(quotes)
 