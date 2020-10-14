class UserUseCase:
    def __init__(self, user_repository_class):
        self.user_repository = user_repository_class()

    def get_user(self, id: int):
        return self.user_repository.get_user(id)
