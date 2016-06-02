from .models import Users

class CustomBackend :
    def __init__(self):
        pass
    def authenticate(self, username=None, password=None):
        try:
            # Try to find a user matching your username
            user = Users.objects.get(User_Name=username)
            if password == user.Password :
                return user
            else :
                return None
            #  Check the password is the reverse of the username
            #if password == username[::-1]:
                # Yes? return the Django user object
                #return user
            #else:
                # No? return None - triggers default login failed
                #return None
        except Users.DoesNotExist:
            # No user was found, return None - triggers default login failed
            print "no user found with password"
            return None
    def get_user(self, user_id):
        try:
            return Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return None
