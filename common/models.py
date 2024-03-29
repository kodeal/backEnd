"""
common/models.py
- Custom User Model 구현
"""
import uuid as uuid
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

DELETED_USER = "deleted_user"


# BaseUserManager 클래스는 User 생성 시 사용하는 Helper Class이므로 이를 상속하여 Usermanager 클래스를 구성
class UserManager(BaseUserManager):

    # create_user()의 기본형: create_user(*username_field*, password=None, **other_fields)
    # 본 프로젝트에서는 username_field에 'user_id'(사용자 아이디)를 사용
    def create_user(self, userid, username, email, password=None):
        if not userid:
            raise ValueError('Users must have an user id')
        if not username:
            raise ValueError('Users must have an user name')
        if not email:
            raise ValueError('Users must have an email')

        user = self.model(
            userid=userid,
            username=username,
            email=self.normalize_email(email),
            # password=password    # 암호화 진행 시 삭제
        )

        user.set_password(password)    # 암호화 진행 시 주석 해제
        user.save(using=self._db)
        return user

    # create_superuser()의 기본형: create_superuser(*username_field*, password, **other_fields)
    # 위와 마찬가지로 username_field에 'user_id'(사용자 아이디)를 사용
    def create_superuser(self, userid, username, email, password):
        user = self.create_user(
            userid,
            password=password,
            username=username,
            email=self.normalize_email(email),
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# AbstractBaseUser를 상속받아 실제 모델을 구현
class User(AbstractBaseUser):
    userid = models.CharField(max_length=50, primary_key=True, null=False, blank=False,
                              unique=True, verbose_name='사용자 아이디')
    username = models.CharField(max_length=50, null=False, blank=False, verbose_name='사용자 이름')
    email = models.EmailField(verbose_name='이메일', max_length=255, unique=True, null=False, blank=False)
    # 아래 두 개의 필드는 Django의 User Model을 구성할 때 필수로 요구되는 항목
    is_active = models.BooleanField(default=True)  # 이메일 인증 시 활용되는 속성
    is_admin = models.BooleanField(default=False)

    # User Model을 생성하기 위해 필수로 요구되는 항목
    # 위에서 생성한 Helper Class를 사용하도록 설정 후 username field를 'user_id'로 등록
    objects = UserManager()
    USERNAME_FIELD = 'userid'
    REQUIRED_FIELDS = ['username', 'email']

    def __str__(self):
        return self.userid

    # True를 반환하여 권한이 있는 것을 알림
    # Object 반환 시 해당 Object로 사용 권한을 확인하는 절차가 필요함
    def has_perm(self, perm, obj=None):
        return True

    # True를 반환하여 주어진 App의 Model에 접근 가능하도록 함
    def has_module_perms(self, app_label):
        return True

    # True 반환 시 Django의 관리자 화면에 로그인 가능
    @property
    def is_staff(self):
        return self.is_admin

    # 실제 데이터베이스에서 보이는 테이블 이름 설정
    class Meta:
        db_table = 'user'


class UserAuth(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name='이메일', max_length=255, null=False, blank=False)
    auth_num = models.CharField(verbose_name='인증번호', max_length=8, null=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'user_auth'


# 사용자정보
class UserInfo(models.Model):
    userid = models.ForeignKey(User, related_name="%(class)s_userid", on_delete=models.SET_DEFAULT,
                               default=DELETED_USER, db_column='userid', verbose_name='사용자 아이디')
    nickname = models.CharField(max_length=255, verbose_name='닉네임', null=True, blank=True, default=userid)
    temperature = models.FloatField(max_length=10,
                                    verbose_name='코덱스온도',
                                    null=True, blank=True,
                                    default=0.1)    # 사용자 별 최적의 코덱스 온도 설정을 위함

    def __str__(self):
        return self.userid

    class Meta:
        db_table = 'user_info'


# 프로필 이미지
class Profile(models.Model):
    inum = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='이미지', blank=True, null=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, verbose_name='UUID')
    userid = models.ForeignKey(User, on_delete=models.SET_DEFAULT,
                               default=DELETED_USER, db_column='userid', verbose_name='사용자 아이디')

    def __str__(self):
        return self.inum

    class Meta:
        db_table = 'image'

