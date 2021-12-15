from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns


from .views import PollsGetCreateView, api_root, PollDetail, QuestionCreateView, TakeAPollView, UserRelatedPolls


urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('polls/', PollsGetCreateView.as_view({'get': 'list', 'post': 'create'}), name='polls'),
    path('poll/<int:pk>', PollDetail.as_view(), name='poll'),
    path('question/create', QuestionCreateView.as_view(), name='question-create'),
    path('take-a-poll/', TakeAPollView.as_view(), name='take-a-poll'),
    path('<int:pk>/polls', UserRelatedPolls.as_view(), name='user-related-polls')
])