"""
Web frontend to gitmarks for use as a bookmarklet.
"""

import sys, os
import csv

import bottle
bottle.debug(False)

from bottle import route, run, request, response, template
from gitmark import gitMark
import settings

@route("/")
def index():
    return template("index", port = settings.GITMARKS_WEB_PORT)

@route("/new")
def new():
    url = request.GET.get('url')

    return template("new", url=url, tags=None, message=None, error=None)

@route("/create", method = "POST")
def create():
    url = request.forms.get('url', '').strip()
    tags = request.forms.get('tags', '').strip()
    message = request.forms.get('message', '').strip()
    push = request.forms.get('nopush', True)

    if push == '1':
        push = False

    if not url:
        return template("new", url=url, tags=tags, message=message, error="URL is required.")

    options = {}
    options['tags'] = tags
    options['push'] = push
    options['msg']  = message

    args = [url]

    g = gitMark(options, args)

    return template("create")

@route("/tags")
def tags():
    tags = request.GET.getall('tags')
    if tags is None:
        tags = os.listdir(settings.TAG_PATH)
        return template("tagList", tags=tags, error=None)
    else:
        bookmarks = None
        for tag in tags:
            if bookmarks is None:
                bookmarks = getTag(tag)
            else:
                bookmarks = bookmarks.intersection(getTag(tag))
    return template("tags", tag=tags, bookmarks=bookmarks, error=None)

@route("/content/:contentHash")
def content(contentHash):
    f = open('%s%s' % (settings.CONTENT_PATH, contentHash), 'r')
    content = f.read()
    f.close
    return content

def getTag(tag):
    f = open('%s%s' % (settings.TAG_PATH, tag), 'r')
    bookmarkReader = csv.reader(f)
    bookmarks = []
    for bookmark in bookmarkReader:
        bookmarks.append(tuple(bookmark))
    return set(bookmarks)

run(host="localhost", port=settings.GITMARKS_WEB_PORT, reloader=False)
