from . import AnalyserRoutes, BaseRoutes

def init_app(app):
    app.register_blueprint(BaseRoutes.routes)
    app.register_blueprint(AnalyserRoutes.routes)
    return app