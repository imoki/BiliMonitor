from .. import re, json, os
from ...views.prompt_view import PromptView

class HomeService():
    def __init__(self, **kwargs): # cookie_path, daily_cookie_path
        self.cookie = ""
        # print(kwargs)
        self.parent = kwargs.get('parent', '')  # os.path.join(os.path.dirname(__file__), 'cookie.json')
        self.daily_cookie_path = kwargs.get('daily_cookie_path', '')
        self.configManager = kwargs.get('configManager', '')
        self.prompt_view = PromptView(self.parent)
    # 保存cookie
    def save_cookie(self):
        value = self.parent.ui.textEdit_home_1.toPlainText()
        if not value:
            self.prompt_view.prompt(text="请输入cookie", type="warning")
            return

        # 格式化cookie，清除value前后空格和换行
        value = re.sub(r'[\s\n]', '', value)

        self.prompt_view.prompt(text="保存成功", type="success")
        self.configManager.update_config("cookie", value)


        self.cookie = value

        # 将cookie值转存一份到cookies.json中，用于执行每日任务
        # 读取 cookies.json 文件，如果文件不存在则创建一个空的 JSON 对象
        if os.path.exists(self.daily_cookie_path):
            with open(self.daily_cookie_path, 'r', encoding='utf-8') as cookies_file:
                cookies_data = json.load(cookies_file)
        else:
            cookies_data = {}

        # 确保 cookies_data 中存在 BiliBiliCookies 键
        if 'BiliBiliCookies' not in cookies_data:
            cookies_data['BiliBiliCookies'] = []

        # 将 config.json 中的 cookie 值添加到 cookies.json 中的 BiliBiliCookies 列表
        cookies_data['BiliBiliCookies'] = [self.cookie]
        # 写回 cookies.json 文件
        with open(self.daily_cookie_path, 'w', encoding='utf-8') as cookies_file:
            json.dump(cookies_data, cookies_file, ensure_ascii=False, indent=2)

    