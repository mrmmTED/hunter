import time

wwwWord = "https://www.liepin.com/"

gl_i = 0
max = 1000
def print_time():
    global gl_i
    print(time.localtime())
    gl_i = gl_i+1
    print(">>>>> "+ str(gl_i)+"  <<<<<")
