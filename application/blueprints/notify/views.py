from flask import (
  render_template,
  Blueprint,
  current_app,
  url_for)

notify = Blueprint('notify', __name__, url_prefix='/notify')

@notify.route('/register')
def register_account():
  return render_template('notify/create_account.html')

@notify.route('/productpage')
def product_page():
  return render_template('notify/product_page.html')

@notify.route('/prebroker')
def pre_broker():
  return render_template('notify/pre_broker.html')

@notify.route('/post-signout')
def post_sign_out():
  return render_template('notify/post_sign_out.html')

@notify.route('/azure/productpage')
def azure_productpage():
  return render_template('notify/product_page.html',
          next_url=url_for('notify.azure_pre_broker'))

@notify.route('/azure/prebroker')
def azure_pre_broker():
  return render_template('notify/pre_broker.html',
          next_url=url_for('broker.azure_request_email'))