from flask import Flask

def create_app():
    
    app = Flask(__name__)
    
    # Set up the project
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = "dev"
    )

    # Register Blueprint
    from . import todo
    app.register_blueprint(todo.bp)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    @app.route("/")
    def index():
        return "Hello world !"
    return app