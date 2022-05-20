from django.db import models


# Create your models here.

class BookInfo(models.Model):
    # 主键自动生成，不需要单独填写
    name = models.CharField(max_length=20)


class PersonInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
