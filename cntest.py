#!/usr/local/bin/python 
#--'-coding:utf-8-'--
from Tkinter import * 
import sys 
#tk useinputmethods 1 

def die(event): 
	sss=entry.get() 
	sss1=sss.encode("eucgb2312_cn") 
	print sss1 
	sys.exit(0) 

root = Tk() 
print root.tk.call("encoding", "names") 
button = Button(root) 
text_bu="Button °´Å¥" 
uni_bu=unicode("Button °´Å¥","eucgb2312_cn")
button["text"] = uni_bu 
button.bind("<Button>",die) 
button.pack() 

root.tk.call("tk", "useinputmethods", "1") 
entry = Entry(root) 
entry.insert(0,uni_bu) 
entry.pack() 

root.mainloop() 