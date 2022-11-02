from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend,BaseBackend

class CaseInsensitiveModelBackend(ModelBackend):
    def authenticate(self,request,username=None,password=None,**kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            case_insensitive_username_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
            user = UserModel._default_manager.get(**{case_insensitive_username_field:username})
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

class UserBackend(BaseBackend):
    model = get_user_model()
    def authenticate(
        self, request, username=None, password=None):
        try:
            user = self.model.objects.get(username=username)
        except self.model.DoesNotExist:
            return None
        if user.check_password(password) and user is not None:
            return user

    def get_user(self, user_id):
        try:
            return self.model.objects.get(pk=user_id)
        except self.model.DoesNotExist:
            return None