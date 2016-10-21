from flask import (
  render_template,
  Blueprint,
  current_app)

local = Blueprint('local', __name__, url_prefix='/local')

@local.route('/signin')
def sign_in():
  return render_template('notify_create_account.html')