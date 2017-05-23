# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post
# Create your views here.
def postList(request):
	post_list = Post.objects.all()
	context = {
		"title": "posts list",
		"postlist": post_list,
	}
	return render(request, "posts/post_list.pug", context)