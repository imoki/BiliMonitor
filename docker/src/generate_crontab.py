import json
import os

try:
    # 读取 config.json 文件
    WORK_PATH = "/app"
    config_path = WORK_PATH + '/src/config/config.json'
    with open(config_path, 'r', encoding='utf-8') as file:
        config = json.load(file)

    # 获取 crons 部分
    crons = config.get('crons', [])

    # 生成 crontab 文件内容
    crontab_content = []
    for cron in crons:
        # name = cron.get('name')
        cron_time = cron.get('cron')
        type_ = cron.get('type')
        # notes = cron.get('notes')

        # 假设 type 为 0 时执行任务
        if type_ == 0:
            # 解析 cron 时间字符串，假设格式为 "HH:MM"
            hour, minute = map(int, cron_time.split(':'))
            # 构建 crontab 行
            crontab_line = f"{minute} {hour} * * * /usr/local/bin/python {WORK_PATH}/src/main.py >> {WORK_PATH}/src/app.log 2>&1"
            crontab_content.append(crontab_line)

    # 写入 crontab 文件，文件末尾需有换行符
    crontab_file_path = '/etc/cron.d/bili_monitor'
    with open(crontab_file_path, 'w', encoding='utf-8') as crontab_file:
        crontab_file.write('\n'.join(crontab_content) + '\n')

    # 给 crontab 文件执行权限
    os.chmod(crontab_file_path, 0o644)

    print("Crontab 文件已生成并加载")
except Exception as e:
    print("生成 crontab 文件时出错，请检查 config.json 文件格式是否正确")
    print(f"发生错误：{e}")