from rest_framework import generics
from ..models import Application
from .serializers import ApplicationSerializer
from rest_framework.viewsets import GenericViewSet


# return a list of all applications
class ApplicationListView(generics.ListAPIView, GenericViewSet):
    """
    View to return a list of all applications.
    """

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


# create a new application
class ApplicationCreateView(generics.CreateAPIView, GenericViewSet):
    """
    View to create a new application.
    """

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    # add the user to the application, using their discord id from the request
    def perform_create(self, serializer):
        serializer.save(user=self.request.user.discord_id)
    