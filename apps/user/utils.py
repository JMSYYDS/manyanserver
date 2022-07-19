# 自定义用户认证的后端:实现多账号登录
from django.contrib.auth.backends import ModelBackend
import re
from user.models import User


def get_user_by_account(account):
    # """
    # 通过账号获取用户
    # :param account: 用户名或者手机号
    # :return: user
    # """
    try:
        if re.match(r'^1[3-9]\d{9}$', account):
            user = User.objects.get(mobile=account)
        else:
            user = User.objects.get(username=account)
    except User.DoesNotExist:
        return None
    else:
        return user


class UsernameMobileBackend(ModelBackend):
    # """自定义用户认证后端"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        # """重写用户认证的方法"""
        # username: 用户名或者手机号
        # 使用账号查询用户
        user = get_user_by_account(username)
        # 校验密码是否正确
        if user and user.check_password(password):
            return user
        else:
            return None
        # 返回user
