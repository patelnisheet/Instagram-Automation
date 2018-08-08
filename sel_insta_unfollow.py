from selenium import webdriver
from time import sleep

browser= webdriver.Chrome("C:/Jars/chromedriver")
browser.get("https://www.instagram.com/username/followers/")  #username
sleep(3)
browser.find_elements_by_xpath("//input[@name='username']")[0].send_keys("username")   #username
browser.find_elements_by_xpath("//input[@name='password']")[0].send_keys("password")    #password
browser.find_elements_by_css_selector("span button._5f5mN.jIbKX.KUBKM.yZn4P")[0].click()
sleep(5)
browser.get("https://www.instagram.com/username/followers/")    #username
sleep(2)

total_follower=int(browser.find_elements_by_xpath("//ul/li/a/span")[0].get_attribute("innerHTML"))
total_following=int(browser.find_elements_by_xpath("//ul/li/a/span")[1].get_attribute("innerHTML"))

browser.find_element_by_partial_link_text("followers").click()
sleep(5)
j=0

followers=[]

while j<total_follower:
    elem=list(browser.find_elements_by_css_selector("a.FPmhX.notranslate.zsYNt"))
    for i in range(j,len(elem)):
        followers.append(elem[i].get_attribute("title"))
        j=i+1
        print(j)
    src=browser.find_element_by_xpath("//div[@class='PdwC2 HYpXt']/div[@class='j6cq2']")
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",src)

browser.find_element_by_xpath("//button[@class='ckWGn']").click()

browser.find_element_by_partial_link_text("following").click()
sleep(5)

k=0
unfollow_count=0
while k < total_following:
    elem=list(browser.find_elements_by_css_selector("a.FPmhX.notranslate.zsYNt"))
    for i in range(k,len(elem)):
        if (str(elem[i].get_attribute("title"))) not in followers:
            browser.find_elements_by_css_selector("div.BW116")[i].click()
            sleep(1)
            browser.find_element_by_css_selector("button.aOOlW.-Cab_").click()
            sleep(1)
            unfollow_count=unfollow_count+1
            print(unfollow_count)
        k=i+1
        if unfollow_count==20:
            sleep(60*15)  #sleep for 15 minutes because if you can not unfollow all following at once
            unfollow_count=0
    src=browser.find_element_by_xpath("//div[@class='PdwC2 HYpXt']/div[@class='j6cq2']")
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",src)
broser.close()
