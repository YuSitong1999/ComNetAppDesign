"""
Django settings for bookstore project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yfg@4mk0!17vaeujd3)m8#a3#rwj@4l#+4tah&5+9a%qu7fx(4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'user',
    'book',
    'order',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'bookstore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 模板搜索路径
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 在INSTALLED_APPS中寻找templates子目录
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookstore.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'en-us'

# 时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# 会话设置
# 缓存并写到数据库
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
# 每次会话缓存
SESSION_SAVE_EVERY_REQUEST = True
# 默认：关闭浏览器后仍有效
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# 邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.qq.com'  # 如果是 163 改成 smtp.163.com
EMAIL_PORT = 465
EMAIL_HOST_USER = 'yusitong1999@qq.com'  # 帐号
EMAIL_HOST_PASSWORD = 'xcjzwgewebtpbccj'  # 密码
DEFAULT_FROM_EMAIL = 'yusitong <' + EMAIL_HOST_USER + '>'

# 使用本地时间
USE_TZ = False

APP_ID = '2016102100732845'
APP_PRIVATE_KEY = '''-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAqSlXzwpHVcCtVV5OB5JLUWEwgnJMXNY4POd5tTACt4RUocm91YxIjlN5uLe04RlYfaWPM0XrwDaVmA5UaTrngtX4e/TDBXlFXJCs3JH7Xc5r8KhqUwmR1Fc0BoBtyTaB+rwhYHcPD07xmZ0h4K8UzAlki70jEhZmQxtf1JQCvdWOkJie7+ojuPB6DE/054wPkyD0imK9LOWQWRjeT2fzLMkAxXNixfNFoyvjos37DJ2ojSyyzDU5B5n2qrdyCzfZbMBzXgg/sqEvKKqz4p8n70Im9Ly2DQbQ8ytpPcn6QER0K4zBNab7nxaHZQe1/YVDWhmVtafnaUpftKgemFszqQIDAQABAoIBAGk1RV+HTQaQZz2JAY7D9gQPJlR7MfMraJ64eIGv8oCg1OIqzt5Z+WZLlJDF8MFvOhIrPfztp8pMKI4Bm443DHXbDkhJ2mE1I2aGtHwabvPQxmFO3ZH3ibM+6SSCC8XxGLYQ+9E7OyqSNsELcV6EhbLAxMAESiOdusxR4jAcPfhCLJMg97RXIX+YQGoDpj2E3427DPXWX+65msvQJL6vjhK5wTAwxLeQi7S08A59uV3xJ9mWuqc5mwxiXe9oE/GIBGc9M859kPZdZvnwuH9lqX3JgWUTQZExKSYafDm4gMfhkqn//HC2Eo4gdVXb2Cavar9taUrmdBTQX2Uv3e69NuECgYEA75dYjflknFDcxs+zaIXGWO6HvtNPRGV8z9PYnSZ7NIpMLxiVM2uUqgfXI56byqbBjpCN5qiTPFp4T5svkvPwj1ouZP/lu3I/rdGhs5FYFoHi1fAQFC0uOfS8JGCFw7leN5wXHFjjPKojcdV9OqU8oZU35X6qbxw1SzZHg4QJLhMCgYEAtL8unQN+AXXiKH7CVM2hJzn2JZSv8yUBsHVOBKv85M6NxwLTTRidmE7NqSIbIJkLPtmB+u4x+dMu8/mi4eUCHU8BblAocvFBNtSMx4od3H9KhSGv20bh0fyNgIeEqXxiICY6qm9qPQvXrcOwLaZRQ94nbKIDqBBbpfggX2WMHtMCgYAWclt9kav3aSwGBFeOp1nZ4x8cpbd7dPaokfRtZLmORpa0otz3oFChTXK+h5GY/t6LeMeSoKCKuv8ility3R/gjlZiaAch9KY6prU7mZZjJXAXExKukT0PePpXfiOKHsfQ9fLEWR+RA2+mrpW49NolWVGPUrqtBjuH/GHe1HP3uQKBgHUkr2ZN/B2gNFqAhRyHRRnyQ+jpa/vPEUA3VsBKY5Y7lMHVv/LosEMlV791flVrO1GZkNd8B2HeEEFJmtqDHRK3wLqpMv4EBHsv2Kn+hwoAaeDNC3e3geYho+gYbM+X8NTbUgxiN12nTjqtaIK9l0/ALJcIjgwfxfZUUU7itqTHAoGAY5GfRM49SjuyM4M65Lwz2XrulgxodZLdI+dKDUPMqpXwgBeP14ci8Mm5ldub13RKanDxtF92byAoI/Yn6xe8zynVgIFmIKI6yf7rk5NA8fGbDeRoLxnSJnMNxihNbS/n799YpXTa5dywl8lCw8kaxdZ+6hz+EZH/wAF24zAfPzo=
-----END RSA PRIVATE KEY-----
'''
ALIPAY_PUBLIC_KEY = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwy7Xzzm9XnT3Clb2wGmO5O/N1/jpiEgIVomCYiFJJCvADlMdPuVcFaRPYMDj2cE6f2w+MiJQucTazpAbOxC0PQMwcjfFjENVvk0ZfuJwWLQI0bOdbiCN79iaPstjqHgrSFKbU3njuoFkbKImKCu4YbgiQoq+vXan+M80QLhVafMmIqa0jDOBLpqF3iw1xsl0FHxfkRFodHs1obF0cj6Z2qbpzele+LGlkTI9J2l0NIXPDaA0S/w1nsLqN5yfMzExpDxcY+PlQCwSgHPzVqwkQ4dspbEKy+RxJTIbuTJpPNbiVvZwsc3WmxrWzvFH9jk2mr7LccjNbxPVOwOIoJLMCwIDAQAB
-----END PUBLIC KEY-----
'''

# 订单状态：已取消 0， 待付款 1， 待发货 2， 已发货 3， 已完成 4
STATUS_NUM_TO_STR = {
    0: '已取消',
    1: '待付款',
    2: '待发货',
    3: '已发货',
    4: '已完成',
}
STATUS_STR_TO_NUM = {
    '已取消': 0,
    '待付款': 1,
    '待发货': 2,
    '已发货': 3,
    '已完成': 4,
}