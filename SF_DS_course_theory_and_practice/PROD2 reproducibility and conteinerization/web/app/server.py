from flask import Flask, request, jsonify
import pickle
import numpy as np
import os

# Get the directory of the current script
# #script_dir = os.path.dirname(__file__)

# Define the output directory relative to the script directory
#model_dir = os.path.join(script_dir, 'models')
    

# загружаем модель из файла
with open('models/model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

# создаём приложение
app = Flask(__name__)

@app.route('/')
def index():
    msg = "Тестовое сообщение. Сервер запущен!"
    return msg

@app.route('/predict', methods=['POST'])
def predict():
    features = request.json
    features = np.array(features).reshape(1, 4)
    # Десериализуем pipeline из файла
    prediction = model.predict(features)
    prediction = prediction[0]
    return jsonify({'prediction': prediction})  

#if __name__ == '__main__':
#    app.run('localhost', 5000)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)