class SignInScreen():
    def __init__(self, driver):
        self.driver = driver
        self.email_or_phone_input = self.driver.instance.find_element_by_id('ap_email')
        #self.password_input = self.driver.instance.find_element_by_id('ap_password')
        self.continue_button = self.driver.instance.find_element_by_id('continue')
        self.create_account_link = self.driver.instance.find_element_by_id('createAccountSubmit')

    def validate_url(self):
        current_url = self.driver.instance.current_url
        assert "signin" in current_url