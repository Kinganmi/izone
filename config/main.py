import os

# 配置数据库
MYSQL_HOST = os.getenv('IZONE_MYSQL_HOST', '127.0.0.1')
MYSQL_NAME = os.getenv('IZONE_MYSQL_NAME', 'my_zone')
MYSQL_USER = os.getenv('IZONE_MYSQL_USER', 'root')
MYSQL_PASSWORD = os.getenv('IZONE_MYSQL_PASSWORD', '123456')
MYSQL_PORT = os.getenv('IZONE_MYSQL_PORT', 3306)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 修改数据库为MySQL，并进行配置
        'NAME': MYSQL_NAME,  # 数据库的名称
        'USER': MYSQL_USER,  # 数据库的用户名
        'PASSWORD': MYSQL_PASSWORD,  # 数据库的密码
        'HOST': MYSQL_HOST,
        'PORT': MYSQL_PORT,
        'OPTIONS': {'charset': 'utf8'}
    }
}

# 使用django-redis缓存页面，缓存配置如下：
REDIS_HOST = os.getenv('IZONE_REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.getenv('IZONE_REDIS_PORT', 6379)

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://{}:{}".format(REDIS_HOST, REDIS_PORT),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 配置管理邮箱，服务出现故障会收到到邮件，环境变量值的格式：name|test@test.com 多组用户用英文逗号隔开
ADMINS = []
admin_email_user = os.getenv('IZONE_ADMIN_EMAIL_USER')
if admin_email_user:
    for each in admin_email_user.split(','):
        a_user, a_email = each.split('|')
        ADMINS.append((a_user, a_email))

# 邮箱配置
EMAIL_HOST = os.getenv('IZONE_EMAIL_HOST', 'smtp.163.com')
EMAIL_HOST_USER = os.getenv('IZONE_EMAIL_HOST_USER', 'your-email-address')
EMAIL_HOST_PASSWORD = os.getenv('IZONE_EMAIL_HOST_PASSWORD', 'your-email-password')  # 这个不是邮箱密码，而是授权码
EMAIL_PORT = os.getenv('IZONE_EMAIL_PORT', 465)  # 由于阿里云的25端口打不开，所以必须使用SSL然后改用465端口
EMAIL_TIMEOUT = 5
# 是否使用了SSL 或者TLS，为了用465端口，要使用这个
EMAIL_USE_SSL = os.getenv('IZONE_EMAIL_USE_SSL', 'True').upper() == 'TRUE'
# 默认发件人，不设置的话django默认使用的webmaster@localhost，所以要设置成自己可用的邮箱
DEFAULT_FROM_EMAIL = os.getenv('IZONE_DEFAULT_FROM_EMAIL', 'L6BJ <your-email-address>')

# 网站默认设置和上下文信息
SITE_END_TITLE = os.getenv('IZONE_SITE_END_TITLE', '')
SITE_DESCRIPTION = os.getenv('IZONE_SITE_DESCRIPTION', '是一个使用 Django+Bootstrap4 搭建的个人博客类型网站')
SITE_KEYWORDS = os.getenv('IZONE_SITE_KEYWORDS', 'Django博客,个人博客')
SITE_LOGO_NAME = os.getenv('IZONE_LOGO_NAME', 'TendCode')

# 个性化设置，非必要信息
# 个人 Github 地址
MY_GITHUB = os.getenv('IZONE_GITHUB', 'https://github.com/Hopetree')
# 工信部备案信息
BEIAN = os.getenv('IZONE_BEIAN', '苏ICP备19010454号')
# 站长统计（友盟）
CNZZ_PROTOCOL = os.getenv('IZONE_CNZZ_PROTOCOL', '')
# 站长推送
MY_SITE_VERIFICATION = os.getenv('IZONE_SITE_VERIFICATION', '')
# 使用 http 还是 https （sitemap 中的链接可以体现出来）
PROTOCOL_HTTPS = os.getenv('IZONE_PROTOCOL_HTTPS', 'HTTPS').lower()
# hao.tendcode.com
HAO_CONSOLE = {
    'flag': os.getenv('IZONE_HAO_FLAG', 'False').upper() == 'TRUE',
    'name': os.getenv('IZONE_HAO_NAME', '微草导航'),
    'url': os.getenv('IZONE_HAO_URL', 'https://hao.tendcode.com')
}