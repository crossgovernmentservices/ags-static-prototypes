from flask import (
  render_template,
  Blueprint,
  current_app)

local = Blueprint('local', __name__, url_prefix='/local')

@local.route('/signin')
def sign_in():
  return render_template('local_idp/signin.html')

@local.route('/create')
def create_account():
  return render_template('local_idp/create_account.html')