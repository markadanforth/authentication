from bottle import route,run,static_file,template,post,request,response
from private.signup import Signup
from private.signin import Signin
from private.signout import Signout
from private.profile import Profile

@route('/signout')
def signout():
    Signout().main()

@route('/profile')
def profile():
    if Profile().IsAuthorized():
        return template('profile', user=Profile().Cookie.GetCookie("Auth"))

@post('/signin')
def do_signin():
    Signin().main(request)

@route('/signin')
def signin():
    return template('signin')

@route('/signup')
def signup():
    return template('signup')

@post('/signup')
def do_signup():
    Signup().main(request)

@route('/')
def index():
    return template('index')

@route('/css/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='public/css/')

# leaving debug and reloader to True for dev purposes
# Set those to False if used in production
run(host='localhost', port=8080, debug=True, reloader=True)