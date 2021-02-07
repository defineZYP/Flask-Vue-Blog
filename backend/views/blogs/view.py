'''
view file of blogs
it is about an overview, not about a people
'''
import os
import sys
import time
import os
from configparser import RawConfigParser
from flask import request, jsonify

from ...models.blogs import Blog
from ..utils import trans_to_json
from . import blogs

@blogs.route("/hot/list/<int:page>")
def hot_blog_list(page):
    '''
    get the hotest blogs
    return: list of blogs which have the most reading
    '''
    li = []
    bloglist = Blog.query.order_by(Blog.read_num.desc()).offset((page-1)*20).limit(20)
    return trans_to_json(bloglist, li)

@blogs.route("/tag/<tag>/list/<int:page>")
def get_tag_list(tag, page):
    '''
    get the list of blogs which have the target tag
    return: the list of blogs 
    '''
    li = []
    bloglist = Blog.query.filter_by(tags=tag).offset((page-1)*20).limit(20)
    return trans_to_json(bloglist, li)

@blogs.route("/search/<key_word>/list/<int:page>")
def silly_search(key_word, page):
    '''
    search something contain key_word
    return: list of the blogs which contain the key_word
    '''
    li = []
    bloglist = Blog.query.like('%' + key_word + '%').offset((page-1) * 20).limit(20)
    return trans_to_json(bloglist, li)
