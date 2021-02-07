USE amadeus;

CREATE TABLE blogs (
    id varchar(20) NOT NULL COMMENT '文章id',
    title varchar(60) NOT NULL COMMENT '文章标题',
    tags varchar(60) COMMENT '标签',
    author varchar(40) NOT NULL COMMENT '作者用户名',
    create_time varchar(10) COMMENT '创建时间',
    update_time varchar(10) COMMENT '更新时间',
    summary varchar(500) COMMENT '内容简介',
    body mediumtext NOT NULL COMMENT '文章内容',
    read_num int(10) COMMENT '阅读量',
    like_num int(10) COMMENT '点赞数量',
    cmts_num int(10) COMMENT '评论数量',
    PRIMARY KEY (id)
)ENGINE=InnoDB CHARSET=utf8mb4;

CREATE TABLE comments (
    id varchar(20) NOT NULL COMMENT '评论的id',
    blog_id varchar(20) NOT NULL COMMENT '评论的是哪一个文章',
    content text NOT NULL COMMENT '评论的内容',
    author varchar(20) COMMENT '评论的人 可以为空表示游客',
    like_num int(10) COMMENT '点赞数量',
    create_time varchar(10) COMMENT '创建时间',
    PRIMARY KEY (id)
)ENGINE=InnoDB CHARSET=utf8mb4;

CREATE TABLE users (
    id varchar(20) NOT NULL COMMENT '用户id',
    name varchar(40) NOT NULL COMMENT '昵称',
    username varchar(40) NOT NULL COMMENT '用户名',
    user_password_hash varchar(128) COMMENT '密码散列',
    admin bool COMMENT '是否拥有管理员权限',
    self_intro TEXT COMMENT '自我介绍之类的',
    PRIMARY KEY (id)
)ENGINE=InnoDB CHARSET=utf8mb4;
