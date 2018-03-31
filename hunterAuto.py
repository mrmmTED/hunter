from selenium import webdriver
import time
import random
import user_sendWord
import gl_set
import main_function
import os
import sys
import tkinter as tka
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get(gl_set.wwwWord)

# 定义一个全局计数变量
this_i = 0

win1 = tka.Tk()
win1.geometry('600x300+200+200')
win1.title("请先输入你要发送的小广告，然后根据需要选择是否在程序结束后自动关机。")

# 定义全局延时函数
def delay_time():
    driver.implicitly_wait(8)


# delay_time()
# 自动关机函数
def _close_computer():
    os.system("shutdown -s -t 120")


#     自动关机的选项配置
shutdown_num = 0
def _setFun1():
    global shutdown_num
    shutdown_num = 1
    user_sendWord.sendWord = text_send.get(1.0, "end")
    win1.destroy()


def _setFun2():
    global shutdown_num
    shutdown_num = 0
    user_sendWord.sendWord = text_send.get(1.0, "end")
    win1.destroy()

button_shutdown1 = tka.Button(win1, text = "自动关机", bg = "red", command = _setFun1 )
button_shutdown2 = tka.Button(win1, text = "不自动关机", command = _setFun2)
button_shutdown1.place(relx=0.5, rely=0.5)
button_shutdown2.place(relx=0.5, rely=0.5)
button_shutdown1.pack(side = "bottom")
button_shutdown2.pack(side = "bottom")
text_send = tka.Text(win1)
text_send.pack(side = "top")
win1.mainloop()


# 定义一个内部随机数函数，不要太僵化，假装自己不是机器人
def random_n():
    mbw = round(random.uniform(1, 3), 2)
    return mbw


# 定义frame之间跳转切换关闭窗口的一个复用函数
def close_frame():
    # print("跳出frame")
    # 跳到操作批量人选的frame里面，关掉已经操作完成的人选。
    driver.switch_to.default_content()
    driver.switch_to.frame("resume_title")
    # 定位到要悬停的元素
    close_target = driver.find_element_by_xpath("/html/body/div[1]/div/dl/dd/ul/li[1]/a")
    # 对定位到的元素执行鼠标悬停操作
    ActionChains(driver).move_to_element(close_target).perform()
    # 能看到关闭元素了，然后点击关闭
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div/dl/dd/ul/li[1]/i")
    except:
        time.sleep(2)
        ActionChains(driver).move_to_element(close_target).perform()
    driver.find_element_by_xpath("/html/body/div[1]/div/dl/dd/ul/li[1]/i").click()
    # 切换到人选frame
    driver.switch_to.default_content()
    driver.switch_to.frame("bottom")


# 点击我是猎头的按钮，等跳出新标签页
driver.find_element_by_link_text("我是猎头").click()

time.sleep(2+random_n())
#操作对象切换到新打开的标签页
driver.switch_to.window(driver.window_handles[1])
        # print(len(driver.window_handles))
        # driver.find_element_by_link_text("账户登录").click()
        # $$$$$$$$$$$$$$$$$$$暂时先不用这种自动登陆，先用人机配合解决问题再说。这个方法后继在测试，需要解决验证码问题，比较麻烦
        # driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/section[1]/div[1]/ul/li[2]").click()
        # #//html/body/div[1]/ol[1]/li[2]/h2/a/strong[2]
        # # /html/body/div[2]/main/div/ul[2]/li[2]/ul[2]/li[2]/a/h3
        # # # time.sleep(5)
        # driver.maximize_window()
        # driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/section[1]/div[2]/div[2]/form/div[1]/input").send_keys("18963985626")
#         等待手动扫码登陆
# delayTime()
# 点击人选

# 现在解决登陆的问题，验证码很难处理，等时间又比较傻，所以用弹出提示框来提示人工操作。
def _login():
    # print("登陆完成")
    # print(user_sendWord.sendWord)
    win2.destroy()
    if gl_set.gl_i < 3:
        try:
            driver.find_element_by_xpath("/html/body/div[5]/div[1]/a").click()
        except:
            time.sleep(1)
            try:
                driver.find_element_by_xpath("/html/body/div[5]/div[1]/a").click()
            except:
                print("出错了")
        time.sleep(3)
    # 点击进入筛选界面
    driver.find_element_by_xpath("/html/body/header/nav/div/ul/li[3]/div/a").click()
    # 点击设置好的筛选条件
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/ul/li[1]/a[2]").click()

    # 从第几页开始，这个是出了问题的时候，再次进入用的。/html/body/div[1]/div/table/tfoot/tr/td[2]/div/a[7]
    # driver.find_element_by_xpath("/html/body/div[1]/div/table/tfoot/tr/td[2]/div/a[7]").click()

    # 点击全选
    def pick_all():
        # print("进入全选")
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/p/label/i").click()

    # 点击批量查看
    def look_all():
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/p/a").click()

    # 点选下一页
    def next_page():
        if gl_set.gl_i < gl_set.max:
            driver.find_element_by_xpath("/html/body/div[1]/div/table/tfoot/tr/td[2]/div/a[8]").click()
        else:
            # print("到位了")
            driver.close()

    # 临时用函数
    # _mm = 0

    # while _mm < 13:
    #     _mm += 1
    #     next_page()

    # 以下为切换到批量操作的页面全称，直到关闭第三个页面，回到第二个页面为止。
    def page_three():
        # 切换到新打开的第三个标签页
        driver.switch_to.window(driver.window_handles[2])
        driver.switch_to.frame("resume_title")
        driver.implicitly_wait(3)
        numFrameButtons = len(driver.find_elements_by_xpath("/html/body/div[1]/div/dl/dd/ul/li"))  # 本处取得数组，为后继遍历操作做准备
        try:
            driver.find_element_by_xpath("/html/body/div[5]/div[1]/a").click()
        except:
            print("没有弹出界面")
        # driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/a/img")
        driver.switch_to.default_content()
        # 进入界面frame，开始关注，搭讪等操作
        driver.switch_to.frame("bottom")
        # 如果当前是没有关注的人选，则进行关注
        # 遍历当前数组的长度，如果长度为1，则为最后一个元素，关了后就要回到前一个页面继续再选一批关注。如果不是最后一个，则关了继续循环。
        # print(numFrameButtons)
        while numFrameButtons > 0:  # 遍历数组循环操作，当数组为零时跳出
            # print("*********              *********")
            # gl_set.print_time()
            try:
                driver.find_element_by_link_text("+ 关注")
                this_bool = True
            except:
                this_bool = False
            if this_bool:
                # 选中输入框
                if gl_set.gl_i < 3:
                    try:
                        driver.find_element_by_xpath("/html/body/div[6]/a").click()
                    except:
                        time.sleep(3)
                driver.find_element_by_link_text("沟通记录").click()

                def _if_can_continue():
                    try:
                        driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]/div[2]/div[4]/textarea")
                        return True
                    except:
                        return False

                while _if_can_continue():
                    # 输入搭讪文字  /html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div/a[2]
                    driver.find_element_by_xpath(
                        "/html/body/div[3]/div/div[3]/div[2]/div[2]/div[4]/textarea").send_keys(
                        user_sendWord.sendWord)
                    # 发送搭讪文字
                    driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]/div[2]/div[5]/a").click()
                    # 点击弹出界面上的关注
                    driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[1]/div/div/div/a/em").click()
                    # 在弹出的界面中选择IT技术专家，本处现在的写法是写死的，需要调整，因为这个地方是变动的。
                    # driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div/div/div/dl[22]/dd/p/a").click()
                    driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div/div/div/h2/p/a").click()
                    # lisa的品牌关注
                    # driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div/div/div/dl[5]/dd/p[23]/a").click()
                    # 崔巍的销售关注设置
                    # driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div/div/div/dl[10]/dt/p/a").click()
                    # 周婷的大数据关注设置
                    # driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div/div/div/dl[26]/dt/p/a").click()
                    # 王晶的星飞游戏关注设置
                    # driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div/div/div/dl[2]/dt/p/a").click()
                    # 关闭弹出的选择分组弹窗。
                    driver.find_element_by_xpath("/html/body/div[6]/div[3]/a").click()
                    # 关闭搭讪窗口
                    driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/a").click()
                    # 切换frame，换一个人选继续操作。
                    close_frame()
                    numFrameButtons = numFrameButtons - 1
                else:
                    driver.find_element_by_link_text("沟通记录").click()
            else:
                # print("已经关注了")
                close_frame()
                numFrameButtons = numFrameButtons - 1
        else:
            driver.close()
            driver.switch_to.window(driver.window_handles[1])
    # 判断是否还可以下一页
    def if_next_page():
        try:
            # driver.find_element_by_class_name("last disabled")
            driver.find_element_by_css_selector("html body#findresume-result div.wrap.resume-search div.result-list table.table-list tfoot tr td.text-right div.pagerbar a.last.disabled")
            return False
        except:
            return True

    #     开始干活啦
    pick_all()
    look_all()
    page_three()
    while if_next_page():
        # print("循环了一次，进入正确判断")
        # 页数很多的情况
        # driver.find_element_by_xpath("/html/body/div[1]/div/table/tfoot/tr/td[2]/div/a[8]").click()
        # 页数很少的情况
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tfoot/tr/td[2]/div/a[6]").click()
        pick_all()
        look_all()
        page_three()
    else:
        # print("**   没有下一页啦，打完啦  **")
        driver.close()
        if(shutdown_num == 1):
            _close_computer()


win2 = tka.Tk()
win1.geometry('600x300+200+200')
win2.title("登陆成功后点击一下下面的按钮就OK，再别乱动鼠标")
button = tka.Button(win2, text = "我是按钮，登陆账号完成后点我一下",command = _login)
button.pack()
win2.mainloop()







