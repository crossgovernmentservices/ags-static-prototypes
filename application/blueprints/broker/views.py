from flask import (
  render_template,
  Blueprint,
  current_app,
  url_for)

import json

broker = Blueprint('broker', __name__, url_prefix='/broker')

@broker.route('/confirm')
def confirm():
  return render_template('confirm.html')

@broker.route('/choose')
def choose():
  return render_template('choiceofidp.html')

@broker.route('/select')
def select():
  return render_template('selectidps.html')

@broker.route('/requestemail')
def request_email():
  return render_template('knowyouremail.html')

@broker.route('/email')
def change_email():
  return render_template('changeemail.html')

@broker.route('/emailsuggestion')
def email_suggestion():
  return render_template('emailsuggestion.html')

@broker.route('/similaremailsuggestion')
def similar_email_suggestion():
  return render_template('similaremail.html')

@broker.route('/firsttime')
def first_time():
  return render_template('firstvisit.html')

# -------------
# Hand off pages
# -------------
@broker.route('/handtoidp')
def handto_idp():
  return render_template('to_idp.html')

@broker.route('/handtoservice')
def handto_service():
  return render_template('to_service.html')

@broker.route('/google-email')
def google_email():
  return render_template('fake_broker.html')

@broker.route('/google-password')
def google_password():
  return render_template('google/google_password.html')

@broker.route('/google-2fa')
def google_2fa():
  return render_template('google/google_2fa.html')

@broker.route('/google-permissions')
def google_permissions():
  return render_template('google/google_permissions.html')

# -------------
# Azure flow / screenshots
# -------------
@broker.route('/azure/requestemail')
def azure_request_email():
  return render_template('knowyouremail.html',
          next_url=url_for('broker.azure_email_confirm'))

@broker.route('/azure/email-confirm-dept')
def azure_email_confirm():
  return render_template('mvp_confirm.html',
          next_url=url_for('broker.azure_handto_idp'))

@broker.route('/azure/handtoidp')
def azure_handto_idp():
  return render_template('to_idp.html',
          next_url=url_for('broker.azure_email'))

@broker.route('/azure/email')
def azure_email():
  return render_template('screenshot_layout.html',
          onclick_url=url_for('broker.azure_2_step'),
          screenshot_url="azure/azure_email_page.png")

@broker.route('/azure/2step')
def azure_2_step():
  return render_template('screenshot_layout.html',
          onclick_url=url_for('broker.handto_service'),
          screenshot_url="azure/azure_2_step.png")

# -------------
# Okta flow / screenshots
# -------------
@broker.route('/okta/requestemail')
def okta_request_email():
  return render_template('knowyouremail.html',
          next_url=url_for('broker.okta_email_confirm'))

@broker.route('/okta/email-confirm-dept')
def okta_email_confirm():
  return render_template('mvp_confirm.html',
          next_url=url_for('broker.okta_handto_idp'))

@broker.route('/okta/handtoidp')
def okta_handto_idp():
  return render_template('to_idp.html',
          next_url=url_for('broker.okta_email'))

@broker.route('/okta/email')
def okta_email():
  return render_template('screenshot_layout.html',
          onclick_url=url_for('broker.okta_first_time'),
          screenshot_url="okta/okta_email.png")

@broker.route('/okta/firsttime')
def okta_first_time():
  return render_template('screenshot_layout.html',
          onclick_url=url_for('broker.okta_2_step'),
          screenshot_url="okta/okta_first_time.png")

@broker.route('/okta/okta2fa')
def okta_2_step():
  return render_template('screenshot_layout.html',
          onclick_url=url_for('broker.handto_service'),
          screenshot_url="okta/okta_2fa.png")

# -------------
# MVP Versions
# -------------
@broker.route('/mvp/select-idp')
def mvp_select_idp():
  with open('application/data/idps.json') as data_file:
      idps = json.load( data_file )
  return render_template('mvp_selectidps.html', idps=idps)

@broker.route('/mvp/email-confirm-dept')
def mvp_email_confirm_dept():
  return render_template('mvp_confirm.html')

@broker.route('/mvp/confirm-auto-routing')
def mvp_auto_routing():
  return render_template('mvp_confirm.html', flow='signbackin')

@broker.route('/mvp/sign-out')
def mvp_sign_out():
  return render_template('mvp_sign_out.html')