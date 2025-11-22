问题1 driver:host不生效,
报错1 failed to create network redis_redis_network: Error response from daemon: only one instance of "host" network is allowed
告警2  redis Published ports are discarded when using host network mode
 https://stackoverflow.com/questions/63777655/docker-error-only-one-instance-of-host-network-is-allowed

 问题2 挂载redis.conf配置文件未生效
 https://stackoverflow.com/questions/30547274/redis-in-docker-compose-any-way-to-specify-a-redis-conf-file
 需要指定文件 command: redis-server /usr/local/etc/redis/redis.conf
 建议先编译dockerfile,参考https://registry.hub.docker.com/_/redis/
 且volumes挂载的是目录,不能指定具体配置文件,可能docker-compose的语法不一样

 问题3,redis配置错误 docker-compose启动redis报错 redis-1 exited with code 0
 redis.conf 中daemonize=yes，后台模式会导致docker认为无任务可做而退出,从而导致redis无法启动,需要设置,daemonize=no。
 https://blog.csdn.net/qq_42837385/article/details/125932945

 问题4,redis配置错误  使用docker-compose启动redis后,无法远程访问
 检查redis配置是否绑定了127.0.0.1

命令
cd /home/ubuntu/code/compose/redis/
sudo docker-compose up -d
sudo docker-compose down
sudo docker-compose exec redis bash
cat /usr/local/etc/redis/redis.conf
redis-cli -h 192.168.190.2
auth your_password
查看有哪些数据卷
sudo docker volume ls
查看数据卷具体映射在服务器路径
sudo docker volume inspect redis_redis_vol
查看docker-compose启动的容器的状态

docker run --name my-redis -d -p 0.0.0.0:6379:6379 redis:latest

docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:lts
