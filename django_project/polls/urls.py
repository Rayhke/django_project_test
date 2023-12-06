from django.urls import path
from .views import IndexView, DetailView, ResultsView, VoteView
# from . import views

app_name = "polls"
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', VoteView.as_view(), name='vote'),
    # path("", views.PollsModelView.as_view(), name="index"),
    # path("choice/", views.ChoiceList.as_view(), name="choice_list"),
    # path("question/", views.Question.as_view(), name="question_list"),
    # path("choice/<int:pk>/", views.ChoiceDetail.as_view(), name="choice_detail"),
    # path("question/<int:pk>/", views.Question.as_view(), name="question_detail"),
    # path("", views.index, name="index"),
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/results/", views.results, name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]
