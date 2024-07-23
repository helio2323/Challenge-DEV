from flask import Flask
from src.routes.auth_routes import routes
from src.routes.userCha_routes import ChaRoutes

app = Flask(__name__)

app.register_blueprint(routes, url_prefix="/api/v1")
app.register_blueprint(ChaRoutes, url_prefix="/api/v1")

if __name__ == "__main__":
    app.run(debug=True)