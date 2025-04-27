FROM python:3.9-slim
 
WORKDIR /app
 
COPY . /app

RUN apt-get update && apt-get install -y cron && apt-get install -y vim

RUN pip install --no-cache-dir -r requirements.txt  -i https://mirrors.aliyun.com/pypi/simple/

RUN touch /app/src/app.log
RUN mkdir -p /app/src/config
RUN mkdir -p /app/src/video

RUN python /app/src/generate_crontab.py

CMD ["sh", "-c", "cron -f & python /app/src/monitor_config.py"]