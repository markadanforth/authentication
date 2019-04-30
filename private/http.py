from bottle import response

class Http:

    def Redirect(self,code,location):
        response.status = code
        response.set_header('Location', f'{location}')