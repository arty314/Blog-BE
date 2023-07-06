from django.db import models

# 로그인/로그아웃 기능(비밀번호 재설정 가능 => )
# 유저아이디, 이메일, 패스워드

class User(models.Model):
    user_id = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    user_image = models.ImageField(upload_to = 'profile_images/')
    # introduction = models.TextField()

    class Meta:
        db_table = 'user'