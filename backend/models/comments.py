from ..utils import db

class COMMENT(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.String(20), primary_key = True, nullable = False)   # 主键，评论的id
    blog_id = db.Column(db.String(20), nullable = False)                  # 评论的是哪一篇文章
    content = db.Column(db.TEXT(10000), nullable = False)                 # 评论的内容
    author = db.Column(db.String(20))                                     # 发表这个评论的人
    like_num = db.Column(db.Integer)                                      # 点赞的人
    # create_time = db.Column(db.DateTime, server_default=db.func.now())    # 创建时间
    create_time = db.Column(db.String(10))
