from flask import Flask, request,jsonify
from flask_pymongo import PyMongo

#init app
app=Flask(__name__)

app.secret_key='harshcharasiya6768@gmail.com'

app.config['MONGO_URI']='mongodb://localhost:27010/Users'

mongo=PyMongo(app)   

@app.route('/register',methods=['POST'])
def register():

    _json=request.json   #get the data from request
    
    _name=_json['name']
    _email=_json['email']
    _age=_json['age']
    
    print(request.json)
    
    if _name and _email and request.method=='POST':
        print('inside if statement')
        return jsonify({
            'name':_name,
            "email":_email,
            "age":_age
        })


@app.route('/login',methods=['POST'])
def login():
    print('login user')

@app.route('/getUsers',methods=['GET'])
def get_users():
    print('users detail')


#start server
if __name__=='__main__':
    app.run(debug=True)
