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

@app.route('/api/v1/tutors/opentimes/', methods=['GET'])
def broad_open_times():
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

@app.route('/api/v1/tutors/opentimes/math', methods=['GET'])
def open_math():
    times = []
    for tutor in tutors:
        if "math" in tutor["broad-subjs"]:
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
def subj_tutor():
    subj = request.args.get("subj")
    return jsonify([tutor for tutor in tutors if subj in tutor["broad-subjs"]]) if subj in ["math", "eng", "wl", "sci"] else jsonify({"ERROR": f"invalid subject {subj} request"})


app.run()