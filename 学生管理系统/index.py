import file_manager
import model
import student_manager


def register():
    # 读取json文件,如果文件不存在默认是个字典
    data = file_manager.read_json('data')
    while True:
        teacher_name = input('请输入用户名（3~6位）：')
        if not 3 <= len(teacher_name) <= 6:
            print('不符合要求，请重新输入！')
        else:
            break

    while True:
        password = input('请输入密码（6~12位）：')
        if not 6 <= len(password) <= 12:
            print('不符合要求，请重新输入！')
        else:
            break
    # 输入正确后可创建一个对象
    teacher = model.Teacher(data, password)
    # 建议将密码加密保存
    data[teacher_name] = teacher.password
    file_manager.write_json('data', data)


def login():
    # 读取文件，若没有则默认为一字典
    data = file_manager.read_json('data', {})
    teacher_name = input('请输入用户名：')
    if teacher_name not in data.keys():
        print('用户名不存在！')
        return

    password = input('请输入密码：')
    import tools
    if data[teacher_name] == tools.encrypt_password(password):
        print('登录成功')
        student_manager.name = teacher_name
        student_manager.show_manager()
    else:
        print('密码错误，登录失败！')


def start():
    file_manager.base_dir = './files/'  # 可以在此处修改读取地址
    while True:
        operator = input(file_manager.read_txt('welcome') + '\n请选择输入（1-3）：')
        if operator == '1':
            print('登录')
            login()

        elif operator == '2':
            print('注册')
            register()
        elif operator == '3':
            exit(0)
        else:
            print('输入有误！')


if __name__ == '__main__':
    start()
