from flask import Flask
from app.database import db, ma
from app.models import Material, Category, Item, ItemMaterial  # Importar todos los modelos
from app.routes import item_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')


    # Inicializar extensiones
    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(item_routes.bp, url_prefix='/items')
    with app.app_context():
        try:
            print("Creando tablas...")
            db.create_all()
            print("Tablas creadas correctamente.")
        except Exception as e:
            print(f"Error al crear tablas: {e}")

    return app
