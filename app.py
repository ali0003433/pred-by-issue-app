import flask
from flask import request, jsonify
from funcs import make_prediction

# initialize app 
app = flask.Flask(__name__)

@app.route("/", methods=['POST'])
def print_piped():
    if request.form['mes']:
        msg = request.form['mes']
        print(msg)
        x_input, pred_class, pred_proba = make_prediction(str(msg))
        flask.render_template('index.html',chat_in=x_input,prediction_class=pred_class,prediction_prob=pred_proba)
    return jsonify(pred_class)

@app.route('/', methods=['GET'])
def predict():
    # request.args contains arguments from the form
    print(request.args)
    if (request.args):
        x_input, pred_class, pred_proba = make_prediction(request.args['chat_in'])
        print(x_input)
        return flask.render_template('index.html',
                                     chat_in=x_input,
                                     prediction_class=pred_class, 
                                     prediction_prob=pred_proba)
    else:
        # first load, request.args will be empty immutabledict type, don't throw error
        return flask.render_template('index.html', 
                                     chat_in='', 
                                     prediction_class='',
                                     prediction_proba='')

# start the server, listen for requests 
if __name__ == '__main__':
#     app.run(debug=True)  # local dev
    app.run(host='0.0.0.0')
    app.run()
