from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True, verbose_name='사용자 아이디')
    user_name = models.CharField(max_length=50, verbose_name='사용자 이름')
    password1 = models.BinaryField(max_length=200, blank=True, null=True, verbose_name='사용자 비밀번호')
    password2 = models.BinaryField(max_length=200, blank=True, null=True, verbose_name='사용자 비밀번호(확인)')
    email = models.EmailField(max_length=100, unique=True, verbose_name='이메일')

    def __str__(self):
        return self.user_name

    class Meta:  # 메타 클래스를 이용하여 테이블명 지정
        db_table = 'user'
