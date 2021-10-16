from auth import login_user
from menu import menu


@login_user
def app(user_id:int):
    return menu(user_id)

if __name__ == "__main__":
    app()
