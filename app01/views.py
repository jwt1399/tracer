from django.shortcuts import render
from django.shortcuts import render, HttpResponse
# Create your views here.

from django import forms
from app01 import models  # ？？？我感觉ModelForm可以卸载forms.py中
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class RegisterModelForm(forms.ModelForm):
    # 用Form重写model手机字段
    mobile_phone = forms.CharField(label='手机号', validators=[RegexValidator(r'^(1[3|4|5|6|7|8|9])\d{9}$', '手机号格式错误'), ])
    # 重写model密码字段
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    # 增加重复密码字段
    confirm_password = forms.CharField(label='重复密码', widget=forms.PasswordInput())
    # 增加验证码字段
    code = forms.CharField(label='验证码', widget=forms.TextInput())

    class Meta:
        model = models.UserInfo
        fields = "__all__"

    #重写__init__(初始化)方法,为所有字段加上class和placeholder
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():  # 拿到每一个name(eg:password)和field(eg:forms.CharField)
            field.widget.attrs['class'] = 'form-control'  # 为每一个field字段加上class
            field.widget.attrs['placeholder'] = '请输入%s' % (field.label)  # 为每一个field字段加上placeholder


def register(request):
    form = RegisterModelForm()
    return render(request, 'app01/register.html', {'form': form})
