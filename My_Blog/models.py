import os
from datetime import datetime

from django.db import models
from django.utils import timezone

# for slug, get_absolute_url
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

# delete md_file before delete/change model
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.files.base import ContentFile
import markdown2
from unidecode import unidecode
import time
from taggit.managers import TaggableManager


# Create your models here.
class BlogPost(models.Model):

    class Meta:
        ordering = ['-pub_date']

    CATEGORY_CHOICES = (
        ('programming', 'Programming'),
        ('acg', 'Anime & Manga & Novel & Game'),
        ('nc', 'No Category'),
    )

    title = models.CharField('标题',max_length=50)
    category = models.CharField('分类',max_length=30, choices=CATEGORY_CHOICES)
    body = models.TextField('正文')
    pub_date = models.DateField('发表日期')
    slug = models.SlugField(max_length=200, blank=True) 
    description = models.TextField('描述',blank=True)
    tags = TaggableManager()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        self.slug = slugify(unidecode(self.title))
        return  reverse('blogpost',kwargs={'id':self.id,'slug':self.slug})




#    def save(self):
#        self.slug = slugify(unidecode(self.title))

