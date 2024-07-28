from flask import Flask
from src.routes.auth_routes import routes
from src.routes.userCha_routes import ChaRoutes
from src.routes.question_routes import question_routes
from src.routes.qVerify_route import qVerify

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(routes, url_prefix="/api/v1")
app.register_blueprint(ChaRoutes, url_prefix="/api/v1")
app.register_blueprint(question_routes, url_prefix="/api/v1")
app.register_blueprint(qVerify, url_prefix="/api/v1")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)