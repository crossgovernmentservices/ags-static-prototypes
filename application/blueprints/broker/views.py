from flask import (
  render_template,
  Blueprint,
  current_app)

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

@broker.route('/emailsuggestion')
def email_suggestion():
  return render_template('emailsuggestion.html')

@broker.route('/similaremailsuggestion')
def similar_email_suggestion():
  return render_template('similaremail.html')

@broker.route('/firsttime')
def first_time():
  return render_template('firstvisit.html')
