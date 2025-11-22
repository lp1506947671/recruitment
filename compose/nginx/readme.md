### 1.操作步骤

- 1.删除所有没有被任何容器引用的镜像
  - docker image prune -a
- 2.构建镜像
  - docker build --network=host -t xiaopawnye/nginx:v2 nginx/
- 3.启动容器
  - docker run --rm --network=host  -p 80:80 -p 443:443 -v /home/jason/recruitment/compose/nginx/log:/var/log/nginx -v /home/jason/recruitment/compose/nginx/nginx.conf:/etc/nginx/conf.d/nginx.conf -v /home/jason/recruitment/compose/nginx/ssl:/usr/share/nginx/ssl xiaopawnye/nginx:v2


