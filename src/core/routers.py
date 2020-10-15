from apps.users import routers as user_routers


def init_routers(app):
    app.include_router(
        user_routers.router,
        prefix="/users",
        tags=["users"],
    )
    return app
