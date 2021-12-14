from tkinter import messagebox
from entities.store import Store

from repositories.store_repository import store_repository

class UserInputError(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass


class StoreService:
    """Class that provides functionality for safely communication with the database repository"""

    def __init__(self, store_repository):
        self._store = None
        self._store_repository = store_repository


    def register(self, storenumber, password, password_confirmation, login = True):

        """Inserts a new store into the database."""

        self.validate(storenumber, password, password_confirmation)

        store = self._store_repository.create_new(
            Store(storenumber, password)
        )

        if login:
            self._store_id = store
            print(self._store_id)

        return store

    def validate(self, storenumber, password, password_confirmation):
        """Makes sure that storenumber and password are valid"""
        if not storenumber or not password:
            messagebox.showerror("showerror", "You need to insert valid storenumber and password")
            raise UserInputError("You need to insert valid storenumber and password")

        if len(password) < 8:
            messagebox.showerror("showerror", "Password needs to have at least 8 characters")
            raise UserInputError("Password too short")

        if password != password_confirmation:
            messagebox.showerror("showerror", "Passwords don't match")

            raise UserInputError("Passwords don't match")

        if storenumber == ('^[0-9]+$'):
            messagebox.showerror("showerror", "Storenumber can only contain numbers 0-9")

            raise UserInputError("Storenumber can only contain numbers 0-9")

        if password == ('[^a-z]'):
            messagebox.showerror("showerror", "Password cannot consist of letters only")

            raise UserInputError("Password should not contain only characters a-z")


    def login(self, storenumber, password):
        """Log in the user"""

        store = self._store_repository.find_by_storenumber(storenumber)

        if not store or store.password != password:
            messagebox.showerror("showerror", "Invalid storenumber or password")

            raise InvalidCredentialsError("Invalid storenumber or password")

        self._storenumber = storenumber

        return storenumber

    def get_current_store(self):
        """Gets the current user id number"""

        return self._store_id

    def get_storenumber_by_id(self, store_id):
        """Gets the current user storenumber"""

        storenumber = self._store_repository.get_store_information(store_id)

        return storenumber

    def logout(self):
        """Log out current user"""
        self._storenumber = None



store_service = StoreService(store_repository)
