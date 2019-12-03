import flask
import cgi, cgitb
from flask import request, jsonify, render_template
from funcs import make_prediction

# initialize app 
app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    form = cgi.FieldStorage()
    # res_sz
    if form.getvalue('size'):
        res_sz = form.getvalue('size')
    else:
        res_sz = '2'
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
    print(res_dict)
    return render_template('index.html')

# start the server, listen for requests 
if __name__ == '__main__':
    app.run(debug=True)  # local dev
    # app.run(host='0.0.0.0')
    app.run()