def add_stu_info(all_info):
    while True:
        name=input('请输入学生姓名：')
        if not name:
            break
        age=int(input('请输入学生年龄：'))
        score=int(input('请输入学生成绩：'))
        all_info+=[{'name':name,'age':age,'score':score}]
    return all_info

def show_stu_info(all_info):
    for i in all_info:
        #print(i)
        print('|%s|%s|%s|' % (i['name'].center(20),str(i['age']).center(6),str(i['score']).center(6)))

def chang_stu_info(all_info):
    flag=0
    name=input('请输入要修改信息的学生姓名：')
    for j in all_info:    
        if j['name']==name:
            flag=1
            print('****系统找到该学生的信息****')
            age=int(input('请输入学生年龄：'))
            score=int(input('请输入学生成绩：'))
            j['age']=age
            j['score']=score
            print('修改后的学生信息是：','|%s|%s|%s|' % (j['name'].center(20),str(j['age']).center(6),str(j['score']).center(6)))
    
    if flag==0:
        print('系统没有',name,'的学生信息,无法修改')

def del_stu_info(all_info):
    flag=0
    count=0
    name=input('请输入学生姓名：')
    for k in all_info:    
        if k['name']==name:
            del all_info[count]
            flag=1
            print('学生',name,'的信息已经删除')
        count+=1
    if flag==0:           
        print('系统没有',name,'的学生信息，不需要删除')
