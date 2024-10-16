from flask import Flask,make_response,request
from flask_migrate import Migrate
from models import * 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recap.db'

migrate = Migrate(app,db)
db.init_app(app)

@app.route('/')
def index():
    return 'Welcome to flask'

@app.route('/users')
def users():
    if request.method == 'GET':
        response = [user.to_dict() for user in User.query.all()]
        return make_response(response,200)
    if request.method == 'POST':
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        response = new_user.to_dict()
        return ({"message":"User has been added successfully"},200)
    
    
    
    @app.route ('/post')   
    def post():
        return 'post' = [user.to_dict() for user in User.query.all()]
    return make_response(response,200)
            
            
@app.route('/posts')
def posts():
    response = [post.to_dict() for post in Post.query.all()]
    return make_response(response, 200)            

if __name__ == '__main__':
    app.run(port=5545,debug=True)