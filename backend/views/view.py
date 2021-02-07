'''
some global view func
'''
import os
import sys
import time
import os
from configparser import RawConfigParser
from flask import request, jsonify, make_response
from flask_login import login_user, logout_user, current_user, login_required

from ..utils import app, db
from ..models.users import User

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            resp = make_response('错误的用户名或密码，请重试', 400)
            return resp
        else:
            user = User.query.filter_by(username=username).first()
            if user is None:
                resp = make_response('错误的用户名或密码，请重试', 400)
                return resp
            elif user.validate_password(password):
                login_user(username)
                ret_dict = {
                    'user_id': username,
                }
                resp = make_response(jsonify(ret_dict), 200)
                return resp
    else:
        return "GET"

@app.route("/logout")
@login_required
def logout():
    '''
    log out the current user
    '''
    if current_user is not None:
        logout_user()
        resp = make_response("success", 200)
        return resp
    else:
        resp = make_response("ERROR: you can't logout before login", 400)
        return resp
