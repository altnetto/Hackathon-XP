def init_app(app):
    from routes.user_routes import bp_user
    from routes.bank_routes import bp_bank
    from routes.general_routes import bp_general

    app.register_blueprint(bp_user)
    app.register_blueprint(bp_bank)
    app.register_blueprint(bp_general)
