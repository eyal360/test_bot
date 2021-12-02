import os
import sqlite3
import sys
import time
from selenium import webdriver

def add_com(browser):
    cfile = open(os.path.join(sys.path[0], "what_to_comment.txt"),
                 'r')  # same procedure as opening links to create a list of comments
    coms = cfile.read().split(' :break: ')
    for com in coms:  # navigating through the list of comments
        try:
            combox = browser.find_element_by_css_selector(
                "textarea[class*='mentions-input']")  # find the text area where the new comments are to be added
            combox.send_keys(com)
            time.sleep(1)  # time interval after typing the current comment in the comment box
            p_btn = browser.find_element_by_css_selector(
                "button[value='Post']")  # finding the post button which turned blue after typing the comment and clicking it
            p_btn.click()
            time.sleep(
                3)  # time interval after clicking the "post" button to wait for the comment to be shown and the comment box to become available
        except:
            break

def del_usr_coms(uname, browser):
    lst = browser.find_elements_by_css_selector(
        "div[data-sigil='comment']")  # used to select all the comments as a list
    for ele in lst:
        chld = ele.find_element_by_css_selector(
            "div[class]+div[class]")  # find the html tag containing the name of the author
        author = chld.find_element_by_css_selector('a[href]')
        if author.text == uname:  # in case the author name of the comment is same as the supplied username to the script, this bloc deletes the comment
            btn = ele.find_element_by_css_selector(
                "a[data-store*='editComment']")  # find the button which enables "more" actions on the comment
            btn.click()
            time.sleep(1)  # time control after clicking the "more" button
            btn = browser.find_element_by_css_selector(
                "a[data-sigil='touchable touchable deleteCommentSigil enabled_action']")  # find the delete button which is enabled after clicking "more"
            btn.click()
            time.sleep(
                1)  # time control after clicking the "delete button" waiting for the confirm delete pop up to arise
            obj = browser.switch_to.alert  # switch the webriver control to the popup alert and confirm the deletion of comment
            obj.accept()
            time.sleep(1)  # time interval after deleting the comment before moving on to next comment in the list

def share_post(browser):
    s_btn = browser.find_element_by_css_selector(
        "a[data-click*='click_share_ufi']")  # to find the "share" button which is underneath the post content and click it
    s_btn.click()
    time.sleep(3)  # time interval to wait for the share menu to emerge
    btn = browser.find_element_by_css_selector(
        "a[data-sigil='touchable touchable share-one-click-button']")  # find the share now button which quickly just shares the post to your timeline
    btn.click()
    time.sleep(3)  # time interval after sharing the post for the confirmation dialogue to appear on the screen

def open_posts(uname, browser, share_state):
    links = []

    with open(SYSTEM_PATH + 'what_to_advertise.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if 'http' in line:
                links.append(line.rstrip())

    for link in links:  # navigating through the list of links
        browser.get(str(link))  # open the current link and wait for a second
        time.sleep(5)
        del_usr_coms(uname,
                     browser)  # find all the comments made by the user on the currently opened post and delete them
        time.sleep(2)
        add_com(browser)  # add comments on the post
        if (share_state):
            share_post(browser)  # share the post in case the share_state is true
    time.sleep(5)  # time interval after the script execution is complete
    browser.quit()  # closing the webdriver

def login(email, passwrd, browser):
    browser.get('https://m.facebook.com')  # .get() function is used to open links in the webdriver
    uname = browser.find_element_by_css_selector("input[name='email']")  # find the text input where email is entered
    uname.send_keys(
        email)  # .send_keys() is used to type text in compatible inputs or textareasin this case its email id

    pswd = browser.find_element_by_css_selector("input[name='pass']")  # following the same procedure to enter password
    pswd.send_keys(passwrd)

    btn = browser.find_element_by_css_selector("button[name*='login']")  # find the login button and click it
    btn.click()

def execute_script(email, pswrd, uname, share_state):
    browser = webdriver.Chrome(executable_path=SYSTEM_PATH+'chromedriver.exe')
    login(email, pswrd, browser)
    time.sleep(
        3)  # this is the time interval after the login button press to make sure the login process is complete before opening the post links
    open_posts(uname, browser, share_state)

def get_user_cred():
    DB = SYSTEM_PATH + 'database.db'
    platform = 'system'
    db_connect = sqlite3.connect(DB)
    cursor = db_connect.cursor()
    cursor.execute("SELECT *,oid FROM users WHERE platform=:platform",
                   {'platform': platform
                    })
    cred = cursor.fetchone()
    cursor.close()
    db_connect.close()

    print(cred)
    return cred

if __name__ == '__main__':
    email, pswrd, uname = get_user_cred()
    SYSTEM_PATH = 'קבצי מערכת - לא לגעת/'

    cycle = 0

    while True:  # this has to remain true to create an infinite loop of cycles
        #        share_state = input('Would you like to share? (y/n) ')
        #        if share_state == 'y':
        #            sharing = True
        #        else:
        #            sharing = False
        #        try:
        execute_script(email, pswrd, uname, False)
        #        except:
        cycle += 1
        #        print('Something went wrong(check internet connection)')
        print('Finished ' + str(cycle) + ' cycle')
        time.sleep(3600 * 5)  # time interval after each cycle
