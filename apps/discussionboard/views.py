from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from apps.discussionboard.models import User, Topic, Comment, Idea, Upvote, Downvote
from django.utils import timezone
from datetime import datetime
from collections import Counter
from django.db.models import Count


def index(request):
	print (request.GET)
	print (request.method)
	return render(request, 'discussionboard/index.html')

def register(request):
	print ("Registration")
	user = User.objects.filter(email= request.POST.get('email'), password=request.POST.get('password'))
	if len(user) > 0 and len(request.POST.get('email'))<3:
		return redirect('/')
	else:
		user = User()
		user.first_name = request.POST.get('first_name')
		user.last_name = request.POST.get('last_name')
		user.email = request.POST.get('email')
		user.description = request.POST.get('description')
		user.password = request.POST.get('password')
		user.created_at = timezone.now()
		user.save()
		print ("Successful Registration")
		print (user.first_name)
		print (user.last_name)
		print (user.email)
		print (user.password)
		return redirect('/')

def login(request):
	print ("Login")
	print (request.POST.get('email'))
	print (request.POST.get('password'))
	user = User.objects.filter(email=request.POST.get('email'))
	if len(user)<1:
		print ("Failed")
		return redirect('/')
	else:
		print ("Success")
		request.session['user_id'] = user[0].id
		print ("Logging In..")
		return redirect('/dashboard')

def dashboard(request):
	print ("User Dashboard")
	if "user_id" in request.session:
		user = User.objects.get(id=request.session['user_id'])
		current_user = User.objects.get(id=request.session['user_id'])
		topics = Topic.objects.all()[:4]
		context = { 'topics': topics,'current_user': current_user,'user': user }
		return render(request, 'discussionboard/dashboard.html', context)
	else:
		del request.session
		return redirect('/')

def topic(request):
	print ("Adding a topic")
	user = User.objects.get(id=request.session['user_id'])
	topic = Topic()
	topic.topic = request.POST.get('topic')
	topic.category = request.POST.get('category')
	topic.created_at = timezone.now()
	topic.description = request.POST.get('description')
	topic.user = user
	topic.save()
	return redirect('/dashboard')

def delete_topic(request, topic_id):
	print ("Deleting a topic..")
	topic = Topic.objects.get(id=topic_id)
	comments = Comment.objects.all().filter(topic=topic)
	ideas = Idea.objects.all().filter(comment=comments)
	ideas.delete()
	comments.delete()
	topic.delete()
	return redirect('/dashboard')

def edit_topic(request, topic_id):
	print ("Editing a topic...")
	topic = Topic.objects.get(id=topic_id)
	context = {'topic': topic}
	return render(request, 'discussionboard/edit.html', context)

def show_topic(request, topic_id):
	print ("Showing a topic")
	topic = Topic.objects.get(id=topic_id)
	comments = Comment.objects.all().filter(topic=topic)
	upvotes = Upvote.objects.all().distinct('comment_id')
	ideas = Idea.objects.all()
	downvotes = Downvote.objects.all().distinct('comment_id')
	context = {'upvotes': upvotes, 'ideas': ideas, 'comments': comments, 'topic': topic,'downvotes': downvotes}
	return render(request, 'discussionboard/show.html', context)

def update(request, topic_id):
	print ("Updating topic")
	topic = Topic.objects.get(id=topic_id)
	topic.topic = request.POST.get('topic')
	topic.description = request.POST.get('description')
	topic.category = request.POST.get('category')
	topic.updated_at = timezone.now()
	topic.save()
	return redirect('/dashboard')

def show_user(request, user_id):
	print ("showing user")
	user = User.objects.get(id=user_id)
	current_user = User.objects.get(id=request.session['user_id'])
	topics = Topic.objects.all().filter(user=user)[:1]
	comments = Comment.objects.all().filter(user=user)
	ideas = Idea.objects.all().filter(user=user)
	context = {'user': user, 'topics': topics, 'comments': comments, 'ideas': ideas, 'current_user': current_user}
	return render(request, 'discussionboard/user.html', context)

def post_comment(request, topic_id):
	print ("posting comment")
	user = User.objects.get(id=request.session['user_id'])
	topic = Topic.objects.get(id=topic_id)
	topic.counter +=1;
	topic.save()
	comment = Comment()
	comment.user = user
	comment.topic = topic
	comment.comment = request.POST.get('comment')
	comment.created_at = timezone.now()
	comment.save()
	return redirect('/dashboard')

def post_idea(request, comment_id):
	print ("posting idea")
	user = User.objects.get(id=request.session['user_id'])
	comment = Comment.objects.get(id=comment_id)
	idea = Idea()
	idea.idea = request.POST.get('idea')
	idea.created_at = timezone.now()
	idea.user = user
	idea.comment = comment
	idea.save()
	return redirect('/dashboard')

def upvote(request, comment_id):
	print ("upvoting comment")
	user = User.objects.get(id=request.session['user_id'])
	comment = Comment.objects.get(id=comment_id)
	upvote = Upvote()
	print (upvote.counter)
	upvote.comment = comment
	upvote.user = user
	upvote.created_at = timezone.now()
	upvote.counter +=1;
	upvote.save()
	print (upvote.counter)
	return redirect('/dashboard')

def downvote(request, comment_id):
	print ("downvoting comment")
	user = User.objects.get(id=request.session['user_id'])
	comment = Comment.objects.get(id=comment_id)
	downvote = Downvote()
	print (downvote.counter)
	downvote.user = user
	downvote.comment = comment
	downvote.created_at = timezone.now()
	downvote.save()
	downvote.counter-=1;
	downvote.save()
	return redirect('/dashboard')

def delete_comment(request, comment_id):
	print ("deleting comment")
	comment = Comment.objects.get(id=comment_id)
	ideas = Idea.objects.all().filter(comment=comment)
	ideas.delete()
	comment.delete()
	return redirect('/dashboard')

def delete_idea(request, idea_id):
	print ("deleting idea")
	idea = Idea.objects.get(id=idea_id)
	idea.delete()
	return redirect('/dashboard')

def logout(request):
	print ("Logging Out")
	del request.session['user_id']
	return redirect('/')