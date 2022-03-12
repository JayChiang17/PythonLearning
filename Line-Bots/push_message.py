# -*- coding: utf-8 -*-

from linebot import LineBotApi
from linebot.models import TextSendMessage
import time

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('pmBPLloMdShVgpWU1JwQBAALxOI6x+OosuBmBWRFJ09VdZ9SLSAWwyaxmlb6LDyTveUbwy5Zyp6CGZO2nSXmqZdnLWR6xYz5uqbNQwSAgOuszoV4w+XF3znBCrtWv+zIGGko9WgNEhZ+YB0vGZZUbgdB04t89/1O/w1cDnyilFU=')
# 請填入您的ID
yourID = 'Uc549f6792592e32b1b683b349723f2b9'
# 主動推播訊息
line_bot_api.push_message(yourID, 
                          TextSendMessage(text='安安您好！早餐吃了嗎？'))
# 用迴圈推播訊息
for i in [1,2,3,4,5]:
    line_bot_api.push_message(yourID, 
                              TextSendMessage(text='我們來倒數：'+str(i)))
    time.sleep(1)