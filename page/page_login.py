from base.base_login import BaseLogin
import page


class PageLogin(BaseLogin):
    # 输入手机号
    def page_phone(self, phone):
        self.base_input(page.login_phone, phone)

    # 输入密码
    def page_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击登录
    def page_click_btn(self):
        self.base_click(page.login_click)

    # 组合业务方法
    def page_login(self, phone, pwd):
        self.page_phone(phone)
        self.page_pwd(pwd)
        self.page_click_btn()
