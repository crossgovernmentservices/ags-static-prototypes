# -*- coding: utf-8 -*-
"""
Flask app factory class
"""

import os

from flask import Flask, render_template, session

def create_app(config='config.py', **kwargs):
    """
    App factory function
    """

    app = Flask(__name__)
    app.config.from_pyfile(config)
    app.config.update(kwargs)

    register_blueprints(app)
    register_extensions(app)

    return app

def register_blueprints(app):
    """
    Import and register blueprints
    """

    from application.blueprints.base.views import base
    app.register_blueprint(base)

def register_extensions(app):
    """
    Import and register flask extensions and initialize with app object
    """

    from application.assets import assets
    assets.init_app(app)
