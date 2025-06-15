import os
import django
from django_mailbox.models import EmailConfig

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

try:
    email_config = EmailConfig.objects.latest('updated_at')
    sender_username = email_config.sender_username
    sender_pwd = email_config.sender_pwd
    receive_list = email_config.receive_list
    print(receive_list)
except EmailConfig.DoesNotExist:
    # 处理未找到配置的情况
    pass
