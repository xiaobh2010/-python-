"""
学生管理
"""
#存储学生信息name age score id
class StudentModel:
    def __init__(self,name="",age=0,score=0,id=1):
        self.name=name
        self.age=age
        self.score=score
        self.id=id


class StudentController:
    #公用的变量--类变量
    stu_id=1

    def __init__(self):
        self.__stu_list=[]

    @classmethod
    def __generate_id(cls,stu):
        stu.id=cls.stu_id
        #每插入一个学生增加1
        cls.stu_id+=1

    def insert_student(self):
        name=input('name:')
        age=int(input('age:'))
        score=int(input('score:'))
        id=int(input('id:'))
        #得到一个学生
        stu=StudentModel(name=name,age=age,score=score,id=id)
        StudentController.__generate_id(stu)
        #添加学生
        self.__stu_list.append(stu)
        print(self.__stu_list)
        self.show_student()

    def show_student(self):
        for item in self.__stu_list:
            print('ID:%d-name:%s-age:%d-score:%d'%(item.id,item.name,item.age,item.score))

    def delete_student(self):
        name = input('delete name:')
        for item in self.__stu_list:
            if item.name==name:
                self.__stu_list.remove(item)
                print('delete success')
                break
        self.show_student()

    def change_student(self):
        #获取索引 lst.index('xxx')
        name=input('change name:')
        for item in self.__stu_list:
            if item.name==name:
                score=int(input('change score:'))
                item.score=score

        self.show_student()

    def sort_student(self):
        for i in range(len(self.__stu_list)-1):
            for j in range(len(self.__stu_list)-i-1):
                if self.__stu_list[j].score>self.__stu_list[j+1].score:
                    self.__stu_list[j],self.__stu_list[j+1]=self.__stu_list[j+1],self.__stu_list[j]

        self.show_student()

class StudentView:
    def __init__(self):
        self.controller=StudentController()

    # 私有方法
    def __display_menu(self):
        print("""
        1) 添加学生信息
        2) 显示学生信息
        3) 删除学生信息
        4) 修改学生成绩
        5) 学生成绩升序排序 
        """)

    def __select_menu(self):
        cmd=input('请输入选项:')
        if cmd == '1':
            self.controller.insert_student()

        elif cmd == '2':
            self.controller.show_student()
        elif cmd == '3':
            self.controller.delete_student()
        elif cmd == '4':
            self.controller.change_student()
        elif cmd == '5':
            self.controller.sort_student()
        else:
            print('请输入正确选项')


    def main(self):
        while True:
            self.__display_menu()
            #选择功能
            self.__select_menu()



stu=StudentView()
stu.main()
