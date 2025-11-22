# recruitment
- 启动Docker容器:
  - cd /home/jason/recruitment/
  - docker run --rm -p 39979:39979 -v "$(pwd)":/data/recruitment --env server_params="--settings=settings.local" xiaopawnye/recruitment-base:v1`

