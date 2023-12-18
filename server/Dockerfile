#FROM 指令指定container使用的image檔案，如果電腦內沒有gcc:latest，就會 自動去docker hub下載 gcc:latest
FROM python:3.12.1-slim

#WORKDIR 指令在container內的工作目錄， container會切換至/code 目錄
WORKDIR /code

#COPY 指令將專案根目錄內的檔案複製到container內的HelloWorld目錄內
COPY requirements.txt .

#RUN 指令指定container執行 gcc 將hello.c編輯成HelloWorld執行檔
RUN pip install -r requirements.txt
COPY . .
# EXPOSE 5000
#CMD 指令執行HelloWorld執行檔
# CMD [ "python", "app.py"]
# ENTRYPOINT ["./HelloWorld"]

