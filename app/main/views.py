from flask import render_template,request,redirect,url_for,abort,flash
from . import main

@main.route('/')
def index():
  title = 'Blog'
  return render_template('index.html', title=title)