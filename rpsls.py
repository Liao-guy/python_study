#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：植产05廖建
日期：2020/4/7
"""

import random
comp_number=random.randrange(0,5,1)


def name_to_number(name):   #将玩家输入转为数
	if name=="石头":
		number=0
	elif name=="史波克":
		number=1
	elif name=="纸":
		number=2
	elif name=="蜥蜴":
		number=3
	elif name=="剪刀":
		number=4
	return number

def number_to_name(number):    #将系统输出数转为名
	if number==0:
		name="石头"
	elif number==1:
		name="史波克"
	elif number==2:
		name="纸"
	elif number==3:
		name="蜥蜴"
	else:
		name="剪刀"
	return name

def rpsls(player_choice):
	if player_choice=="石头" or player_choice=="史波克" or player_choice=="纸" or player_choice=="蜥蜴" or player_choice=="剪刀":
		player_choice_number=name_to_number(player_choice)
		print("您的选择为: "+choice_name)
		print("计算机的选择为: "+number_to_name(comp_number))
		if player_choice_number==0 and (comp_number==3 or comp_number==4):
			print("您赢了")
		elif player_choice_number==1 and (comp_number==0 or comp_number==4):
			print("您赢了")
		elif player_choice_number==2 and (comp_number==0 or comp_number==1):
			print("您赢了")
		elif player_choice_number==3 and (comp_number==1 or comp_number==2):
			print("您赢了")
		elif player_choice_number==4 and (comp_number==2 or comp_number==3):
			print("您赢了")
		elif player_choice_number==comp_number:
			print("您和计算机出的一样呢")
		else:
			print("计算机赢了")
	else:
		print("Error: No Correct Name")


print("欢迎使用RPSLS游戏")
print("请输入您的选择:")
choice_name=input()
print("----------------")
rpsls(choice_name)


