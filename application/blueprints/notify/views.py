from flask import (
  render_template,
  Blueprint,
  current_app)

notify = Blueprint('notify', __name__, url_prefix='/notify')

@notify.route('/register')
def register_account():
  return render_template('notify_create_account.html')

@notify.route('/productpage')
def product_page():
  return render_template('product_page.html')