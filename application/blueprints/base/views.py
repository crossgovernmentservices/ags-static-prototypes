import json

from flask import (
  render_template,
  Blueprint,
  current_app)

base = Blueprint('base', __name__)

@base.route('/')
@base.route('/index')
def index():
  return render_template('index.html')

@base.route('/product_page')
def product_page():
  return render_template('product_page.html')

@base.route('/dex-example')
def dex_example():
  with open('application/data/idps.json') as data_file:
      idps = json.load( data_file )
  return render_template('dex.html', idps=idps)
