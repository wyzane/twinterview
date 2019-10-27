from django.views import View

from core.utils import Validator
from core.utils import Encryption
from core.utils import ResponseMixin

from .models import User, Login


class Register(ResponseMixin, View):
    """用户注册
    """

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        username = validator.arg_check(
            arg_key="username",
            arg_type=str)
        password = validator.arg_check(
            arg_key="password",
            arg_type=str)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:
            user_info = {
                "username": username,
                "password": Encryption.encrypt(password)
            }
            User.objects.create(**user_info)
            return self.get_json_response()
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_json_response()


class UserLogin(ResponseMixin, View):
    """用户登录
    """

    def post(self, request):
        args = request.POST.copy()
        validator = Validator(params=args)

        username = validator.arg_check(
            arg_key="username",
            arg_type=str)
        password = validator.arg_check(
            arg_key="password",
            arg_type=str)

        is_arg_valid, err_msg = validator.arg_msg()
        if is_arg_valid:

            encrypt_password = Encryption.encrypt(password)

            user = (User.objects.filter(is_deleted=False,
                                        username=username,
                                        password=encrypt_password)
                                .first())
            if user:
                login_info = {
                    "user_id": user.user_id
                }

                Login.objects.create(**login_info)

                self.message = "登陆成功"
                return self.get_json_response()
            else:
                self.code = "00005"
                self.message = "登录失败"
                return self.get_json_response()
        else:
            self.code = "00001"
            self.status = False
            self.message = err_msg
        return self.get_json_response()
