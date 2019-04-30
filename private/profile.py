from private.http import Http
from private.cookie import Cookie

class Profile:
    Cookie = Cookie()

    def IsAuthorized(self):
        if not self.Cookie.GetCookie("Auth"):
            print("not logged in")
            Http().Redirect(303, '/signin')
            return False
        else:
            return True