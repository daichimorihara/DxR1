from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
from .utils import getNoteList, getNoteDetail, updateNote, deleteNote, createNote
 

# Create your views here.
@api_view(['GET', 'POST'])
def getRoutes(request):

    routes = [
        {"body": "ionbnobwr",
        "update": "oweojnnovewnvjwe"}
    ]

    return Response(routes)







@api_view(['GET', 'POST'])
def getNotes(request):
    if request.method == 'GET':
        return getNoteList(request)
    
    if request.method == 'POST':
        return createNote(request)
    # notes = Note.objects.all()
    # serializer = NoteSerializer(notes, many=True)
    # return Response(serializer.data)






@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):

    if request.method == 'GET':
        return getNoteDetail(request, pk)
    
    if request.method == 'PUT':
        return updateNote(request, pk)
    
    if request.method == 'DELETE':
        return deleteNote(request, pk)

    # if request.method == "GET":
    #     note = Note.objects.get(id=pk)
    #     serializer = NoteSerializer(note, many=False)
    #     return Response(serializer.data)
    
    # if request.method == "PUT":
    #     data = request.data
    #     note = Note.objects.get(id=pk)
    #     serializer = NoteSerializer(instance=note, data=data)

    #     if serializer.is_valid():
    #         serializer.save()

    #     return Response(serializer.data)                







# @api_view(['PUT'])
# def updateNote(request, pk):
#     data = request.data
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance=note, data=data)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)