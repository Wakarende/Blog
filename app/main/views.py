from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User,Post
from .forms import UpdateProfile,PostForm
from .. import db,photos
from flask_login import login_required


@main.route('/')
def index():
  title = 'Blog'
  return render_template('index.html', title=title)

@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()

  if user is None:
    abort(404)

  return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
  user = User.query.filter_by(username = uname).first()
  if user is None:
    abort(404)

  form = UpdateProfile()

  if form.validate_on_submit():
    user.bio = form.bio.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile',uname=user.username))

  return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
  user = User.query.filter_by(username = uname).first()
  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.profile_pic_path = path
    db.session.commit()
  return redirect(url_for('main.profile',uname=uname))

#Post Display
@main.route("/post/<int:id>", methods = ["POST", "GET"])
def post(id):
    post = Post.query.filter_by(id = id).first()
    return redirect(url_for("main.post", id = post.id))


#New Post
@main.route("/post/new", methods = ["POST", "GET"])
@login_required
def new_post():
  post_form = PostForm()
  if post_form.validate_on_submit():
      post_title = post_form.title.data
      post_form.title.data = ""
      post_content = post_form.post.data
      post_form.post.data = ""
      new_post = Post(post_title = post_title,
                      post_content = post_content,
                      posted_at = datetime.now(),
                      post_by = current_user.username,
                      user_id = current_user.id)
      new_post.save_post()
      return redirect(url_for("main.post", id = new_post.id))
    
  return render_template("new_post.html",
                            post_form = post_form)

@main.route("/post/<int:id>/update", methods = ["POST", "GET"])
@login_required
def edit_post(id):
  post = Post.query.filter_by(id = id).first()
  edit_form = UpdatePostForm()

  if edit_form.validate_on_submit():
    post.post_title = edit_form.title.data
    edit_form.title.data = ""
    post.post_content = edit_form.post.data
    edit_form.post.data = ""

    db.session.add(post)
    db.session.commit()
    return redirect(url_for("main.post", id = post.id))

    return render_template("edit_post.html", 
                            post = post,
                            edit_form = edit_form)