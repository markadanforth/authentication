from private.database import Database
from private.http import Http
from private.formfields import FormFields
from private.cookie import Cookie

class Signin:
    
    def __init__(self):
        self.Database = Database()
        self.Http = Http()
        self.FormFields = FormFields()
        self.Cookie = Cookie()

    def main(self,request):
        user = self.Database.GetUser(request.forms["email"])

        if user is None:
            print("user not found in database")
            self.Http.Redirect(303,'/signin')
            return

        if not self.FormFields.PasswordMatchHash(
                                request.forms["password"],
                                user["password"]):
            print("passwords don't match")
            self.Http.Redirect(303,'/signin')
            return

        self.Cookie.CreateCookie(user)
        self.Http.Redirect(303,'/profile')