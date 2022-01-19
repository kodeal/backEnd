from django.contrib import admin
from .models import UserModel


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'password1', 'email')  # User 클래스의 변수 이름과 통일해야 함


admin.site.register(UserModel, UserAdmin)  # site에 등록