#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�ֲ��05�ν�
���ڣ�2020/4/7
"""

import random
comp_number=random.randrange(0,5,1)


def name_to_number(name):   #���������תΪ��
	if name=="ʯͷ":
		number=0
	elif name=="ʷ����":
		number=1
	elif name=="ֽ":
		number=2
	elif name=="����":
		number=3
	elif name=="����":
		number=4
	return number

def number_to_name(number):    #��ϵͳ�����תΪ��
	if number==0:
		name="ʯͷ"
	elif number==1:
		name="ʷ����"
	elif number==2:
		name="ֽ"
	elif number==3:
		name="����"
	else:
		name="����"
	return name

def rpsls(player_choice):
	if player_choice=="ʯͷ" or player_choice=="ʷ����" or player_choice=="ֽ" or player_choice=="����" or player_choice=="����":
		player_choice_number=name_to_number(player_choice)
		print("����ѡ��Ϊ: "+choice_name)
		print("�������ѡ��Ϊ: "+number_to_name(comp_number))
		if player_choice_number==0 and (comp_number==3 or comp_number==4):
			print("��Ӯ��")
		elif player_choice_number==1 and (comp_number==0 or comp_number==4):
			print("��Ӯ��")
		elif player_choice_number==2 and (comp_number==0 or comp_number==1):
			print("��Ӯ��")
		elif player_choice_number==3 and (comp_number==1 or comp_number==2):
			print("��Ӯ��")
		elif player_choice_number==4 and (comp_number==2 or comp_number==3):
			print("��Ӯ��")
		elif player_choice_number==comp_number:
			print("���ͼ��������һ����")
		else:
			print("�����Ӯ��")
	else:
		print("Error: No Correct Name")


print("��ӭʹ��RPSLS��Ϸ")
print("����������ѡ��:")
choice_name=input()
print("----------------")
rpsls(choice_name)


