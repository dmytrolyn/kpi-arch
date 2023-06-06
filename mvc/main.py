from model import User
from view import View
from controller import Controller

if __name__ == "__main__":
    user = User("Dmytro")
    view = View()
    controller = Controller(user, view)

    controller.handle_user_input()