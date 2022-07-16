import sys
sys.path.append('/home/hrayr/imdb_site_test_case/')

from pom.Homepage_Nav import HomePage
import pytest



@pytest.mark.usefixtures("setup_teardown_driver_firefox")
class TestIMDBHomePage:
   
   def test_sign_in_positive(self):
      homepage = HomePage(self.driver)
      text = homepage.sign_in_positive(valid_email="bamilob426@storypo.com", valid_password="hxdygc57541j")
      assert text == "Sign out", 'The test failed because the site identified you as a bot.\nPlease enter another valid email and password'
 
   @pytest.mark.parametrize('email, password, excpected_result', [
      ("armanatanesyan@mail.com", "armantjy584", "We cannot find an account with that email address"),
      ("tixava8831@lenfly.com", "drjnhkKL5", "Your password is incorrect"),
      ("harutgasparyan@mail.ru", "dvrmgfcr658kKL5", "We cannot find an account with that email address")
      ])
   def test_sign_in_negative(self, email, password, excpected_result):
      homepage = HomePage(self.driver)
      result = homepage.sign_in_negative(email=email, password=password)
      assert result == excpected_result, 'The test failed because the site identified you as a bot.\nPlease enter another invalid email or password'
   
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
      ('//*[@id="iconContext-instagram"]', 'https://www.instagram.com/accounts/login/?next=/imdb/https://www.instagram.com/imdb/'),
      ('//*[@id="iconContext-twitch"]', 'https://www.twitch.tv/IMDb'),
      ('//*[@id="iconContext-twitter"]', 'https://twitter.com/imdb'),
      ('//*[@id="iconContext-youtube"]', 'https://www.youtube.com/imdb')
   ])
   def test_sotial_network_links(self, button_social_network_xpath, social_network_home_page_link):
      homepage = HomePage(self.driver)
      txt = homepage.social_natworks_links_check(button_social_network_xpath)
      assert txt in social_network_home_page_link