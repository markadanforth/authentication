from bottle import response,request

class Cookie:
    cookieKey = ";1h68=2pG.|a+4!-||~2T54TR8|%!~E84gM7~=8+O=_.81p-i--:_J:^.p3*841Y"

    def CreateCookie(self, user):
        response.set_cookie("Auth",user,secret=self.cookieKey)

    def GetCookie(self, name):
        return request.get_cookie(name, secret=self.cookieKey)