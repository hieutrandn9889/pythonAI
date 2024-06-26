from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
import tensorflow as tf

#load keras model >> fixed TF is nit an element of this graph
sess = tf.Session()
graph = tf.get_default_graph()

with sess.as_default():
    with graph.as_default():
        face_model = load_model("facenet.h5")


# khoi tao flask server backend
app = Flask(__name__)

# apply flask CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/nhandienkhuonmat', methods=['POST', 'GET'])
@cross_origin(origins='*')
def uppercase_process():
    face = request.args.get('nhandienkhuonmat')
    with sess.as_default():
        with graph.as_default():
            tenNguoi = face_model.predict(face)
    return tenNguoi


#start Backend
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9999')
