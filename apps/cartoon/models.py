from django.db import models

# Create your models here.


# 收藏漫画表
class LoveCartoon(models.Model):
    # 用户名
    username = models.CharField(max_length=100)
    # 漫画名
    cartoonName = models.CharField(max_length=100)
    # 漫画封面图
    cartoonImg = models.CharField(max_length=100)
    # 漫画简介
    description = models.CharField(max_length=200)
    # 漫画id
    cartoonId = models.IntegerField()
    # 是否收藏
    isLove = models.BooleanField(default=False)

    # 改表名
    class Meta:
        db_table = 'lovecartoon'


# 漫画浏览历史表
class HistoryCartoon(models.Model):
    # 用户名
    username = models.CharField(max_length=100)
    # 漫画名
    cartoonName = models.CharField(max_length=100)
    # 漫画封面图
    cartoonImg = models.CharField(max_length=100)
    # 漫画简介
    description = models.CharField(max_length=200)
    # 漫画id
    cartoonId = models.IntegerField()
    # 浏览时间
    readTime = models.CharField(max_length=100)

    # 改表名
    class Meta:
        db_table = 'historycartoon'


# 全部漫画表
class CartoonMess(models.Model):
    # 漫画id
    cartoonId = models.IntegerField()
    # 漫画名
    cartoonName = models.CharField(max_length=100)
    # 漫画封面图
    cartoonImg = models.CharField(max_length=200)
    # 漫画简介
    description = models.TextField()
    # 漫画状态
    cartoonState = models.CharField(max_length=30)
    # 漫画标签
    cartoonTag = models.CharField(max_length=100)
    # 漫画作者
    cartoonAuthor = models.CharField(max_length=100)
    # 更新时间
    updateTime = models.CharField(max_length=100)

    # 改表名
    class Meta:
        db_table = 'cartoonmess'
