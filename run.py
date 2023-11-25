from app import application
from views import user_bp

application.register_blueprint(user_bp)

application.run(debug=True)
