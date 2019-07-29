from django.contrib import admin
from .models import Post
# Register your models here.

# 관리자 페이시에서 만들 모델 등록
admin.site.register(Post)