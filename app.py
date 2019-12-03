import flask
from flask import request, jsonify, render_template
from funcs import make_prediction

# initialize app 
app = flask.Flask(__name__)

@app.route('/', methods=['POST'])
def survey_page():
    if request.method == 'POST': 
        print(request.form)
        print('printing post')
        res_size = request.form.get('size')
        res_racial = request.form.get('racial')
        res_climate = request.form.get('climate')
        res_budget = request.form.get('budget')
        res_immigration = request.form.get('immigration')
        res_terrorism = request.form.get('terrorism')
        res_gender = request.form.get('gender')
        print('res_size:', res_size, 'res_racial:', res_racial, 'res_climate:', res_climate, 'res_terrorism:', res_terrorism, 'res_budget:', res_budget, 'res_immigration:', res_immigration, 'res_gender:', res_gender)
        return 'submitted form'
    else:
        return flask.render_template('index.html')

@app.route('/', methods=['GET'])
def render_page():
    if request.args:
        print(request.args)
        prediction = make_prediction()
        print(prediction)
        return flask.render_template('res.html')
    else: 
        return flask.render_template('index.html')
# start the server, listen for requests 
if __name__ == '__main__':
    app.run(debug=True)  # local dev
    # app.run(host='0.0.0.0')
    app.run()