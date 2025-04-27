import os
import time
import hashlib
import subprocess

WORH_PATH = "/app"
CONFIG_PATH = WORH_PATH + '/src/config/config.json'
CRONTAB_PATH = '/etc/cron.d/bili_monitor'
GENERATE_CRONTAB_SCRIPT = WORH_PATH + '/src/generate_crontab.py'
TIME_CHECK = 30

def get_file_hash(file_path):
    """获取文件的哈希值"""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def regenerate_crontab():
    """重新生成 crontab 文件"""
    subprocess.run(['python3', GENERATE_CRONTAB_SCRIPT], check=True)
    print("Crontab 文件已重新生成")

def set_crontab():
    subprocess.run(['crontab', CRONTAB_PATH], check=True)
    print("添加定时任务")

def monitor_config():
    """监控 config.json 文件的变化"""
    last_hash = get_file_hash(CONFIG_PATH)
    print(f"初始哈希值: {last_hash}")

    while True:
        time.sleep(TIME_CHECK)  # 每 TIME_CHECK 秒检查一次
        current_hash = get_file_hash(CONFIG_PATH)
        if current_hash != last_hash:
            print(f"检测到 config.json 文件变化，重新生成 crontab 文件")
            regenerate_crontab()
            set_crontab()
            last_hash = current_hash

if __name__ == "__main__":
    monitor_config()