#/usr/bin/python
#-*- coding:utf-8 -*-
import getpass
name=raw_input("请输入用户名：")
pwd=getpass.getpass("请输入密码")
if name=="tina" and pwd=="1234":
	print "welcome,tina!"
else:
	print "username or password error!!!"
