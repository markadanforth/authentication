import bcrypt

class FormFields():

    def PasswordsDontMatch(self,pass1,pass2):
        if pass1 != pass2:
            return True
        else:
            return False

    def HashPassword(self,password):
        return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    def PasswordMatchHash(self,password,hashPassword):
        return bcrypt.checkpw(
                password.encode('utf-8'), 
                hashPassword.encode('utf-8'))