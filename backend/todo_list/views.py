# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view()
# def list_view(request):
#     return Response({"message": "List View!"})
import logging
from rest_framework.response import Response
from .models import TodoList, Folder
from .serializers import TodoListSerializer, FolderSerializer
from rest_framework import generics
from api.mixins import (IsStaffEditorMixin, UserQuerySetMixin)
logger = logging.getLogger(__name__)

class TodoListDetailView(IsStaffEditorMixin, generics.RetrieveAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


    def handle_exception(self, exc):
        logger.error("An error occurred during creation: %s", str(exc))
        return super().handle_exception(exc)


class TodoListView(UserQuerySetMixin, generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    def perform_create(self,serializer):
         serializer.save(user=self.request.user)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        user = self.request.user
        return qs.filter(user=user)
        


class TodoListUpdateView(generics.UpdateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    # permission_classes = [IsAdminUser]

class TodoListDeleteView(generics.DestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    # permission_classes = [IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"id": pk, "message": f"To-do List has been deleted"}, status=204)
        except Exception as e:
                error_message = str(e)
                return Response({"message": "An error has occurred", "error": error_message}, status=400)

class FolderListView(generics.ListCreateAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    # permission_classes = [IsAdminUser]
    

class FolderDetailView(generics.RetrieveAPIView):
    queryset = Folder.objects.all()
    serializer_class = Folder
    # permission_classes = [IsAdminUser]


class FolderUpdateView(generics.UpdateAPIView):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    # permission_classes = [IsAdminUser]

class FolderDeleteView(generics.DestroyAPIView):
    queryset = Folder.objects.all()
    serializer_class = TodoListSerializer

    # permission_classes = [IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"id": pk, "message": f"Folder has been deleted"}, status=204)
        except Exception as e:
                error_message = str(e)
                return Response({"message": "An error has occurred", "error": error_message}, status=400)