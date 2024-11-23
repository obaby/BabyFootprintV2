# 使用官方Python运行时作为父镜像
FROM python:3.8.18-slim

# 设置工作目录
WORKDIR /app

# 将当前目录内容复制到位于/app中的容器中
COPY . /app


# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.pip -i https://pypi.tuna.tsinghua.edu.cn/simple

# 暴露端口8000，与Django的默认运行端口一致
EXPOSE 10086

# 定义环境变量
ENV NAME=Django

# 在容器启动时运行Django的manage.py命令
CMD ["python", "manage.py", "runserver", "0.0.0.0:10086"]