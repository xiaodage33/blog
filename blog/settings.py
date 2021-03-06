#coding=utf-8
"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.conf import global_settings
from django.utils.six import python_2_unicode_compatible


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$=^026@61q-ee()w9y=)@9czuk$+52ii8c*cpqts(5&_q&vt9p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',  # 富文本
    'ckeditor_uploader',  # 富文本
    'haystack',  # 全文搜索
    'post',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'post.mycontextprocessor.getRightInfo',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'blog2020', #数据库需要提前创建
        'USER': 'xiaoming', #连接mysql 用户名
        'PASSWORD': '123456',
        'HOST': '192.168.1.11', #指定ip
        'PORT': 3306,
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
from django.utils.translation import gettext_lazy as _
LANGUAGES = [
    ('zh-Hans', _('Chinese')),
]
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static','css')
]

#后台上传文件
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CKEDITOR_UPLOAD_PATH = 'upload/'

# # 指定生成的索引路径
# HAYSTACK_CONNECTIONS = {
#         'default': {
#             'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
#             'PATH': os.path.join(BASE_DIR, 'whoosh_index'), #whoosh_index是自动生成的目录
#         },
#     }

#指定中文分词，上面是针对英文分词
# 指定生成的索引路径
# from post.whoosh_cn_backend import WhooshEngine  #不用这行
HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'post.whoosh_cn_backend.WhooshEngine',
            'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
            # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
            # 'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
            # 'ENGINE': 'post.whoosh_cn_backend.whoosh_backend.WhooshEngine',
            # 'PATH': os.path.join(BASE_DIR, 'whoosh_index'),  #whoosh_index是自动生成的目录
        },
    }

# 实时生成索引文件
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'