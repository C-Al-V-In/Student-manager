base_dir = './files/'  # 设置地址可以方便修改


def read_txt(file_name):
    try:
        with open(base_dir + file_name + '.txt', 'r', encoding='utf8') as file:
            return file.read()
    except FileNotFoundError:
        print('文件未找到。')


def read_json(file_name, default_data={}):
    try:
        with open(base_dir + file_name + '.json', 'r', encoding='utf8') as file:
            import json
            return json.load(file)
    except FileNotFoundError:
        print('文件未找到。')
        return default_data  # 文件未找到就默认以空字典写入


def write_json(file_name, data):
    with open(base_dir + file_name + '.json', 'w', encoding='utf8') as file:
        import json
        json.dump(data, file)
