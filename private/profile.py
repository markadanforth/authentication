from private.http import Http
from private.cookie import Cookie

class Profile:

    def __init__(self):
        self.Cookie = Cookie()
        self.Http = Http()

    def IsAuthorized(self):
        if not self.Cookie.GetCookie("Auth"):
            print("not logged in")
            self.Http.Redirect(303, '/signin')
            return False
        else:
            return True