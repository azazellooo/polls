from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Poll
from .serializers import PollListSerializer, PollCreateSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'polls/': reverse('polls', request=request, format=format),
    })

class PollsGetCreateView(viewsets.ModelViewSet):
    serializer_class = PollListSerializer
    permission_classes = [AllowAny]
    queryset = Poll.objects.filter(date_end=None)


    def get_permissions(self):
        if self.request.method == 'POST':
            self.serializer_class = PollCreateSerializer
            return [IsAdminUser()]
        return super(PollsGetCreateView, self).get_permissions()

# Create your views here.
