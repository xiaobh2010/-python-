from menu import *
from stu_info import *
from sorted import *
from file import *

all_info=[]
while True:
    show_menu()
    num=input('请选择：')
    if num=='1':
        all_info=add_stu_info(all_info)        
    elif num=='2':
        show_stu_info(all_info)
    elif num=='3':
        chang_stu_info(all_info)
    elif num=='4':
        del_stu_info(all_info)
    elif num=='5':
        score_high2low(all_info)
    elif num=='6':
        score_low2high(all_info)
    elif num=='7':
        age_high2low(all_info)
    elif num=='8':
        age_low2high(all_info)
    elif num=='9':
        save_file(all_info)
    elif num=='10':
        read_file()
    elif num=='q':    
        break
