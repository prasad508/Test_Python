class LoginPage():
    def __init__(self, dr):
        self.dr = dr
        self.username_textbox_id = "txtUsername"
        self.password_text_id = "txtPassword"
        self.login_button_id = "btnLogin"

    def enter_username(self, username):
        self.dr.find_element_by_id(self.username_textbox_id).clear()
        self.dr.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.dr.find_element_by_id(self.password_text_id).clear()
        self.dr.find_element_by_id(self.password_text_id).send_keys(password)

    def click_login(self):
        self.dr.find_element_by_id(self.login_button_id).click()


