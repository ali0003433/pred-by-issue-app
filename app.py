import flask
import cgi, cgitb
from flask import request, jsonify
from funcs import make_prediction

# initialize app 
app = flask.Flask(__name__)


@app.route("/", methods=['POST'])

# def print_piped():
#     if request.form['mes']:
#         msg = request.form['mes']
#         print(msg)
#         x_input, pred_class, pred_proba = make_prediction(str(msg))
#         flask.render_template('index.html',chat_in=x_input,prediction_class=pred_class,prediction_prob=pred_proba)
#     return jsonify(pred_class)

@app.route('/', methods=['GET'])
def predict():
    form = cgi.FieldStorage()
    # res_sz
    if form.getvalue('size'):
        res_sz = form.getvalue('size')
    else:
        res_sz = '8'
    # res_rc
    if form.getvalue('racial'):
        res_rc = form.getvalue('racial')
    else:
        res_rc = '8'
    #res_clm
    if form.getvalue('climate'):
        res_clm = form.getvalue('climate')
    else:
        res_clm = '8'
    # res_bgt
    if form.getvalue('budget'):
        res_bgt = form.getvalue('budget')
    else:
        res_bgt = '8'
    # res_imm
    if form.getvalue('immigration'):
        res_imm = form.getvalue('immigration')
    else: 
        res_imm = '8'
    # res_trr
    if form.getvalue('terrorism'):
        res_trr = form.getvalue('terrorism')
    else:
        res_trr = '8'
    # res_gdr
    if form.getvalue('gender'):
        res_gdr = form.getvalue('gender')
    else:
        res_gdr = '8'
    res_dict = {'res_sz': res_sz, 'res_rc': res_rc, 'res_clm': res_clm, 'res_bgt': res_bgt, 'res_imm': res_imm, 'res_trr': res_trr, 'res_gdr': res_gdr}
    return res_dict


    # # request.args contains arguments from the form
    # print(request.args)
    # if (request.args):
    #     x_input, pred_class, pred_proba = make_prediction(request.args['chat_in'])
    #     print(x_input)
    #     return flask.render_template('index.html',
    #                                  chat_in=x_input,
    #                                  prediction_class=pred_class, 
    #                                  prediction_prob=pred_proba)
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
