# HUONG DAN CAI DAT CSDL POSTGRES tren Ubuntu


## 1. Cai dat csdl postgres va tao superuser

```sh
$ sudo apt update

$ sudo apt install postgresql postgresql-contrib

$ sudo systemctl start postgresql.service

$ sudo -i -u postgres

# Tao mot super user trong postgres
$ createuser --interactive
# nhap user name moi la erp15
# new role supperuser y

# Tao csdl 
$ createdb erp15

# exit ra user goc
# Tao user
$ sudo adduser erp15

# Doi mat khau user
$ sudo passwd erp15

# Chuyen user
$ sudo -i -u erp15

# Ket noi csdl
$ psql

# Dau nhac csdl
=# \du


# Tạo user database cho erp15 
postgres # CREATE USER erp15 WITH PASSWORD '1234';


postgres # ALTER USER erp15 WITH CREATEDB;
postgres # ALTER USER erp15 WITH LOGIN;

# Hoặc đổi mật khẩu mặt định bằng lệnh
postgres # ALTER USER erp15 WITH PASSWORD '1234';

# Tạo csdl nếu cần nếu không thì không cần
postgres # CREATE DATABASE erp15 WITH ENCODING 'UTF8';


# Xem file cau hinh da luu
=# show config_file;
/etc/postgresql/12/main/pg_hba.conf


```


## Khai bao cau hinh FW cua postgres cho phep cac user, lop mang, may tinh truy cap vao csdl
```conf
# TYPE  DATABASE        USER            ADDRESS                 METHOD
# "local" is for Unix domain socket connections only
local   all             all                                     trust
# IPv4 local connections:
host    all             erp15           10.24.191.0/24          md5
```

## Remove PostgreSQL
```sh

$ sudo apt remove postgresql postgresql-contrib

```


## 2. Cài đặt Postgresql client lên máy chủ ubuntu để có thể kết nối được với csdl ở trên
```sh

$ sudo apt install postgresql-client

$ psql -h 10.38.21.248 -p 5432 -d erp15 -U erp15 -W

```
