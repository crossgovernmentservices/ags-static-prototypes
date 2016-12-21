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

@notify.route('/productpage2')
def product_page2():
  return render_template('notify/product_pageV2.html')

@notify.route('/prebroker')
def pre_broker():
  return render_template('notify/pre_broker.html')

@notify.route('/post-signout')
def post_sign_out():
  return render_template('notify/post_sign_out.html')

# ----------------
# Start Azure flow
# ----------------
@notify.route('/azure/productpage')
def azure_productpage():
  return render_template('notify/product_pageV2.html',
          next_url=url_for('notify.azure_pre_broker'))

@notify.route('/azure/prebroker')
def azure_pre_broker():
  return render_template('notify/pre_broker.html',
          next_url=url_for('broker.azure_request_email'))

# ----------------
# Start Okta flow
# ----------------
@notify.route('/okta/productpage')
def okta_productpage():
  return render_template('notify/product_pageV2.html',
          next_url=url_for('notify.okta_pre_broker'))

@notify.route('/okta/prebroker')
def okta_pre_broker():
  return render_template('notify/pre_broker.html',
          next_url=url_for('broker.okta_request_email'))

# ----------------
# Start CO flow
# ----------------
@notify.route('/co/productpage')
def co_productpage():
  return render_template('notify/product_pageV2.html',
          next_url=url_for('notify.co_pre_broker'))

@notify.route('/co/prebroker')
def co_pre_broker():
  return render_template('notify/pre_broker.html',
          next_url=url_for('broker.co_request_email'))
