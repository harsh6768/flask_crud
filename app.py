from flask import Flask, request,jsonify
from  flask_mysqldb import MySQL
import yaml

#init app
app=Flask(__name__)


#Configure db
db=yaml.load(open('db.yaml'))
app.config['MYSQL_HOST']=db['mysql_host']
app.config['MYSQL_USER']=db['mysql_user']
app.config['MYSQL_PASSWORD']=db['mysql_password']
app.config['MYSQL_DB']=db['mysql_database']

#initializing mysql
mysql=MySQL(app)



@app.route('/register',methods=['POST'])
def register():

    _json=request.json   #get the data from  json request
    # _json=request.form   #get the data from form 
    
    _name=_json['name']
    _email=_json['email']
    _password=_json['password']
    
    print(request.json)
    
    if _name and _email and _password and request.method=='POST':
        cursor=mysql.connection.cursor()
        cursor.execute('insert into users(name,email,password) values(%s,%s,%s)',(_name,_email,_password))
        mysql.connection.commit()

        cursor.close()
        return 'success'


@app.route('/login',methods=['POST'])
def login():
    print('login user')
    _json=request.json
    
    _email=_json['email']
    _password=_json['password']
    
    if _email and _password and request.method=='POST':
        cursor=mysql.connection.cursor()
        resultValue=cursor.execute('select * from users')
        
        if resultValue>0:
            #to fetch all the values
            userDetails=cursor.fetchall()
            for user in userDetails:
                print(user)
                if _email==user[2] and _password==user[3]:
                    return 'login successfull'
    return 'login failed'   

@app.route('/getUsers',methods=['GET'])
def get_users():
    print('users detail')
    if request.method=='GET':
        cursor=mysql.connection.cursor()
        resultValue=cursor.execute('select * from users')
        
        if resultValue>0:
            #to fetch all the values
            userDetails=cursor.fetchall()
            print(userDetails)
            return jsonify(userDetails)


#start server
if __name__=='__main__':
    app.run(debug=True)
