from ..utils import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String(20), primary_key = True, nullable = False)     # 用户id唯一
    name = db.Column(db.String(40), nullable = False)                       # 昵称
    username = db.Column(db.String(40), nullable = False)                   # 用户名
    user_password_hash = db.Column(db.String(128))                          # 密码
    admin = db.Column(db.Boolean)                                           # 是否是管理员
    self_intro = db.Column(db.TEXT(10000))                                  # 自我介绍之类的s
    
    def set_password(self, password):
        '''
        set password
        '''
        self.user_password_hash = generate_password_hash(password) 

    def validate_password(self, password):
        '''
        validate password
        '''
        return check_password_hash(self.user_password_hash, password)   
               
@login_manager.user_loader
def load_user(user_id):
    '''
    load user
    '''
    return User.query.get(user_id)