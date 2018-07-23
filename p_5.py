# coding=utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os, time, subprocess

# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.maximize_window()
# driver.set_window_size(800, 600)

# driver.find_element_by_id('kw').clear()
# driver.find_element_by_id('kw').send_keys('good job')
# driver.find_element_by_id('su').click()
# time.sleep(10)
# driver.quit()
# locate = driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
# ActionChains(driver).move_to_element(locate).perform()
# driver.find_element_by_link_text('高级搜索').click()
# driver.find_element_by_css_selector("form[name='f1']>div>table>tbody>tr>td#adv-setting-1>input#adv_keyword").send_keys('woola')

# 测试xpath & css
# driver.find_element_by_xpath("//form/span/input[@id='kw']").send_keys('nail') # this part worked
# driver.find_element_by_css_selector("form[name='f']>span>input#kw").send_keys('nail') # this part worked

# driver.find_element_by_xpath("//form/span/input[@id='kw']").send_keys('popgreen')
# driver.find_element_by_xpath("//form/span/input[@id='kw']").send_keys(Keys.ENTER)


# check = 'file:///' + os.path.abspath('c:/23.html')
# driver = webdriver.Chrome()
# driver.get(check)
# driver.implicitly_wait(10)
# driver.find_element_by_css_selector('#controlAll').click()
# driver.find_element_by_css_selector('body > form > input[type="checkbox"]:nth-child(9)').click()

# locat2 = driver.find_elements_by_css_selector('body > form > input[type="checkbox"]')
# print 'lo1:', len(locat2)
# locat2[0].click()
# print 'lo2:', len(locat2)

# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# # element = WebDriverWait(driver, 5, 0.5).until(EC.title_is(u'百度一下，你就知道'))
# element1 = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, "kw")))
#
# element1.send_keys('selenium')
# time.sleep(2)
# driver.quit()

# cmd = 'cmd.exe c:/kill.bat'
# p = subprocess.Popen('cmd.exe /c' + 'c:/kill.bat abc', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# curline = p.stdout.readline()
# while(curline != b''):
#     print(curline)
#     curline = p.stdout.readline()
#
# p.wait()
# print(p.returncode)


# print dir(webdriver.support.expected_conditions)



# import re, datetime
# f0 = open(r'C:\Users\Administrator\Desktop\for_python\wt.txt')
# pat = r"\d\d:\d\d:\d\d"
# f1 = f0.read()
# l0 = re.findall(pat, f1)
#
# temp = []
# for i in l0:
#     h = int(i[0: 2])
#     m = int(i[3: 5])
#     s = int(i[6:])
#     delta = datetime.timedelta(seconds = 4)
#     t = datetime.datetime(2018, 07, 20, h, m, s) - delta
#     t1 = datetime.datetime.strftime(t, '%H:%M:%S')
#     temp.append(t1)
#
# result = []
# for i in range(len(temp)):
#     f1 = f1.replace(l0[i], temp[i])
#
# new = open(r'C:\Users\Administrator\Desktop\for_python\neww.srt', 'w')
# new.write(f1)
# f0.close()
# new.close()


import os
y = r'd:/output/new.src'
# print y[0:10]
if os.path.exists(y[0:10]):
    print "it's already exists"
else:
    print 'make dir'
    os.mkdir(y[0:10])






























































