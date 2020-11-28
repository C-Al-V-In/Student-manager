import file_manager
import model

name = ''  # 老师用户名


def add_student():
    x = file_manager.read_json(name, {})
    if not x:
        students = []
        num = 0
    else:
        students = x['all_student']
        num = int(x['num'])

    while True:
        s_name = input('请输入学生姓名：')
        s_age = input('请输入学生年龄：')
        s_gender = input('请输入学生性别：')
        s_tel = input('请输入学生电话号码：')

        num += 1
        # zfill为字符串补齐方法，前面补0
        s_id = 'stu_' + str(num).zfill(4)  # num存在重复问题
        # 创建一个Student对象
        s = model.Student(s_id, s_name, s_age, s_gender, s_tel)

        students.append(s.__dict__)
        data = {'all_student': students, 'num': len(students)}
        file_manager.write_json(name, data)

        choice = input('添加成功!\n继续1\n返回2\n请选择:')
        if choice == '2':
            break


def show_student():
    key = value = ''  # 指定查询类型
    x = input('1.查看全部学生\n2.按姓名查询\n3.按学号查询\n4.返回\n请选择：')
    y = file_manager.read_json(name, {})
    students = y.get('all_student', [])

    if not students:
        print('该教师未添加学员，请添加学员。')
        return

    if x == '1':  # 查看全部学生相当于不指定查询类型
        pass
    elif x == '2':
        value = input('请输入查询学生姓名：')
        key = 'name'
    elif x == '3':
        value = input('请输入查询学生id：')
        key = 's_id'
    else:
        return

    students = filter(lambda s: s.get(key, '') == value, students)
    if not students:
        print('未找到学员。')
        return
    for student in students:
        print('学号{s_id}，姓名{name}，年龄{age}，性别{gender}，电话{tel}'.format(**student))


def modify_student():
    print('服务器维护中……（还没做呢，等我更新了再说。）')
    pass


def del_student():
    key = value = ''
    y = file_manager.read_json(name, {})
    all_students = y.get('all_student', [])

    if not all_students:
        print('该教师未添加学员，请添加学员。')
        return
    num = input('1.按姓名删\n2.按学号删\n3.返回\n请选择：')
    if num == '1':
        key = 'name'
        value = input('请输入要删除学生的姓名')
    elif num == '2':
        key = 's_id'
        value = input('请输入要删除学生的id')
    else:
        return
    students = list(filter(lambda s: s.get(key, '') == value, all_students))  # 值得好好看看
    if not students:
        print('未找到学员。')
        return
    for i, student in enumerate(students):
        print('{x},学号{s_id}，姓名{name}，年龄{age}，性别{gender}，电话{tel}'.format(x=i, **student))

    n = input('请输入要删除的学生标号（0~%d），q—退出：'.format(i))  # i有潜在风险（可能未被定义）
    if not n.isdigit() or not 0 <= int(n) <= i:
        print('输入内容不合法。')
        return
    all_students.remove(students[int(n)])

    y['all_student'] = all_students
    file_manager.write_json(name, y)


def show_manager():
    content = file_manager.read_txt('students_page') % name  # 显示对应老师用户名
    while True:
        print(content)
        operator = input('请选择（1~5）')
        if operator == '1':
            add_student()
        elif operator == '2':
            show_student()
        elif operator == '3':
            modify_student()
        elif operator == '4':
            del_student()
        elif operator == '5':
            break
