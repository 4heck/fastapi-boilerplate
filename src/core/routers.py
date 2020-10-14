from apps.users import routers as user_routers

ROUTERS = (user_routers,)


def init_routers(app):
    for router in ROUTERS:
        app.include_router(router.router)
