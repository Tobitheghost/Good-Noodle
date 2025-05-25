from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .main.views import home
    app.register_blueprint(home)
    
    return app

if __name__ == '__main__':
    create_app()