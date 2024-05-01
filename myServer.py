from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request

# khoi tao flask server backend
app = Flask(__name__)

# apply flask CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# http://127.0.0.1:9999/add?sothunhat=10&sothuhai=3
@app.route('/add', methods=['POST', 'GET'])
@cross_origin(origins='*')
def add_process():
    a = int(request.args.get('sothunhat'))
    b = int(request.args.get('sothuhai'))
    result = a + b 
    return "ketqua ham cong: " + str(result)

# http://127.0.0.1:9999/minus?sothunhat=10&sothuhai=3
@app.route('/minus', methods=['POST', 'GET'])
@cross_origin(origins='*')
def minus_process():
    a = int(request.args.get('sothunhat'))
    b = int(request.args.get('sothuhai'))
    result = a - b 
    return "ket qua ham tru: " + str(result)

@app.route('/multi', methods=['POST','GET'] )
@cross_origin(origin='*')
def multi_process():
    a = int(request.args.get('sothunhat'))
    b = int(request.args.get('sothuhai'))
    result = a * b
    return "Hàm nhân: " + + str(result)

@app.route('/uppercase', methods=['POST', 'GET'])
@cross_origin(origins='*')
def uppercase_process():
    s = request.args.get('chuoiInput')
    return s.upper()


#start Backend
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9999')
