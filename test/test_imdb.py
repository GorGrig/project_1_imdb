import sys
sys.path.append('/home/hrayr/imdb_site_test_case/')

from pom.Homepage_Nav import HomePage
import pytest



@pytest.mark.usefixtures("setup_teardown_driver_firefox")
class TestIMDBHomePage:
   
   def test_sign_in_positive(self):
      homepage = HomePage(self.driver)
      username = homepage.sign_in_positive()
      assert username != "Sign In"   
   
   @pytest.mark.parametrize('email, password', [
      ("bdhftdy@fly.net", "hHC63MZBeJenLp9"),
      #("tixava8831@lenfly.com", "drDRwdd3658kKL5"),
      #("bdhftdy@fly.net", "drDRwdd3658kKL5")
      ])  
   def test_sign_in_negative(self, email, password):
      homepage = HomePage(self.driver)
      result = homepage.sign_in_negative(email=email, password=password)
      text = "We cannot find an account with that email address Your password is incorrect"
      #assert result in text
   # To better protect your account, please re-enter your password and then enter the characters as they are shown in the image below.
   
   '''
   @pytest.mark.parametrize('name_move, excpected_result', [
      ("The Terminator", 'Results for "The Terminator"'),
      ("tryexcpect", 'No results found for "tryexcpect"')
   ])  
   def test_search_field(self, name_move, excpected_result):
      homepage = HomePage(self.driver)
      text = homepage.search_field_check(name_move)
      assert text == excpected_result
      
   def test_menu_button(self):
      homepage = HomePage(self.driver)
      txt = homepage.menu_button_test()
      assert "Movies" == txt
      
   def test_change_language(self):
      homepage = HomePage(self.driver)
      txt = homepage.language_change()
      assert txt == "Suivante"
         
   @pytest.mark.parametrize('button_social_network_xpath, social_network_home_page_link', [
      ('//*[@id="iconContext-facebook"]', 'https://www.facebook.com/imdb'),
      ('//*[@id="iconContext-instagram"]', 'https://www.instagram.com/imdb/'),
      ('//*[@id="iconContext-twitch"]', 'https://www.twitch.tv/IMDb'),
      ('//*[@id="iconContext-twitter"]', 'https://twitter.com/imdb'),
      ('//*[@id="iconContext-youtube"]', 'https://www.youtube.com/imdb')
   ])
   def test_sotial_network_links(self, button_social_network_xpath, social_network_home_page_link):
      homepage = HomePage(self.driver)
      txt = homepage.social_natworks_links_check(button_social_network_xpath)
      assert txt == social_network_home_page_link
      
   '''