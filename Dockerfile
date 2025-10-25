FROM python:3.10-alpine
MAINTAINER xiaopawnye
ENV DJANGO_SETTINGS_MODULE=settings.local
WORKDIR /data/recruitment
COPY ./requirements.txt .
COPY ./start.sh .
COPY ./src .
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories # 替换为apk阿里云镜像
RUN apk add --update --no-cache curl jq py3-configobj py3-pip py3-setuptools python3-dev \
  && apk add --no-cache gcc g++ jpeg-dev zlib-dev libc-dev libressl-dev musl-dev libffi-dev \
  && python -m pip install --upgrade pip \
  && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple \
  && apk del gcc g++ libressl-dev musl-dev libffi-dev python3-dev \
  && apk del curl jq py3-configobj py3-pip py3-setuptools \
  && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
  && echo 'Asia/Shanghai' >/etc/timezone  \
  && rm -rf /var/cache/apk/*
RUN sed -i 's/\r//' /data/recruitment/start.sh
RUN chmod +x ./start.sh
EXPOSE 39979
CMD ["/bin/sh", "/data/recruitment/start.sh"]
