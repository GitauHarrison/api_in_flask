from app.api import bp
from app.models import Post, User
from flask import jsonify, request, url_for
from app import db
from app.api.errors import bad_request


@bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    return jsonify(Post.query.get_or_404(id).to_dict())


@bp.route('/posts', methods=['GET'])
def get_posts():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = Post.to_collection_dict(Post.query, page, per_page, 'api.get_posts')
    return jsonify(data)


@bp.route('/posts/user/<int:id>', methods=['POST'])
def create_post(id):
    data = request.get_json() or {}
    user = User.query.get_or_404(id)
    if 'title' not in data or 'body' not in data:
        return bad_request('title and body fields must be included.')
    post = Post(title=data['title'], body=data['body'], author=user)
    db.session.add(post)
    db.session.commit()
    response = jsonify(post.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_post', id=post.id)
    return response


@bp.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    post = Post.query.get_or_404(id)
    data = request.get_json() or {}
    post.from_dict(data)
    db.session.commit()
    return jsonify(post.to_dict())


@bp.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10), 100)
    data = Post.to_collection_dict(Post.query, page, per_page, 'api.get_posts')
    return jsonify(data)
