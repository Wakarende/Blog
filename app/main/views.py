from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User,Post
from .forms import UpdateProfile,PostForm,UpdatePostForm
from .. import db,photos
from flask_login import login_required,current_user


@main.route('/',methods=['GET','POST'])
def index():
  title = 'Blog'
  posts = Post.query.all()
  return render_template('index.html', title=title, posts=posts)

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

#New Post
# @main.route('/post/new', methods= ['GET','POST'])
# @login_required
# def new_post():
#   form = PostForm()
#   if form.validate_on_submit():
#     title=form.title.data
#     post_content=form.post_content.data
#     short_description=form.short_description.data
#     author_id=current_user
#     print(current_user._get_current_object().id)
#     new_post = Post(title=title,post_content=post_content,short_description=short_description,author_id=current_user)
#     db.session.add(new_post)
#     db.session.commit()

#     flash('Your Post has been created!','success')
#     return redirect(url_for('main.index'))
#   return render_template('create_post.html',title='New Post', form=form)

@main.route('/new_post', methods=['GET','POST'])
@login_required
def new_post():
  form=PostForm()
  if form.validate_on_submit():
    title=form.title.data
    post_content=form.title.data
    short_description=form.short_description.data
    user=current_user
    post=Post(title=title, post_content=post_content, user=user, short_description=short_description)
    post.save_posts()

    flash("Post created successfully!")
    return redirect(url_for('main.index'))

  return render_template("create_post.html", form=form, title="New Post")