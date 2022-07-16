import sys
sys.path.append('/home/hrayr/imdb_site_test_case/')
from base.Selenium_base import SeleniumBase




class HomePage(SeleniumBase):
    
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver
        self.__button_sign_in_xpath = "/html/body/div[2]/nav/div[2]/div[5]/a/div"
        self.__button_sign_in_with_IMDB_xpath = "/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[1]/a[1]/span[2]"
        self.__email_field_id = "ap_email"
        self.__password_field_id = "ap_password"
        self.__sing_in_button_id = "signInSubmit"
        self.__user_name_xpath = "/html/body/div[2]/nav/div[2]/div[5]/div/label[2]/div/span"
        self.__message_window_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/ul/li/span"      
        self.__search_field_id = "suggestion-search"
        self.__result_wind_xpath = "/html/body/div[2]/div/div[2]/div[3]/div[1]/div/h1"
        self.__find_buttom_xpath = '//*[@id="iconContext-magnify"]'
        self.__menu_button_xpath = '/html/body/div[2]/nav/div[2]/label[2]/div'
        self.__menu_block_title_xpath = '/html/body/div[2]/nav/div[2]/aside/div/div[2]/div/div[1]/span/label/span[2]'
        self.__language_button_xpath = '/html/body/div[2]/nav/div[2]/div[6]/label/div'
        self.__language_franch_button_xpath = '/html/body/div[2]/nav/div[2]/div[6]/div/div/span/ul[2]/li[3]/span[2]'
        self.__up_next_txt_xpath = '/html/body/div[2]/main/div/div[3]/div[1]/div/div/div[2]/div[1]/div[1]/span'        
        self.__sign_out_xpath = '/html/body/div[2]/nav/div[2]/div[5]/div/div/div/span/ul/a[6]/span'

        
    def sign_in_positive(self, valid_email, valid_password) -> str:
        self.is_visible_element_click("xpath", self.__button_sign_in_xpath)
        self.is_visible_element_click("xpath", self.__button_sign_in_with_IMDB_xpath)
        self.send_text_to_field("id", self.__email_field_id, valid_email)
        self.wait_time(2)
        self.send_text_to_field("id", self.__password_field_id, valid_password)
        self.is_visible_element_click("id", self.__sing_in_button_id)
        self.is_visible_element_click("xpath", self.__user_name_xpath)
        return self.get_text('xpath', self.__sign_out_xpath)
    
    def sign_in_negative(self, email : str, password : str) -> str:
        self.is_visible_element_click("xpath", self.__button_sign_in_xpath)
        self.is_visible_element_click("xpath", self.__button_sign_in_with_IMDB_xpath)
        self.send_text_to_field("id", self.__email_field_id, email)        
        self.wait_time(3)
        self.send_text_to_field("id", self.__password_field_id, password)
        self.is_visible_element_click("id", self.__sing_in_button_id)    
        return self.get_text("xpath", self.__message_window_xpath)
    
    def search_field_check(self, name_move : str) -> str:
        self.send_text_to_field("id", self.__search_field_id, name_move)
        self.is_visible_element_click("xpath", self.__find_buttom_xpath)
        return self.get_text("xpath", self.__result_wind_xpath)
        
    def menu_button_test(self) -> str:
        self.is_visible_element_click('xpath', self.__menu_button_xpath)
        return self.get_text("xpath", self.__menu_block_title_xpath)
    
    def language_change(self) -> str:
        self.is_visible_element_click("xpath", self.__language_button_xpath)
        self.is_visible_element_click("xpath", self.__language_franch_button_xpath)
        return self.get_text("xpath", self.__up_next_txt_xpath)

    def social_natworks_links_check(self, button_social_network_xpath) -> str:
        self.scoll()
        self.is_visible_element_click("xpath", button_social_network_xpath)
        self.switching_between_tabs(1)
        self.wait_time(7)
        return self.get_current_url()