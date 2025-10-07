import logging

from dingtalkchatbot.chatbot import DingtalkChatbot
from django.conf import settings

logger = logging.getLogger("operate_logger")


def send(message, at_mobiles=None):
    try:
        # 引用 settings里面配置的钉钉群消息通知的WebHook地址:
        if at_mobiles is None:
            at_mobiles = [
                settings.DINGTALK_TEST_PHONE,
            ]
        webhook = settings.DINGTALK_WEB_HOOK
        xiaoding = DingtalkChatbot(webhook, secret=settings.DINGTALK_WEB_HOOK_SECRET)

        # Text消息@所有人
        print(f"settings.DINGTALK_TEST_PHONE:{settings.DINGTALK_TEST_PHONE}")
        xiaoding.send_text(msg=("hello test: %s" % message), at_mobiles=at_mobiles)

    except Exception as e:
        print("send dingtalk message failed: %s" % e)
