from models import Contact
from rest_framework import viewsets
from serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited.
    """
    queryset = Contact.objects.all().order_by('-date_added')
    serializer_class = ContactSerializer