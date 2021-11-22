import os
import sys
import time
from selenium import webdriver

def add_com(browser):
    cfile = open(os.path.join(sys.path[0], "coms.txt"),
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
    #    link_file = open(os.path.join(sys.path[0], "links.txt"), 'r') #open the links file and read its content as a single string
    #    links = link_file.read().split(' :break: ') #split the total text in links file into a list of strings/ URLs
    #    link_file.close()
    mercedes_wheel = ['https://m.facebook.com/groups/1426418190986868/posts/2732975843664423',
                  'https://m.facebook.com/groups/159347124910017/permalink/946329936211728/?sale_post_id=946329936211728',
                  'https://m.facebook.com/groups/1636903359880434/permalink/3071492296421526/?sale_post_id=3071492296421526',
                  'https://m.facebook.com/groups/1206797219459205/permalink/3144305892374985/?sale_post_id=3144305892374985',
                  'https://m.facebook.com/groups/benzishop4u/permalink/3134877586798876/?sale_post_id=3134877586798876',
                  'https://m.facebook.com/groups/1639631189671254/permalink/2663272793973750/?sale_post_id=2663272793973750',
                  'https://m.facebook.com/groups/1535010683480811/permalink/2881076765540856/?sale_post_id=2881076765540856',
                  'https://m.facebook.com/groups/722170757928336/permalink/2707131212765604/?sale_post_id=2707131212765604',
                  'https://m.facebook.com/groups/1533233360297413/permalink/2994467637507304/?sale_post_id=2994467637507304',
                  'https://m.facebook.com/groups/1513975295589591/permalink/3143155376004900/?sale_post_id=3143155376004900',
                  'https://m.facebook.com/groups/902227499892708/permalink/5571745829607495/?sale_post_id=5571745829607495',
                  'https://m.facebook.com/groups/1648989485390976/permalink/2729136134042967/?sale_post_id=2729136134042967',
                  'https://m.facebook.com/groups/132058890503290/permalink/1478900665819099/?sale_post_id=1478900665819099',
                  'https://m.facebook.com/groups/Shpilsher/permalink/4254018374667515/?sale_post_id=4254018374667515',
                  'https://m.facebook.com/groups/konimzolyad2/permalink/2075735795899818/?sale_post_id=2075735795899818',
                  'https://m.facebook.com/groups/436216826415896/permalink/4252486821455525/?sale_post_id=4252486821455525',
                  'https://m.facebook.com/groups/1111390508890562/permalink/4804197316276511/?sale_post_id=4804197316276511'
                  ]

    guillotine = [
        'https://m.facebook.com/groups/konimzolyad2/permalink/2075749145898483/?sale_post_id=2075749145898483',
        'https://m.facebook.com/groups/1206797219459205/permalink/3144316305707277/?sale_post_id=3144316305707277',
        'https://m.facebook.com/groups/436216826415896/permalink/4252525514784989/?sale_post_id=4252525514784989',
        'https://m.facebook.com/groups/Shpilsher/permalink/4254056674663685/?sale_post_id=4254056674663685',
        'https://m.facebook.com/groups/1426418190986868/permalink/2732985303663477/?sale_post_id=2732985303663477',
        'https://m.facebook.com/groups/benzishop4u/permalink/3134887433464558/?sale_post_id=3134887433464558',
        'https://m.facebook.com/groups/1111390508890562/permalink/4804231652939744/?sale_post_id=4804231652939744',
        'https://m.facebook.com/groups/159347124910017/permalink/946338189544236/?sale_post_id=946338189544236',
        'https://m.facebook.com/groups/902227499892708/permalink/5571789122936499/?sale_post_id=5571789122936499',
        'https://m.facebook.com/groups/yad22222/permalink/2985863054985231/?sale_post_id=2985863054985231',
        'https://m.facebook.com/groups/1535010683480811/permalink/2881090485539484/?sale_post_id=2881090485539484',
        'https://m.facebook.com/groups/1513975295589591/permalink/3143167802670324/?sale_post_id=3143167802670324',
        'https://m.facebook.com/groups/1639631189671254/permalink/2663282127306150/?sale_post_id=2663282127306150'
    ]

    suitcase = ['https://m.facebook.com/groups/436216826415896/posts/4252544151449792',
                'https://m.facebook.com/groups/132058890503290/permalink/1478918419150657/?sale_post_id=1478918419150657',
                'https://m.facebook.com/groups/1533233360297413/permalink/2994480790839322/?sale_post_id=2994480790839322',
                'https://m.facebook.com/groups/benzishop4u/permalink/3134894600130508/?sale_post_id=3134894600130508',
                'https://m.facebook.com/groups/konimzolyad2/permalink/2075754995897898/?sale_post_id=2075754995897898',
                'https://m.facebook.com/groups/1535010683480811/permalink/2881096058872260/?sale_post_id=2881096058872260',
                'https://m.facebook.com/groups/1206797219459205/permalink/3144323032373271/?sale_post_id=3144323032373271',
                'https://m.facebook.com/groups/1513975295589591/permalink/3143175902669514/?sale_post_id=3143175902669514',
                'https://m.facebook.com/groups/159347124910017/permalink/946342796210442/?sale_post_id=946342796210442',
                'https://m.facebook.com/groups/722170757928336/permalink/2707150209430371/?sale_post_id=2707150209430371',
                'https://m.facebook.com/groups/159347124910017/permalink/946342732877115/?sale_post_id=946342732877115',
                'https://m.facebook.com/groups/Shpilsher/permalink/4254078094661543/?sale_post_id=4254078094661543',
                'https://m.facebook.com/groups/1426418190986868/permalink/2732989746996366/?sale_post_id=2732989746996366',
                'https://m.facebook.com/groups/1206797219459205/permalink/3144323322373242/?sale_post_id=3144323322373242',
                'https://m.facebook.com/groups/Shpilsher/permalink/4254078414661511/?sale_post_id=4254078414661511',
                'https://m.facebook.com/groups/1636903359880434/permalink/3071508779753211/?sale_post_id=3071508779753211',
                'https://m.facebook.com/groups/1648989485390976/permalink/2729149270708320/?sale_post_id=2729149270708320',
                'https://m.facebook.com/groups/436216826415896/permalink/4252544151449792/?sale_post_id=4252544151449792',
                'https://m.facebook.com/groups/1535010683480811/permalink/2881095922205607/?sale_post_id=2881095922205607',
                'https://m.facebook.com/groups/482415075275045/permalink/1724064104443463/?sale_post_id=1724064104443463',
                'https://m.facebook.com/groups/yad22222/permalink/2985868844984652/?sale_post_id=2985868844984652',
                'https://m.facebook.com/groups/1111390508890562/permalink/4804260266270216/?sale_post_id=4804260266270216']

    chain = [
        'https://m.facebook.com/groups/132058890503290/permalink/1478922319150267/?sale_post_id=1478922319150267',
        'https://m.facebook.com/groups/1111390508890562/permalink/4804274196268823/?sale_post_id=4804274196268823',
        'https://m.facebook.com/groups/konimzolyad2/permalink/2075759252564139/?sale_post_id=2075759252564139',
        'https://m.facebook.com/groups/Shpilsher/permalink/4254092614660091/?sale_post_id=4254092614660091',
        'https://m.facebook.com/groups/436216826415896/permalink/4252562028114671/?sale_post_id=4252562028114671',
        'https://m.facebook.com/groups/1513975295589591/permalink/3143179799335791/?sale_post_id=3143179799335791',
        'https://m.facebook.com/groups/yad22222/permalink/2985871918317678/?sale_post_id=2985871918317678',
        'https://m.facebook.com/groups/1206797219459205/permalink/3144326339039607/?sale_post_id=3144326339039607',
        'https://m.facebook.com/groups/482415075275045/permalink/1724067294443144/?sale_post_id=1724067294443144',
        'https://m.facebook.com/groups/902227499892708/permalink/5571827936265951/?sale_post_id=5571827936265951',
        'https://m.facebook.com/groups/Shpilsher/permalink/4254092414660111/?sale_post_id=4254092414660111',
        'https://m.facebook.com/groups/722170757928336/permalink/2707155672763158/?sale_post_id=2707155672763158',
        'https://m.facebook.com/groups/132058890503290/permalink/1478922269150272/?sale_post_id=1478922269150272',
        'https://m.facebook.com/groups/1636903359880434/permalink/3071512549752834/?sale_post_id=3071512549752834',
        'https://m.facebook.com/groups/159347124910017/permalink/946345926210129/?sale_post_id=946345926210129',
        'https://m.facebook.com/groups/1111390508890562/permalink/4804274019602174/?sale_post_id=4804274019602174',
        'https://m.facebook.com/groups/436216826415896/permalink/4252561841448023/?sale_post_id=4252561841448023',
        'https://m.facebook.com/groups/1426418190986868/permalink/2732993490329325/?sale_post_id=2732993490329325',
        'https://m.facebook.com/groups/1639631189671254/permalink/2663291303971899/?sale_post_id=2663291303971899',
        'https://m.facebook.com/groups/1535010683480811/permalink/2881099358871930/?sale_post_id=2881099358871930',
        'https://m.facebook.com/groups/1648989485390976/permalink/2729153387374575/?sale_post_id=2729153387374575',
        'https://m.facebook.com/groups/1533233360297413/permalink/2994485234172211/?sale_post_id=2994485234172211',
        'https://m.facebook.com/groups/benzishop4u/permalink/3134897320130236/?sale_post_id=3134897320130236'
    ]
    grandma_warehouse = ['https://m.facebook.com/groups/879231698850734/permalink/3709413482499194',
                         'https://m.facebook.com/groups/com.real.luah1/permalink/1207016266382843',
                         'https://m.facebook.com/groups/226696460730867/posts/4259822884084851']

    bat_yam_apartment = ['https://m.facebook.com/marketplace/item/1494698827556868',
                         'https://m.facebook.com/groups/817575694971912/posts/4580389348690509',
                         'https://m.facebook.com/iamhomeisrael/posts/2925387241110833',
                         'https://m.facebook.com/permalink.php?story_fbid=1606402332896538&id=974574322746012',
                         'https://m.facebook.com/iamhomeisrael/posts/2925945464388344',
                         'https://m.facebook.com/groups/1494404674165851/permalink/3029429707329999']

    grandma_store = ['https://m.facebook.com/groups/com.real.luah1/permalink/1180046452413158',
                     'https://m.facebook.com/groups/1877701092313967/posts/4271690992914953',
                     'https://m.facebook.com/groups/879231698850734/permalink/4304150909692112',
                     'https://m.facebook.com/groups/2587977648098690/posts/3229935103902938']


    # ~~~~~~~~~~~~~~~~~~~~~~~  Choose here what to upvote ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    links = mercedes_wheel + guillotine + grandma_warehouse + suitcase + chain + grandma_store

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

if __name__ == '__main__':
    email = 'eyal_360@hotmail.com'  # enter your email
    pswrd = '3fy9fcnZ'  # enter password
    uname = 'Eyal Huri'  # enter your username
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
