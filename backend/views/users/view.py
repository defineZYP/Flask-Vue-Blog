'''
view file of an spicific user and his or her blogs
'''
import os
import sys
import time
import os
from datetime import datetime
from configparser import RawConfigParser
from flask import request, jsonify, make_response
from flask_login import login_required, current_user

from ...models.blogs import Blog
from ...models.users import User
from ...utils import app, db
from ..utils import trans_to_json, get_timestamp_now
from . import users

@users.route("/<username>/home/")
def info(username):
    '''
    get an user's base information
    return: json of his or her information
    '''
    li = []
    userinfo = User.query.filter_by(username=username).first()
    li.append({
        "username": userinfo.username,
        "name": userinfo.name,
        "self_intro": userinfo.self_intro,
    })
    return jsonify(li)

@users.route("/<username>/blogs/list/<int:page>")
@login_required
def hot_blog_list(username, page):
    '''
    get an user's hotest blogs
    return: json of his or her blogs with most reading
    '''
    li = []
    bloglist = Blog.query.filter_by(author=username).offset((page-1)*20).limit(20)
    return trans_to_json(bloglist, li)

@users.route("/<username>/blogs/tags/<tag>/list/<int:page>")
@login_required
def get_tag_list(username, tag, page):
    '''
    get the list of blogs which have the target tag
    return: the list of blogs
    '''
    li = []
    bloglist = Blog.query.filter_by(author=username).filter_by(tags=tag).offset((page-1)*20).limit(20)
    return trans_to_json(bloglist, li)

@users.route('/<username>/blogs/create/', methods=['GET', 'POST'])
@login_required
def create_blog(username):
    if request.method == "POST":
        # otherwise, we can get some information from the request
        # and generate a new blog
        # and save it into our database
        title = request.form.get('title')
        tags = request.form.get('tags')
        author = username
        create_time = get_timestamp_now()
        update_time = create_time
        summary = request.form.get('summary')
        body = request.form.get('body')
        read_num = like_num = cmts_num = 0
        blog = Blog(
            title = title,
            tags = tags,
            author = author,
            create_time = create_time,
            update_time = update_time,
            summary = summary,
            body = body,
            read_num = read_num,
            like_num = like_num,
            cmts_num = cmts_num
        )
        db.session.add(blog)
        db.session.commit()
        return make_response(f"success create a new blog", 200)
    else:
        return "GET"

@users.route('/<username>/blogs/edit/<bid>', methods=['GET', 'POST'])
@login_required
def edit(username, bid):
    # we must search if there is some blog's id is bid
    blog = Blog.query.get_or_404(bid)
    if request.method == "POST":
        title = request.form['title']
        tags = request.form['tags']
        update_time = get_timestamp_now()
        summary = request.form['summary']
        body = request.form['body']
        blog.title = title
        blog.tags = tags
        blog.update_time = update_time
        blog.summary = summary
        blog.body = body
        db.session.commit()
        return make_response(f"success edit the blog {bid}", 200)
    else:
        return "GET"