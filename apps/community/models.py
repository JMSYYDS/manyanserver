from django.db import models

# Create your models here.


class tb_comment(models.Model):

    pl_content = models.CharField(max_length=200, verbose_name='评论内容')
    pl_time = models.CharField(max_length=20, verbose_name='评论时间')
    pl_likes = models.IntegerField(default=0)


# 文章数据表
class AllEssay(models.Model):
    # 文章id
    essayId = models.AutoField(primary_key=True)
    # 文章作者用户名
    essayAuthor = models.CharField(max_length=200)
    # 文章标题
    essayTitle = models.CharField(max_length=200)
    # 文章内容
    essayContent = models.TextField()
    # 文章发布时间
    essayTime = models.CharField(max_length=100)
    # 文章点赞数
    essaySupport = models.IntegerField(default=0)
    # 文章点击量
    essayClicks = models.IntegerField(default=0)

    # 改表名
    class Meta:
        db_table = 'allessay'


# 评论表
class Comment(models.Model):

    # 评论id
    commentId = models.AutoField(primary_key=True)
    # 文章id
    essayId = models.IntegerField()
    # 评论内容
    commentContent = models.TextField()
    # 评论时间
    commentTime = models.CharField(max_length=100)
    # 评论人
    commentAuthor = models.CharField(max_length=200)
    # 点赞数
    commentClicks = models.IntegerField(default=0)

    # 改表名
    class Meta:
        db_table = 'comment'


# 文章点赞表
class Support(models.Model):

    # 文章id
    essayId = models.IntegerField()
    # 点赞人
    supportAuthor = models.CharField(max_length=200)
    # 是否点赞
    isSupport = models.BooleanField(default=False)

    # 改表名
    class Meta:
        db_table = 'support'


# 评论点赞表
class supportComment(models.Model):

    # 文章id
    essayId = models.IntegerField()
    # 评论id
    commentId = models.IntegerField()
    # 点赞人
    supportAuthor = models.CharField(max_length=200)
    # 是否点赞
    isSupport = models.BooleanField(default=False)

    # 改表名
    class Meta:
        db_table = 'supportcomment'