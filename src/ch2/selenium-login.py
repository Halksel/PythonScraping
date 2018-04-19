from selenium import webdriver

USER = "JS-TESTER"
PASS = "ipCU12ySxI"

browser = webdriver.Firefox()
browser.implicitly_wait(3)

url_login = "https://uta.pw/sakusibbs/users.php?action=login"
browser.get(url_login)
print("login to webpage")

e = browser.find_element_by_id("user")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pass")
e.clear()
e.send_keys(PASS)

frm = browser.find_element_by_css_selector("#loginForm form")
frm.submit()

a = browser.find_element_by_css_selector(".islogin a")
url_mypage = a.get_attribute('href')
print("mypage's =",url_mypage)

browser.get(url_mypage)

links = browser.find_elements_by_css_selector("#favlist li > a")
for a in links:
    href = a.get_attribute('href')
    title = a.text
    print("-",title,">",href)
