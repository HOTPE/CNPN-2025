from flask import Flask, jsonify
from flasgger import Swagger
from flask_swagger_ui import get_swaggerui_blueprint

from api.swagger import spec
from api.controllers.todo_controller import bp as todo_bp
from api.home import home_bp
from api.valuation import valuation_bp

from api.middleware import middleware
from api.responses import success_response
from infrastructure.databases import init_db
from config import Config, SwaggerConfig


def create_app():
    app = Flask(__name__)
    Swagger(app)

    # Đăng ký blueprint
    app.register_blueprint(todo_bp, url_prefix="/todos")
    app.register_blueprint(home_bp)  # route "/"
    app.register_blueprint(valuation_bp, url_prefix="/valuation")  # route "/valuation"

    # Swagger UI
    SWAGGER_URL = '/docs'
    API_URL = '/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={'app_name': "Todo & Diamond API"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    # Khởi tạo DB
    init_db(app)

    # Middleware
    middleware(app)

    # Tự động thêm swagger paths
    with app.test_request_context():
        for rule in app.url_map.iter_rules():
            if rule.endpoint.startswith(('todo.', 'valuation.', 'home.')):
                view_func = app.view_functions[rule.endpoint]
                print(f"Adding path: {rule.rule} -> {view_func}")
                try:
                    spec.path(view=view_func)
                except Exception as e:
                    print(f"⚠️ Không thể thêm path {rule.rule}: {e}")

    @app.route("/swagger.json")
    def swagger_json():
        return jsonify(spec.to_dict())

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=6868, debug=True)
