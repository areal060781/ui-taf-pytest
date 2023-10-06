import pytest

from values import strings
from pageobjects.showsearchscreen import ShowSearchScreen as SearchScreen
from pageobjects.showresultsscreen import ShowResultsScreen as ResultsScreen


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('headless')
    return chrome_options


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.headless = True
    return firefox_options


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(3)
    selenium.maximize_window()
    return selenium


def test_show_search(selenium):
    selenium.get('http://localhost:3000/shows')

    search = SearchScreen(selenium)
    search.run('batman')

    results = ResultsScreen(selenium)
    results.go_external_url_by_index(2)

    selenium.back()

    results.change_background_color_by_result_title('Batman Unlimited', '#4a148c')
    results.press_back_button()

    search.validate_input_search_is_empty()