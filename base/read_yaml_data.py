import yaml,os

#读取yaml文件
def read_yaml_data(file_name):
    with open("./data" + os.sep + file_name , "r" , encoding = "utf-8") as f:
        yaml_data = yaml.load(f)
        return yaml_data

