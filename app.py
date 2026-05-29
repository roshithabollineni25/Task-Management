from flask import Flask
from config.database import init_db
from Routes.auth_routes import auth_bp
from Routes.task_routes import task_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
init_db(app)

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(task_bp, url_prefix='/api/task')

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)