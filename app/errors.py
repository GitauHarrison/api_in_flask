from app import app, db
from flask import render_template


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', title='Page Not Found'), 404


@app.errorhandler(500)
def not_found(error):
    db.session.rollback()
    return render_template('500.html', title='Unexpected Error'), 500
