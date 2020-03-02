link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    button_text = browser.find_element_by_css_selector("button.btn-add-to-basket").text
    assert button_text != ""


