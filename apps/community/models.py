from django.db import models

# Create your models here.


class tb_comment(models.Model):

    pl_content = models.CharField(max_length=200, verbose_name='评论内容')
    pl_time = models.CharField(max_length=20, verbose_name='评论时间')
    pl_likes = models.IntegerField(default=0)

