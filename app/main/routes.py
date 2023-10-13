from app import db
from app.main import bp
from flask import render_template, url_for, flash, redirect, request, current_app
from app.main.forms import PostForm,EditProfileForm
from flask_login import current_user,  login_required
from app.models import User, Post
from datetime import datetime


# Update the last time a user was seen
@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is live')
        return redirect(url_for('main.index'))
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page=page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('main.index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template(
        'main/index.html',
        title='Make a post',
        form=form,
        posts=posts.items,
        next_url=next_url,
        prev_url=prev_url)


@bp.route('/profile/<username>', methods=['GET', 'POST'])
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page=page, per_page=current_app.config['POSTS_PER_PAGE'], error_out=False)
    next_url = url_for('main.profile', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.profile', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None
    return render_template(
        'main/profile.html',
        title='Profile',
        user=user,
        posts=posts.items,
        prev_url=prev_url,
        next_url=next_url)


@bp.route('/edit-profile/<username>', methods=['GET', 'POST'])
@login_required
def edit_profile(username):
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('main.profile', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('main/edit_profile.html', title='Edit Profile', form=form)
