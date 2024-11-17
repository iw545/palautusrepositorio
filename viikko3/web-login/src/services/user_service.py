from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        check_existing_user = self._user_repository.find_by_username(username)
        if check_existing_user:
            raise AuthenticationError("Username not available, choose another one")
        
        if not str(username).isalpha():
            raise UserInputError("Username can only consist of a-z")
        
        if len(str(username)) < 3:
            raise UserInputError("Username must be at least 3 characters")
        
        if password != password_confirmation:
            raise UserInputError("Password doesn't match")
        
        if len(str(password)) < 8:
            raise UserInputError("Password must be at least 8 characters")
        
        if str(password).isalpha():
            raise UserInputError("Password can't consist of characters only")



user_service = UserService()
