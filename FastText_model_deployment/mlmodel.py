from flask import Flask, request, jsonify
import fasttext_model as model


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Ubuntu Server Online'
    
    
@app.route('/get_prediction', methods = ['POST'])
def get_sentiment():
    tx = request.get_json(force = True)
    text = tx['Comment']
    
    pred = model.get_prediction(text)
    d = dict(pred)
    for key in d:
        d[key] = str(d[key])
    
    return jsonify(result = pred)


    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True, use_reloader = False) #default port = 5000
