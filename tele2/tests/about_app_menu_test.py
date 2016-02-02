# coding=utf-8
from core.base_test import BaseTest


class AboutAppMenuTest(BaseTest):

    def test_1_about_app_menu(self):
        # Test data
        expected_title = u'Översikt'

        # Test steps

        # Test asserts
        self.assertEqual(self.driver.find_element_by_id("title").text, expected_title)

    def test_2_unsuccessful_login(self):
        # Test data
        login = ''
        password = ''

        # Test steps
        self.driver.find_element_by_id("go_to_app_btn").click()

        self.driver.find_element_by_xpath("//*[contains(@class, 'EditText') and @resource-id='loginForm.username']").send_keys(login)
        self.driver.find_element_by_xpath("//*[contains(@class, 'EditText') and @resource-id='loginForm.password']").send_keys(password)

        self.driver.find_element_by_xpath("//*[@content-desc='Logga in']").click()

        # Test asserts