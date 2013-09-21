from flask import Flask, request, redirect, url_for,render_template, session
import os
import math
from pantiltcmd import *

app=Flask(__name__)

SECRET_KEY = "secret secret"

app.config.from_object(__name__)

radius = 400
connected = True

device = None

@app.route("/",methods=["GET"])
def home():	
	return render_template("ui.html",radius=radius)

@app.route("/move",methods=["POST"])
def move():
	try:
		x = int(request.form.get("x"))
		y = int(request.form.get("y"))
		if device:
			device.move_servos(x/float(radius), y/float(radius))
		else:
			return "false"
	except Exception as e:
		raise e
		return "false"
	return "true"


if __name__ == '__main__':
    try:
    	device = BraduinoUSBCommunicator()
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as e:
        app.logger.debug("%s"%e)