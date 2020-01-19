from datetime import datetime

menu ='''
**************************
欢迎使用【学生管理系统】
    1.显示所有学生信息
    2.新建学生信息
    3.查询学生信息
    4.修改学生信息
    5.删除学生信息
    6.退出系统
***************************

'''

#模拟的学生数据
dates=[
    {
        'name':'james',
        'sex':'男',
        'birthday':'20000101'
    },
    {
        'name':'kobe',
        'sex':'男',
        'birthday':'19961111'
    },
    {
        'name':'yao',
        'sex':'男',
        'birthday':'20030303'
    }
]

#学生类
class Student:
    def __init__(self,name,sex,birthday):
        self.name = name
        self.sex = sex
        self.birthday=birthday

    def get_age(self):
        age = datetime.now().year-int(self.birthday[:4])
        return age
        # return  datetime.now().year-int(self.birthday[:4])


class System:
    def __init__(self,name):
        self.name=name
        self.dates=[]

    def load_date(self):
        for date in dates:
            student=Student(date['name'],date['sex'],date['birthday'])
            self.dates.append(student)

    def run(self):
        self.load_date()
        while True:
            op=input('请选择操作:')
            if op == '1':
                self.show_all()
            elif op=='2':
                self.create_student()
            elif op =='3':
                self.find_student()

    def show_menu(self):
        print(menu)

    def format_show(self,list):
        for index,student in enumerate(list):
            print(f'序号：{index+1}',end='\t')
            print(f'姓名：{student.name}',end='\t')
            print(f'性别:{student.sex:2}',end='\t')
            print(f'生日：{student.birthday}', end='\t')
            print(f'年龄：{student.get_age()}', end='\t')
            print('\n')

    def show_all(self):
        self.format_show(self.dates)

    def input_name(self):
        while True:
            name=input('请输入姓名：').strip()
            if name:
                return name
            else:
                continue
    def choose_sex(self):
        sex=input('请选择性别：1.男|2.女').strip()
        if sex=='1':
            return  '男'
        elif sex=='2':
            return '女'
        else:
            return '未知'

    def find_by_name(self):
        name=self.input_name()
        find_list = []
        for student in self.dates:
            if name.lower() in student.name.lower():
                find_list.append(student)
                self.format_show(find_list)
        if find_list:
            return  find_list
        else:
            print('未找到该学生')

    def create_student(self):
        name=self.input_name()
        sex=self.choose_sex()
        birthday=input('请输入生日：')
        student=Student(name,sex,birthday)
        self.dates.append(student)

    def find_student(self):
        find_list=self.find_by_name()
        self.format_show(find_list)

    def modify_student(self):





if __name__ == '__main__':
    system = System('福')
    system.show_menu()
    system.run()