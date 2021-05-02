from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User,Post,Comment,Subscribe
from .forms import UpdateProfile,PostForm,UpdatePostForm,AddComment,AddSubscriber
from .. import db,photos
from flask_login import login_required,current_user
from ..email import subcriber_mail


@main.route('/',methods=['GET','POST'])
def index():
  title = 'Blog'
  page=request.args.get('page', 1, type=int)
  recent_page= request.args.get('page', 1, type=int)
  posts = Post.query.order_by(Post.posted.asc()).paginate(page=page, per_page=6)
  recent=Post.query.order_by(Post.posted.desc()).paginate(page= recent_page, per_page=6)
  form=AddSubscriber()
  if form.validate_on_submit():
    email=form.email.data
    new_post=Subscribe(email=email)
    new_post.save_subscriber()

  return render_template('index.html', title=title, posts=posts, recent=recent,form=form)

@main.route('/profile/<uname>')
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
    subcriberList=Subscribe.query.all()
    subcribers=[]
    for subcriber in subcriberList:
      subcribers.append(subcriber.email)
    for subcriber in subcribers:
      subcriber_mail("New Blog Created!","email/subscribe",subcriber,user=current_user,post=post)

    flash("Post created successfully!")
    return redirect(url_for('main.index'))

  return render_template("create_post.html", form=form, title="New Post", legend='New Post')

#See Full Post
@main.route('/posts/<int:post_id>', methods=['GET','POST'])
@login_required
def posts(post_id):
  post=Post.query.get_or_404(post_id)
  if post is None:
    abort(404)
  all_comments = Comment.get_comments(post.id)
  comment_form = AddComment()
  if comment_form.validate_on_submit():
    comment = Comment(contents=comment_form.contents.data,user=current_user, post_id=post_id)
    comment.save_comments()

    return redirect(url_for('main.posts',post_id=post_id))
  return render_template('post.html', title=post.title, post=post, comments=all_comments, comment_form=comment_form)

#Update Post
@main.route('/posts/<int:post_id>/update', methods=['GET','POST'])
@login_required
def update_posts(post_id):
  post=Post.query.get_or_404(post_id)
  if post.user != current_user:
    abort(403)
  form = PostForm()
  if form.validate_on_submit():
    post.title=form.title.data
    post.post_content=form.post_content.data
    post.short_description=form.short_description.data
    db.session.commit()
    flash('your post has been updated!')
    return redirect(url_for('main.posts', post_id=post.id))
  elif request.method == 'GET':
    form.title.data=post.title
    form.short_description.data=post.short_description
    form.post_content.data = post.post_content
  return render_template('create_post.html', title='Update Post', form =form, legend='Update Post')

#Delete Posts
@main.route('/posts/<int:post_id>/delete', methods=['GET','POST'])
@login_required
def delete_posts(post_id):
  post=Post.query.get_or_404(post_id)
  if post.user != current_user:
    abort(403)
  db.session.delete(post)
  db.session.commit()
  flash('Your Post Has Been Deleted')
  return redirect(url_for('main.index'))

#Add Comments
@main.route('/new_comment',methods=["GET","POST"])
def new_comment():
  form=AddComment()
  if form.validate_on_submit():
    contents=form.contents.data
    user=current_user
    comment=Comment(contents=contents,user=user)
    comment.save_comments()

    
    return redirect(url_for('main.new_comment'))

  return render_template('new_comment.html',form=form)

#Delete Comment
@main.route('/del_comment/<post_id>/<comment_id>',methods=["POST","GET"])
@login_required
def delete_comment(post_id,comment_id):
  post=Post.get_posts(post_id)
  comment=Comment.get_comment(comment_id)
  if post.user != current_user:
    abort(404)
  comment.delete_comment()

  return redirect(url_for('main.posts',post_id=post.id,comment_id=comment.id))

#Function to display Blogs created by specific user
# @main.route('/user/<string:username>',methods=['GET','POST'])
# def user_posts(username):
#   title = 'Blog'
#   page=request.args.get('page', 1, type=int)
#   user = User.query.filter_by(username=username).first_or_404()
#   posts = Post.query.filter_by(user=user).order_by(Post.posted.desc()).paginate(page=page, per_page=5)
#   return render_template('user_posts.html', title=title, posts=posts, user=user)

#Function to display Blogs created by specific user.
@main.route('/user_posts/<string:username>',methods=["GET","POST"])
def user_posts(username):
  user=User.query.filter_by(username=username).first()
  posts=Post.query.filter_by(user=user).order_by(Post.posted.desc()).all()
  return redirect(url_for("main.profile",posts=posts,uname=username))