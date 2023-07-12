from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Blog(models.Model):
    Blogname = models.CharField(max_length=150)
    intro = models.CharField(max_length=200, default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Blogname


# 카테고리(-게시물과 one-many 연결)와 태그(게시물에 태그 할당)
class Category(models.Model):
    name = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 


class Tag(models.Model):
    name = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name


# 게시물-썸네일,제목,작성일 / 게시물에 대한 댓글
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body =  models.TextField()
    #image = models.ImageField(upload_to = 'post_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_post')

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class Reply(models.Model):
    reply = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    Comment = models.ForeignKey(Comment, on_delete=models.CASCADE)






# 검색(게시물 검색/제목, 내용, 작성자, 태그 등 필터링)

#페이징 기능

#views 파일에서 구현 맞나요 ?