from flask import (
  render_template,
  Blueprint,
  current_app)

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