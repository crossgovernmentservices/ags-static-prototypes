from flask import (
  render_template,
  Blueprint,
  current_app)

base = Blueprint('base', __name__)

@base.route('/')
@base.route('/index')
def index():
  return render_template('index.html')

@base.route('/confirm')
def confirm():
  return render_template('confirm.html')

@base.route('/choose')
def choose():
  return render_template('choiceofidp.html')

@base.route('/select')
def select():
  return render_template('selectidps.html')

@base.route('/requestemail')
def request_email():
  return render_template('knowyouremail.html')

@base.route('/emailsuggestion')
def email_suggestion():
  return render_template('emailsuggestion.html')

@base.route('/firsttime')
def forst_time():
  return render_template('firstvisit.html')

@base.route('/product_page')
def product_page():
  return render_template('product_page.html')
