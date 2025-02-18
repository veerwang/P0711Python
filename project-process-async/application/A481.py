
import json
import os
import requests
import time

url = 'http://192.168.1.100:7125/printer/gcode/script'

def send_ReagentPBST():
    response = requests.post(url, json={'script': 'ReagentPBST'})
    print(response.status_code)
    print(response.json())
    time.sleep(5)

def send_gcode_commandsxyz():
    gcode_commandsxyz = ['G90', 'G1 X152 F7800', 'G4 P1000', 'G1 Y116 F7800', 'G4 P1000']
    for command in gcode_commandsxyz:
        response = requests.post(url, json={'script': command})
        print(response.status_code)
        print(response.json())
        time.sleep(5)

def send_wells():
    response = requests.post(url, json={'script': 'wells'})
    print(response.status_code)
    print(response.json())
    time.sleep(5)

def send_WashHead():
    response = requests.post(url, json={'script': 'WashHead'})
    print(response.status_code)
    print(response.json())
    time.sleep(5)

def send_gcode_commands(gcode_commands):
    for command in gcode_commands:
        response = requests.post(url, json={'script': command})
        print(response.status_code)
        print(response.json())
        time.sleep(5)

def send_wasted():
    response = requests.post(url, json={'script': 'wasted'})
    print(response.status_code)
    print(response.json())
    time.sleep(5)

def send_all_commands(gcode_commands):
    send_ReagentPBST()
    send_gcode_commandsxyz()
    send_wells()
    send_WashHead()
    send_gcode_commands(gcode_commands)
    send_wasted()

if __name__ == '__main__':
    # 获取当前文件的上级目录
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 构造JSON文件的路径
    json_file_path = os.path.join(parent_dir, 'inputs.json')

    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # 获取当前文件的文件名（不包括扩展名）
    filename = os.path.splitext(os.path.basename(__file__))[0]

    # 从JSON数据中获取与文件名对应的数据
    user_inputs = data.get(filename)

    if user_inputs is not None and len(user_inputs) >= 4:
        command1 = f'G4 P{user_inputs[0]}'
        command2 = f'G4 P{user_inputs[1]}'
        command3 = f'G4 P{user_inputs[2]}'
        command4 = f'G4 P{user_inputs[3]}'

        gcode_commands = [command1,
                          'ReagentPBST',
                          'ReagentPBST',
                          'ReagentPBST',
                          'ReagentPBST',
                          'ReagentPBST',
                          'ReagentPBST',
                          command2,
                          'Mix',
                          'ReagentM',
                          'ReagentM',
                          command3,
                          'ReagentPBST',
                          'ReagentPBST',
                          command4]
        send_all_commands(gcode_commands)
