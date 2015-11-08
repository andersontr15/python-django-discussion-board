from django.db import models

class User(models.Model):
	first_name = models.TextField(blank=False, max_length=20, null=True)
	last_name = models.TextField(blank=False, max_length=20,null=True)
	email = models.TextField(blank=False, max_length=20,null=True)
	description = models.TextField(blank=False, max_length=500,null=True)
	password = models.TextField(blank=False, max_length=20,null=True)
	created_at = models.DateField(null=True)
	updated_at = models.DateField(null=True)
	class Meta:
		db_table = 'user'

class Topic(models.Model):
	user = models.ForeignKey(User, related_name="topic_user")
	topic = models.TextField(blank=False, max_length=70)
	description = models.TextField(blank=False, max_length=250)
	category = models.TextField(blank=False, max_length=30)
	counter = models.IntegerField(blank=False, null=True, default=0)
	created_at = models.DateField(null=True)
	updated_at = models.DateField(null=True)
	class Meta:
		db_table = 'topic'

class Comment(models.Model):
	user = models.ForeignKey(User, related_name="comment_user")
	comment = models.TextField(blank=False, max_length=200)
	topic = models.ForeignKey(Topic, related_name="comment_topic")
	class Meta:
		db_table = 'comment'

class Idea(models.Model):
	comment = models.ForeignKey(Comment, related_name="comment_idea")
	user = models.ForeignKey(User, related_name="idea_user")
	created_at = models.DateField(null=True)
	idea = models.TextField(blank=False, max_length=200)
	class Meta:
		db_table = 'idea'

class Upvote(models.Model):
	user = models.ForeignKey(User, related_name="upvote_user", null=True)
	comment = models.ForeignKey(Comment, related_name="comment_upvote", null=True)
	counter = models.IntegerField(null=True, blank=False, default=0)
	created_at = models.DateField(null=True)
	total = models.IntegerField(null=True, blank=False)
	class Meta:
		db_table = 'upvote'

class Downvote(models.Model):
	user = models.ForeignKey(User, related_name="downvote_user", null=True)
	comment = models.ForeignKey(Comment, related_name="comment_downvote", null=True)
	created_at = models.DateField(null=True)
	counter = models.IntegerField(null=True, blank=False, default=0)
	class Meta:
		db_table = 'downvote'