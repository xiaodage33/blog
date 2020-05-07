#coding=utf-8
## -*- coding: utf-8 -*-

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class CateGory(models.Model):
    cname = models.CharField(max_length=30,unique=True,verbose_name=u'类别名称')


    class Meta:
        db_table = 't_category'
        verbose_name_plural=u'类别'

    def __str__(self):
        return u'Category:%s'%self.cname

class Tag(models.Model):
    tname = models.CharField(max_length=30,unique=True,verbose_name='标签名称')

    class Meta:
        db_table = 't_tag'
        verbose_name_plural = u'标签'

    def __str__(self):
        return u'标签名称:%s' % self.tname



class Post(models.Model):
    title = models.CharField(max_length=100,unique=True,verbose_name="帖子名称")
    desc = models.CharField(max_length=100,verbose_name="帖子简介")
    content = RichTextUploadingField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    category = models.ForeignKey(CateGory,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    class Meta:
        db_table = 't_post'
        verbose_name_plural = u'帖子'

    def __str__(self):
        return u'Post:%s' % self.title

