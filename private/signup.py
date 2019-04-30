from private.database import Database
from private.http import Http
from private.formfields import FormFields

class Signup:

    def __init__(self):
        self.Database = Database()
        self.Http = Http()
        self.FormFields = FormFields()
        

    def main(self, request):
        if self.Database.GetUser(request.forms["email"]) is not None:
            print("email exists in database")
            self.Http.Redirect(303,'/signup')
            return

        if self.FormFields.PasswordsDontMatch(
                request.forms["password"],request.forms["password2"]):
            print("passwords don't match")
            self.Http.Redirect(303,'/signup')
            return

        request.forms["password"] = \
            self.FormFields.HashPassword(request.forms["password"])

        self.Database.CreateUser(request.forms)
        self.Http.Redirect(303,'/signin')