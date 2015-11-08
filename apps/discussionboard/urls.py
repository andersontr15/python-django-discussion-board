from django.conf.urls import patterns, url
from apps.discussionboard import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'register$', views.register, name="register"),
	url(r'login$', views.login, name="login"),
	url(r'dashboard$', views.dashboard, name="dashboard"),
	url(r'logout$', views.logout, name="logout"),
	url(r'topic$', views.topic, name="topic"),
	url(r'^users/(?P<user_id>\d+)/$', views.show_user, name="show_user"),
	url(r'^topic/(?P<topic_id>\d+)/delete$', views.delete_topic, name="delete_topic"),
	url(r'^topics/(?P<topic_id>\d+)/edit$', views.edit_topic, name="edit_topic"),
	url(r'^topics/(?P<topic_id>\d+)/update$', views.update, name="update"),
	url(r'^topic/(?P<topic_id>\d+)/$', views.show_topic, name="show_topic"),
	url(r'^topic/(?P<topic_id>\d+)/post$', views.post_comment, name="post_comment"),
	url(r'^idea/(?P<comment_id>\d+)/$', views.post_idea, name="post_idea"),
	url(r'^upvote/(?P<comment_id>\d+)/$', views.upvote, name="upvote"),
	url(r'^downvote/(?P<comment_id>\d+)/$', views.downvote, name="downvote"),
	url(r'^delete/(?P<comment_id>\d+)/$', views.delete_comment, name="delete_comment"),
	url(r'^delete/(?P<idea_id>\d+)/comment$', views.delete_idea, name="delete_idea"),
)