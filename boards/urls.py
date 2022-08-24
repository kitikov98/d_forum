from django.urls import path

from . import views

app_name = "boards"
urlpatterns = [
    path('', views.BoardListView.as_view(), name='index'),
    path('topics/<int:pk>/', views.TopicListView.as_view(), name='boards_topics'),
    path('topics/<int:pk>/new/', views.new_topic, name='new_topic'),
    path('question/', views.IndexView.as_view(), name='question'),
    path('question/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('question/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('question/<int:question_id>/vote/', views.vote, name='vote'),
    path('topics/<int:pk>/<int:topic_pk>/', views.PostListView.as_view(), name='topic_posts'),
    path('topics/<int:pk>/<int:topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    path('topics/<int:pk>/<int:topic_pk>/posts/<post_pk>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
    path('new_post/', views.NewPostView.as_view(), name='new_post'),


]

