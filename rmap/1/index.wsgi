# coding=utf-8
# Author: shawn0lee0
# Mail: run-map@googlegroups.com

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import sae
from myApp import app

application = sae.create_wsgi_app(app)

