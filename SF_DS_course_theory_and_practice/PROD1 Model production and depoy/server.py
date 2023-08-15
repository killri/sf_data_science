import datetime
import pickle
import numpy as np

from flask import Flask, request, jsonify


with open('model.pkl', 'rb') as pkl_file:
    loaded_model = pickle.load(pkl_file)
        
app = Flask(__name__)
#@app.route('/hello')
#def hello_func():
#    name = request.args.get('name')
#    return f'hello, {name}!'

#@app.route('/time')
#def current_time():
#    now = datetime.datetime.now()
#    d = {'time': now}
#    return d

#@app.route('/add', methods=['POST'])
#def add():
#    num = request.json.get('num')
#    if num > 10:
#        return 'too much', 400
#    return jsonify({'result': num + 1})

@app.route('/predict', methods=['POST'])
def predict_func():
    features = request.json
    features = np.array(features).reshape(1, 4)
    # Десериализуем pipeline из файла
    prediction = loaded_model.predict(features)
    prediction = prediction[0]
    return jsonify({'prediction': prediction})    

if __name__ == '__main__':

    app.run('localhost', 5000)