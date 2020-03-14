# -*- coding: utf-8 -*-
import logging
import os
from logging.config import dictConfig

from django.conf import settings

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(process)d:%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}  # 日志格式
        },
    'filters': {
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(settings.BASE_DIR, 'logs', 'blog.log'),                # 日志输出文件
            'maxBytes': 1024*1024*1024*5,                  # 文件大小
            'backupCount': 5,                         # 备份份数
            'formatter': 'standard',                   # 使用哪种formatters日志格式
        },

        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },

    },

    'loggers': {
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': False
        },
        'izone': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

dictConfig(LOGGING)
logger = logging.getLogger('izone')
