#!/usr/bin/env python
# encoding: utf-8
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from flask import Flask
from app.sql_backend_blueprint import sql_backend

flask_app = Flask('__name__')
flask_app.register_blueprint(sql_backend)
flask_app.run()
