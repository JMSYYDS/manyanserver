from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from book.models import BookInfo, PeopleInfo

# Create your views here.


def index(request):
    # 1.到数据库查数据
    books = BookInfo.objects.all()
    # 2.组织数据
    context = {
        'books': books
    }
    render(request, '', context)
    return HttpResponse('index')


# -------------------新增数据-------------------
# 方式1.
book = BookInfo(
    name='python',
    pub_data='2000-1-1',
)
# 需要手动调用save()方法 book.save()
book.save()

# 方式2. 直接入库
# 我们对模型的增删改查都找objects
BookInfo.objects.create(
    name='java',
    pub_data='2010-1-1',
)

# ----------------------更新数据---------------------
# 方式1.
# 1.先查询数据
# 查询id=1的数据
book = BookInfo.objects.get(id=1)

# 2.直接修改实例的属性
book.readcount = 20

# 3.入库
book.save()

# 方式2. 直接更新
BookInfo.objects.filter(id=1).update(
    readcount=100,
    commentcount=200,
)

# ----------------------删除数据---------------------

# 方式1.
# 1.先查询数据
book = BookInfo.objects.get(id=5)
# 2.调用删除方法
book.delete()

# 方式2.
BookInfo.objects.filter(id=6).delete()

# ----------------------基本查询---------------------
# get得到某一个数据
# all()获取所有数据
# count() 返回个数

# 返回一个对象
try:
    book = BookInfo.objects.get(id=1)
except Exception:
    pass

# 返回所有结果 是列表
BookInfo.objects.all()

BookInfo.objects.all().count()
BookInfo.objects.count()

# ----------------------filter,get,exclude---------------------
# 相当于where查询
# filter 筛选或过滤  返回 n个结果
# get    筛选或过滤  返回 1个结果
# exclude 排除掉符合条件剩下的结果  相当于not

# 查询编号为1的图书
# 标准写法
BookInfo.objects.get(id__exact=1)
# 返回列表
BookInfo.objects.filter(id=1)
# 查询书名含‘湖’的图书
# contains 包含
BookInfo.objects.filter(name__contains='湖')
# 查询书名以'部'结尾的
BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的书
BookInfo.objects.filter(name__isnull=True)
# 查询编号为1,3,5的书
BookInfo.objects.filter(id__in=[1, 3, 5])
# 查询编号大于3的图书
# gt是大于  gte是大于等于  equal等于  lt小于  le小于等于
BookInfo.objects.filter(id__gt=3)
# 查询书籍id不为3的书
BookInfo.objects.exclude(id=3)
# 查询1980年发布的图书
BookInfo.objects.filter(pub_data__year=1980)
# 查询1990年1月1号后面的书
BookInfo.objects.filter(pub_data__gt='1990-1-1')

# ----------------------F对象---------------------
from django.db.models import F
# 语法形式  filter(=F('字段名'))
# 查询阅读量大于等于评论量的书
BookInfo.objects.filter(readcount__gte=F('commentcount'))

# 查询阅读量大于等于评论量两倍的书
BookInfo.objects.filter(readcount__gte=F('commentcount')*2)

# ----------------------Q对象---------------------
# 查询id大于2并且阅读量大于20的书
# 方式1.
BookInfo.objects.filter(id__gt=2).filter(readcount__gt=20)
# 方式2.
BookInfo.objects.filter(id__gt=2, readcount__gt=20)

# 查询id大于2或者阅读量大于20的书
from django.db.models import Q

BookInfo.objects.filter(Q(id__gt=2) | Q(readcount__gt=20))
# ~Q 相当于not
# 查询书籍id不为3的书
BookInfo.objects.exclude(id=3)
BookInfo.objects.filter(~Q(id=3))

# ----------------------聚合函数---------------------
# Sum,Max,Min,Avg,Count
# 要使用aggregate
# 查询当前书籍的阅读总量
from django.db.models import Sum, Avg, Max, Min, Count
BookInfo.objects.aggregate(Sum('readcount'))


# ----------------------排序---------------------
# 默认升序
BookInfo.objects.all().order_by('readcount')
# 降序
BookInfo.objects.all().order_by('-readcount')

# ----------------------关联查询---------------------
# 书籍人物  一对多
# 书籍中没有关于人物的字段
# 人物中有关于书籍的book外键
# 语法: 主表模型.关联模型类名小写_set.all()

# 查询书籍为1的所有人物信息
# 通过书籍查询人物
book = BookInfo.objects.get(id=1)
# django自动为我们添加一个属性
book.peopleinfo_set.all()

# 查询人物为1的书籍信息
# 返回person实例对象
person = PeopleInfo.objects.get(id=1)
person.book

# ----------------------关联查询筛选---------------------
# 书籍人物  一对多
# 书籍中没有关于人物的字段
# 人物中有关于书籍的book外键
# 语法: filter(关联模型类名小写__字段__运算符=值)

# 查询图书，要求图书人物为郭靖
BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
BookInfo.objects.filter(peopleinfo__name='郭靖')

# 查询图书，要求图书人物的描述包含‘八’
BookInfo.objects.filter(peopleinfo__description__contains='八')

# 查询书名为天龙八部的所有人物
PeopleInfo.objects.filter(book__name='天龙八部')
# 查询阅读量大于50的书籍的所有人物
PeopleInfo.objects.filter(book__readcount__gt=50)

