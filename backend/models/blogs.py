from ..utils import db

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.String(20), primary_key=True, nullable = False)    # id作为主键
    title = db.Column(db.String(60), nullable = False)                   # 不能为false，文章名字
    tags = db.Column(db.String(60))                                      # 文章标签
    author = db.Column(db.String(40), nullable = False)                  # 文章作者
    # create_time = db.Column(db.DateTime, server_default=db.func.now())   # 文章创建时间
    # update_time = db.Column(db.DateTime, server_default=db.func.now(), 
    #                             server_onupdate=db.func.now())           # 更新时间
    create_time = db.Column(db.String(10))
    update_time = db.Column(db.String(10))
    summary = db.Column(db.String(500))                                  # 文章简介
    body = db.Column(db.TEXT(100000), nullable = False)                  # 内容
    read_num = db.Column(db.Integer)                                     # 阅读量
    like_num = db.Column(db.Integer)                                     # 点赞数量
    cmts_num = db.Column(db.Integer)                                     # 评论数量

