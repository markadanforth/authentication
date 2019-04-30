from bottle import response
from private.http import Http

class Signout:

    def __init__(self):
        self.Http = Http()
    
    def main(self):
        response.delete_cookie("Auth")
        self.Http.Redirect(303,'/signin')