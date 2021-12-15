from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns


from .views import PollsGetCreateView, api_root


urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('polls/', PollsGetCreateView.as_view({'get': 'list', 'post': 'create'}), name='polls'),
])