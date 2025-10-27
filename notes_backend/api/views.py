from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Note
from .serializers import NoteSerializer


@api_view(['GET'])
def health(request):
    """
    PUBLIC_INTERFACE
    Health check endpoint.

    Returns:
        200 OK with a simple JSON message confirming server availability.
    """
    return Response({"message": "Server is up!"})


class NoteViewSet(viewsets.ModelViewSet):
    """
    PUBLIC_INTERFACE
    A viewset providing standard actions to Create, List, Retrieve, Update and Delete notes.

    Endpoints:
    - POST /api/notes/ : create a note
    - GET /api/notes/ : list notes
    - GET /api/notes/{id}/ : retrieve a note
    - PUT/PATCH /api/notes/{id}/ : update a note
    - DELETE /api/notes/{id}/ : delete a note
    """
    queryset = Note.objects.all().order_by("-updated_at")
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="List notes",
        operation_description="Returns a list of notes ordered by latest updated.",
        responses={200: NoteSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a note",
        operation_description="Create a note with title and optional content.",
        request_body=NoteSerializer,
        responses={201: NoteSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a note",
        operation_description="Retrieve a single note by ID.",
        responses={200: NoteSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a note",
        operation_description="Update a note by ID with full or partial data.",
        request_body=NoteSerializer,
        responses={200: NoteSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a note",
        operation_description="Partially update a note by ID.",
        request_body=NoteSerializer,
        responses={200: NoteSerializer()}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a note",
        operation_description="Delete a note by ID.",
        responses={204: openapi.Response(description="Deleted")}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
