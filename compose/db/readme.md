cd /home/ubuntu/code/myproject_docker/compose/mysql
sudo docker-compose up -d
sudo docker-compose exec  mariadb_master bash
mariadb -h 127.0.0.1 -u root -p
mariadb支持哪些环境变量(通过.env文件创建数据库)
ubuntu如何创建代理
报错Error response from daemon: Head "https://registry-1.docker.io/v2/library/mariadb/manifests/latest": Get "https://auth.docker.io/token?scope=repository%3Alibrary%2Fmariadb%3Apull&service=registry.docker.io":
解决方案:https://blog.csdn.net/tjcyjd/article/details/105742086
show databases;
create database onlineshop;
Alter user 'dbuser'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
ALTER USER 'dbuser'@'%' IDENTIFIED BY 'new_password';
初始化脚本未加载
