def init_app(app):
    from routes.user_routes import bp_user

    app.register_blueprint(bp_user)
