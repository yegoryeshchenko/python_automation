from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

webdriver = WebDriver()

webdriver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
sleep(3)


def element_by_xpath(xpath):
    return webdriver.find_element(By.XPATH, xpath)


def elements_by_xpath(xpath):
    return webdriver.find_elements(By.XPATH, xpath)


def element_by_css_selector(css_selector):
    return webdriver.find_element(By.CSS_SELECTOR, css_selector)


def elements_by_css_selector(css_selector):
    return webdriver.find_elements(By.CSS_SELECTOR, css_selector)


def test_check_hello_descriptor():
    # 1
    assert element_by_xpath("//h1[@class='hero-descriptor_title display-2']").text == 'Do more!'
    assert element_by_css_selector(".hero-descriptor_title.display-2").text == 'Do more!'


def test_check_registration_form():
    # 2
    element_by_xpath("//p/following-sibling::button[contains(@class, 'btn-primary')]").click()
    # element_by_css_selector("p ~ button").click()
    # 3
    sleep(2)
    assert element_by_xpath("//div[@class='form-group']/label[@for='signupEmail']").text == 'Name'
    assert element_by_css_selector(".form-group > label[for='signupEmail']").text == 'Name'
    # 4
    assert element_by_xpath("//h4[@class='modal-title']").text == "Registration"
    assert element_by_css_selector('.modal-title').text == "Registration"
    # 5
    assert element_by_xpath('//form').is_displayed()
    assert element_by_css_selector('form').is_displayed()
    # 6
    assert element_by_xpath("//label[.='Password']").text == 'Password'
    assert element_by_css_selector('label[for="signupPassword"]').text == 'Password'
    # 7
    assert element_by_xpath("//*[contains(text(), 'Register')]").is_enabled() == False
    assert element_by_css_selector('*[type="button"][disabled]').is_enabled() == False
    # 8
    assert element_by_xpath('//*[@class="modal-header"]')
    assert element_by_css_selector('.modal-header').is_displayed() == True
    # 9
    sleep(1)
    element_by_xpath("//button[@aria-label='Close']/span").click()
    # element_by_xpath("button[aria-label='Close'] > span").click()
    sleep(1)


def test_check_nav_bar():
    # 10
    assert element_by_css_selector("[appscrollto='contactsSection']").is_displayed()
    assert element_by_xpath('//*[@appscrollto="contactsSection"]').is_displayed()
    # 11
    assert element_by_css_selector("[appscrollto*='about']").is_enabled()
    assert element_by_xpath("//*[contains(@appscrollto, 'about')]").is_displayed()
    # 12
    assert element_by_xpath("//a[@class='header_logo']/../../..").get_attribute('class') == 'container'
    assert element_by_css_selector('.header.bg-basic-dark > div').get_attribute('class') == 'container'
    # 13
    assert element_by_xpath(
        "//*[@class='col-12 col-lg-6']//*[@class='about-block_descr lead'] | //*[contains(text(), 'Keep')] ").text == \
           'Keep track of your replacement schedule and plan your vehicle maintenance expenses in advance.'
    assert element_by_css_selector("p[class='about-block_descr lead']").is_displayed() == True
    # 14
    assert element_by_xpath("//*[contains(@class, 'footer_item')][1]").is_displayed()
    assert element_by_css_selector("[class~='footer_item']").is_displayed()
    # 15
    assert len(webdriver.find_elements(By.XPATH, '//p')) == 7
    assert len(webdriver.find_elements(By.CSS_SELECTOR, 'p')) == 7
    # 16
    assert element_by_xpath("//a[@href='https://ithillel.ua'][1]").text == "ithillel.ua"
    assert element_by_css_selector("a[href='https://ithillel.ua']:nth-child(1)").text == 'ithillel.ua'
    # 17
    assert element_by_xpath(
        "//div[contains(@class, 'flex-md-row align-items-center')]//p[1]").text == "© 2021 Hillel IT school"
    assert element_by_css_selector(
        "div[class*='flex-md-row align-items-center'] > div > p:nth-child(1)").text == "© 2021 Hillel IT school"
    # 18
    assert element_by_xpath("//button[contains(@class, 'header-link -guest')]").is_displayed() == True
    element_by_css_selector("button[class*='header-link -guest']").click()
    # 19
    assert len(elements_by_xpath("//button")) == 3
    assert len(elements_by_css_selector("button")) == 3
    # 20
    assert len(elements_by_xpath("//*[@routerlink]")) == 10
    assert len(elements_by_css_selector("[routerlink]")) == 10
    # 21
    assert element_by_xpath("//button[@id='userNavDropdown']").is_displayed()
    element_by_css_selector('button#userNavDropdown').click()
    # 22
    assert len(elements_by_xpath("//*[contains(@routerlink, '/panel')]")) == 6
    assert len(elements_by_css_selector("[routerlink*='panel']")) == 6
    # 23
    assert element_by_xpath("//button[@class='btn btn-primary']/preceding-sibling::h1").is_displayed()
    assert element_by_css_selector("h1 + button.btn.btn-primary").is_displayed()
    # 24
    assert element_by_xpath("//button/img").is_displayed()
    assert element_by_css_selector("button > img").is_displayed()
    # 25
    assert element_by_xpath(
        "//div[@class='panel-page_empty panel-empty']//p").text == "You don’t have any cars in your garage"
    assert element_by_css_selector("div > svg + p").text == "You don’t have any cars in your garage"
