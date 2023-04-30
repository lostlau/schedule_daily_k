FROM amd64/python:3.8.16-slim

#RUN apk update

#RUN apk add make automake gcc g++ subversion python3-dev libxslt-dev

COPY . /app

WORKDIR /app

ENV PIP3_INSTALL="pip3 install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com"

RUN $PIP3_INSTALL -r /app/requirements.txt

#COPY ./libmini_racer.dylib /usr/local/lib/python3.8/site-packages/py_mini_racer/libmini_racer.dylib

#CMD ["python", "/app/main.py"]

CMD python -u /app/main.py
