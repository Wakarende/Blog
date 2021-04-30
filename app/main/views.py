from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..requests import get_quote

@main.route('/',)
def index():
  quote = get_quote()
  title = 'Blog'
  return render_template('index.html', title=title, quote=quote)