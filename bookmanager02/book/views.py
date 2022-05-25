from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('index')


# 方式一： objects--相当一个代理  实现增删改查
from book.models import BookInfo

# objects 实现增
BookInfo.objects.create(
    name='测试开发简介',
    pub_date='2010-01-01',
    readcount=20,
)

# objects filter 过滤 （更新）
BookInfo.objects.filter(id=5).update(name='Django入门', commentcount=666)

# objects 删除
BookInfo.objects.filter(id=6).delete()

BookInfo.objects.create(
    name='Flask',
    pub_date='2000-01-01',
    readcount=20,
)

# --- 过滤查询----
# 实现SQL语句中的where功能，包括
# objects.filter(属性名__运算符=值) 过滤出多个结果   n=0，1，2...   返回的是一个列表[]
# objects.exclude(属性名__运算符=值) 排除符合条件而剩下的的结果   n=0，1，2...
# objects.get(属性名__运算符=值) 过滤单个结果   n=0，1，2...        返回的是单独一个


# 查询编号为1的图书
BookInfo.objects.filter(id=1)

# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')

# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')

# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)

# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1, 2, 3])

# 查询编号大于3的图书
# 大于gt  小于lt   大于等于gte  小于等于lte

BookInfo.objects.filter(id__gt=3)

# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year='1980')

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')

# F 对象 用于2个属性名的比较操作
# 模型类名.objects.filter(第一个属性名__运算符=F('第二个属性名'))
from django.db.models import F

BookInfo.objects.filter(readcount__gt=F('commentcount'))

# Q 对象 用于或者 |，非 ~   操作
# 模型类名.objects.filter(Q(属性名__运算符=值)|Q(属性名__运算符==值))
from django.db.models import Q

# 并且     id大于1，且阅读数大于10
BookInfo.objects.filter(id__gt=1, readcount__gt=10)

# 或者，非~
# 或者|   id大于3或者阅读数小于50
BookInfo.objects.filter(Q(id__gt=3) | Q(readcount__lt=50))

# 非
BookInfo.objects.filter(~Q(id__gt=4))
