#!/usr/bin/env python

from app import app
from flask.ext.cors import CORS
cors = CORS(app)

if __name__=="__main__":
	app.run(debug=True)
