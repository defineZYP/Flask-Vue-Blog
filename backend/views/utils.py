'''
some tools that can be used
'''
from flask import jsonify
from datetime import timedelta, datetime, timezone

tz = timezone(timedelta(hours=8))

def trans_to_json(bloglist:list, li:list):
    '''
    change the bloglist to jsonify
    @params:
        bloglist: the blogs needed or the result of a query
        li:       result
    @return:
        a jsonify of li
    '''
    for blog in bloglist:
        tgs = blog.tags.split(",")
        li.append({
            "id": blog.id,
            "title": blog.title,
            "tags": tgs,
            "author": blog.author,
            "time": blog.update_time,
            "summary": blog.summary,
            "like_num": blog.like_num,
            "cmts_num": blog.cmts_num,
        })
    return jsonify(li)

def stamp_to_datetime(time_stamp):
    '''
    translate a time stamp to date string
    format:YYYY-MM-dd hh:mm:ss
    '''
    dt = datetime.fromtimestamp(time_stamp, tz)
    time_str = dt.strftime('%Y-%m-%d %H:%M:%S')
    return time_str

def get_timestamp_now():
    '''
    get the current time stamp
    '''
    dt = datetime.now(tz)
    time_stamp = dt.timestamp()
    return str(int(time_stamp))
