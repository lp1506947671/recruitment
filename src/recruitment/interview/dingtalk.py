from dingtalkchatbot.chatbot import DingtalkChatbot
from django.conf import settings


def send(message, at_mobiles=None):
    # 引用 settings里面配置的钉钉群消息通知的WebHook地址:
    if at_mobiles is None:
        at_mobiles = [
            settings.DINGTALK_TEST_PHONE,
        ]
    webhook = settings.DINGTALK_WEB_HOOK

    xiaoding = DingtalkChatbot(webhook, secret=settings.DINGTALK_WEB_HOOK_SECRET)

    # Text消息@所有人
    xiaoding.send_text(msg=("hello test: %s" % message), at_mobiles=at_mobiles)
