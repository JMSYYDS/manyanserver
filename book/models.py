from django.db import models

# Create your models here.


# 自动生成主键id
# 书籍表 id,name,pub_data,readcount,commentcount,is_delete
# CharField 必须设置max_length
# default 默认值    null 是否可以为空    unique 是否唯一    verbose_name 主要是 admin后台使用,后台显示
class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True)
    # 发布日期
    pub_data = models.DateField(null=True)
    # 阅读量
    readcount = models.IntegerField(default=0)
    # 评论量
    commentcount = models.IntegerField(default=0)
    # 是否删除
    is_delete = models.BooleanField(default=False)

    # 改表名
    class Meta:
        db_table = 'bookinfo'
        # 修改后台admin显示信息的设置
        verbose_name = 'admin'

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    # 有序字典
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )

    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='书本信息')
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")

    # 改表名
    class Meta:
        db_table = 'peopleinfo'
        # 修改后台admin显示信息的设置
        verbose_name = '人物信息'

    def __str__(self):
        return self.name


"""
    insert into bookinfo(name, pub_data, readcount, commentcount, is_delete) values
    ('射雕英雄传', '1980-5-1', 12, 34, 0),
    ('天龙八部', '1986-7-24', 36, 40, 0),
    ('笑傲江湖', '1995-12-24', 20, 80, 0),
    ('雪山飞狐', '1987-11-11', 58, 24, 0);
"""
"""
    insert into peopleinfo(name, gender, book_id, description, is_delete) values
    ('郭靖', 1, 1, '降龙十八掌', 0),
    ('黄蓉', 0, 1, '打狗棍法', 0),
    ('黄药师', 1, 1, '弹指神功', 0),
    ('欧阳锋', 1, 1, '蛤蟆功', 0),
    ('梅超风', 0, 1, '九阴白骨爪', 0),
    ('乔峰', 1, 2, '降龙十八掌', 0),
    ('段誉', 1, 2, '六脉神剑', 0),
    ('虚竹', 1, 2, '天山六阳掌', 0),
    ('王语嫣', 0, 2, '神仙姐姐', 0),
    ('令狐冲', 1, 3, '独孤九剑', 0),
    ('任盈盈', 0, 3, '弹琴', 0),
    ('岳不群', 1, 3, '华山剑法', 0),
    ('东方不败', 0, 3, '葵花宝典', 0),
    ('胡斐', 1, 4, '胡家刀法', 0),
    ('苗若兰', 0, 4, '黄衣', 0),
    ('程灵素', 0, 4, '医术', 0),
    ('袁紫衣', 0, 4, '六合拳', 0);    
"""
