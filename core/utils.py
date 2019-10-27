import json
import uuid
import hashlib
from django.http.response import JsonResponse


class Validator:
    """请求参数校验
    """

    SPECIAL_TYPE = ['json', 'list']

    def __init__(self, params):
        self.params = params
        self.detail = ""
        self.arg_null = []
        self.arg_type = []

    def arg_check(self, arg_key, default="",
              arg_type=str, nullable=True):
        """请求参数校验

        Args:
            arg_key: 参数名
            default: 参数默认值
            arg_type: 参数类型
            nullable: 是否可以为空

        Returns:

        """
        value = self.params.get(arg_key, default)

        if (not nullable) and (not value):
            self.arg_null.append(arg_key)
        elif value and (arg_type not in self.SPECIAL_TYPE):
            try:
                value = arg_type(value)
            except ValueError:
                self.arg_type.append(arg_key)
        elif arg_type in self.SPECIAL_TYPE:
            value = json.loads(value)

        return value

    def arg_msg(self):
        if self.arg_null:
            self.detail = ("参数错误，" + self.arg_null[0] + "为空"
                           if len(self.arg_null) == 1
                           else "参数" + ",".join(self.arg_null) + "为空")
        if self.arg_type:
            self.detail = ("参数错误，" + self.arg_type[0] + "类型错误"
                           if len(self.arg_type) == 1
                           else "参数" + ",".join(self.arg_type) + "类型错误")

        if not self.detail:
            return True, ""
        return False, self.detail


class ResponseMixin:
    """响应扩展
    """

    code_message = {
        "00000": "成功",
        "00001": "参数错误,",
        "00002": "对象不存在",
        "00003": "对象已存在",
        "00004": "创建错误，",
        "00005": "登录失败",
        "00006": "请重新登录",
        "00007": "es错误"
    }

    def __init__(self):
        self._code = "00000"
        self._status = True
        self._message = "成功"

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, msg):
        self._message = msg
        # self._message = (self.code_message
        #                  .get(self.code) + msg)

    def get_json_response(self, data=None, **kwargs):
        res = dict()
        res["code"] = self.code
        res["status"] = self.status
        res["message"] = self.message
        res = {**res, **kwargs}
        res["data"] = data
        return JsonResponse(res)


class Encryption:
    """密码加密
    """

    @staticmethod
    def encrypt(password):
        md5 = hashlib.md5()
        md5.update(password.encode("utf-8"))
        return md5.hexdigest()


class GenId:

    @staticmethod
    def gen():
        return uuid.uuid1()
