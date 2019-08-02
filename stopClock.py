import time
import tkinter
import threading

#定义主要显示的内容
def counter_label(label):
    def count():
        global counter
        counter -= 1
        label.config(text='眺望远方{}秒'.format(counter))
        label.after(1000,count)
    count()

def timeover():
    root = tkinter.Tk()
    
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.focus_set()  # <-- move focus to this widget
    #是否使用esc退出
    #root.bind("<Escape>", lambda e: e.widget.quit())
    
    root.title('Sleeping')
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root['width']=width
    root['height']=height
    root.configure(background='black')
    #不允许改变窗口大小
    root.resizable(False,False)

    #显示倒计时
    lbTime = tkinter.Label(root,fg='red',font=("Helvetica", 50),background='black',justify='right')
    lbTime.place(x=0,y=height/2,width=width)

    #lbTime['text'] = '眺望远方20秒'
    counter_label(lbTime)
    
    #def autoClose():
    #    for i in range(10):
    #        lbTime['text'] = '眺望远方{}秒'.format(20-i)
    #        time.sleep(1)


    #t = threading.Thread(target=autoClose)
    #t.start()
    #设定为20秒后关闭TK窗口
    root.after(20000, lambda: root.destroy()) # Destroy the widget after 30 seconds
    #将窗口设定为前端
    root.wm_attributes('-topmost',1)
    #root.focus_force()

    root.mainloop()

while True:
    counter = 20
    time.sleep(20*60)
    print('running next')
    timeover()
    print('ok')
