from flask import *

app = Flask(__name__)

app.secret_key = 'nihardarji'

import project.com.controller
