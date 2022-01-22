from django.db import models


# Create your models here.
class UserModel(models.Model):
    user_name = models.CharField(max_length=50, verbose_name='사용자 이름')
    user_id = models.CharField(max_length=50, primary_key=True, verbose_name='사용자 아이디')
    password1 = models.CharField(max_length=200, verbose_name='사용자 비밀번호')
    email = models.EmailField(max_length=100, unique=True, verbose_name='이메일')

    def __str__(self):
        return self.user_name

    class Meta:  # 메타 클래스를 이용하여 테이블명 지정
        db_table = 'User'
