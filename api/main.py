import flask
from flask import request, jsonify
from flask_cors import CORS
from data import *

# TODO (if i end up following up with this)
# ADD API TOKENS TO PROTECT TUTOR DATA

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/tutors/all', methods=['GET'], endpoint='api_all')
def api_all():
    return jsonify(tutors)

@app.route('/api/v1/tutors/opentimes', methods=['GET'])
def open_times():
    times = []
    for tutor in tutors:
        tutor_times = tutor["open-times"]
        formatted = ["-".join(x) for x in tutor_times]
        for x in formatted:
            if x not in times:      
                times.append(x)
                # making sure we don't add duplicate
                # maybe in future we add feature where it shows how many tutors availible at specific time slot?
    return jsonify(times)

# general "which tutors teach math"
@app.route('/api/v1/tutors/math', methods=['GET'])
def math_tutors():
    return jsonify([tutor for tutor in tutors if "math" in tutor["broad-subjs"]])


# general "which tutors teach math"
@app.route('/api/v1/tutors/eng', methods=['GET'])
def eng_tutors():
    return jsonify([tutor for tutor in tutors if "eng" in tutor["broad-subjs"]])


# general "which tutors teach math"
@app.route('/api/v1/tutors/wl', methods=['GET'])
def wl_tutors():
    return jsonify([tutor for tutor in tutors if "wl" in tutor["broad-subjs"]])


# general "which tutors teach math"
@app.route('/api/v1/tutors/sci', methods=['GET'])
def sci_tutors():
    return jsonify([tutor for tutor in tutors if "sci" in tutor["broad-subjs"]])

app.run()