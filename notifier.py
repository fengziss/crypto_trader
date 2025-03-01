from wxpy import Bot
import json
import os

def send_wechat(msg):
    try:
        # TencentOS路径适配
        config_path = os.path.join(os.path.dirname(__file__), '../config/api_keys.json')
        with open(config_path) as f:
            wechat_id = json.load(f)['WECHAT']['username']
        
        # 使用固定缓存路径
        cache_path = os.path.join(os.path.dirname(__file__), '../wxpy.pkl')
        bot = Bot(cache_path=cache_path, console_qr=False)
        friend = bot.friends().search(wechat_id)[0]
        friend.send(msg)
    except Exception as e:
        print(f"微信通知失败: {e}")