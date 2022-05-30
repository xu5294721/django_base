from django.db import models

# Create your models here.
# 定义模型类
"""
1.类名 对应 表名
2.属性 对应 字段
3.选项 对应 选项 
"""


# 定义书籍类
class BookInfo(models.Model):
    # 定义需求类属性
    name = models.CharField(max_length=10)
    # 发布日期
    pub_date = models.DateField(null=True)
    # 阅读数
    readcount = models.IntegerField(default=0)
    # 评论数
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    # 重定义表名
    class Meta:
        db_table = 'bookinfo'

    def __str__(self):
        return self.name


# 定义人物信息类
class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )

    name = models.CharField(max_length=20)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0)
    description = models.CharField(max_length=200, null=True)
    is_delete = models.BooleanField(default=False)
    # 设置外键，与书籍表进行对应
    # on_delete=models.CASCADE 主键删除、对应也删除
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    # 重定义表名
    class Meta:
        db_table = 'peopleinfo'

    def __str__(self):
        return self.name
