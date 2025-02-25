# HUONG DAN CAI DAT odoo 15 tren centos

- Yêu cầu python3.8 trở lên, và postgresql 9.3 trở lên

-[Xem link] (https://computingforgeeks.com/how-to-install-odoo-centos-rhel-linux/)

-[Xem link] Cài đặt postgres-14 (https://computingforgeeks.com/how-to-install-postgresql-14-centos-rhel-7/)

## 1. Update system và cài đặt python 3.8 trở lên:

```sh

[root@centos7 ~]# yum update -y

[root@centos7 ~]# yum install -y python3
# No chi cai dat version 3.6.8 nen khong hop le
# Phai cai dat phien ban cao hon tu source code


[root@centos7 ~]# yum install gcc openssl-devel bzip2-devel libffi-devel -y

[root@centos7 ~]# curl -O https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tgz

[root@centos7 ~]# tar -xzf Python-3.8.1.tgz

[root@centos7 ~]# cd Python-3.8.1/

[root@centos7 Python-3.8.1]# ./configure --enable-optimizations

[root@centos7 Python-3.8.1]# make altinstall

[root@centos7 Python-3.8.1]# python3.8 --version

```

## 2. Install python3 and others - Cài đặt các module phụ thuộc của python phục vụ cho odoo

```sh

[root@centos7 ~]#  yum install git gcc wget nodejs libxslt-devel bzip2-devel openldap-devel libjpeg-devel freetype-devel

[root@centos7 ~]#  yum install python3-pip  wget python3-dev python3-venv python3-wheel

[root@centos7 ~]#  yum install  libxml2-dev libpq-dev libjpeg8-dev liblcms2-dev libxslt1-dev zlib1g-dev libsasl2-dev libldap2-dev build-essential git libssl-dev libffi-dev libmysqlclient-dev libjpeg-dev libblas-dev libatlas-base-dev

[root@centos7 ~]#  yum groupinstall "Development Tools"
[root@centos7 ~]#  yum install python3-devel postgresql-libs postgresql-devel

[root@centos7 ~]#  yum install wkhtmltopdf


# Khong cai duoc postgres client tren centos
# nen phai cai server database
[root@centos7 ~]#  yum install postgresql-client


```


## 3. Cài đặt máy chủ database postgres 14 tren centos7 

```sh

[root@centos7 ~]# subscription-manager register --auto-attach

[root@centos7 ~]# yum info postgresql-server

# Lay kho
[root@centos7 ~]# sudo yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm

# Xem list co 14
[root@centos7 ~]# yum repolist -y


[root@centos7 ~]# yum -y update 

# Chua can reboot
[root@centos7 ~]# systemctl reboot


[root@centos7 ~]# yum install -y postgresql14-server postgresql14

[root@centos7 ~]# rpm -qi postgresql14-server postgresql14

[root@centos7 ~]# /usr/pgsql-14/bin/postgresql-14-setup initdb

[root@centos7 ~]# systemctl enable --now postgresql-14

[root@centos7 ~]# systemctl status postgresql-14

[root@centos7 ~]# su - postgres

postgres $ psql

postgres=# alter user postgres with password 'Mobifone1ErpEcontract';

postgres=# CREATE USER odoo15 WITH PASSWORD 'Mobifone1ErpEcontract';
postgres=# ALTER USER odoo15 WITH SUPERUSER;
postgres=# ALTER USER odoo15 WITH LOGIN;
postgres=# CREATE DATABASE odoo15 WITH ENCODING 'UTF8';

postgres=# show config_file;
# /var/lib/pgsql/14/data/postgresql.conf

# thoat khoi
postgres=# \q

postgres $ exit

```

## 4. Instal virtual environment python3.8 - Cài đặt môi trường ảo của python

```sh

[root@centos7 ~]# cd /opt/PYTHON/src/mbf-1erp

[root@centos7 ~]#  python3.8 -m venv mbf-odoo15-venv

[root@centos7 ~]# source mbf-odoo15-venv/bin/activate

[root@centos7 ~]#  pip3 install --upgrade pip3

[root@centos7 ~]#  pip3 install wheel
[root@centos7 ~]#  pip3 install -r requirements.txt

# Có 2 gói bị lỗi cài đặt trên môi trường centos7
# libsass==0.18.0;
# psycopg2==2.8.6;

# Để cài bằng tay từng gói này thì ta tìm kiếm cách cài trên google
# Bang cai dat libsass la 0.22.0
[root@centos7 ~]#  pip3 install libsass

# bi loi version nay
[root@centos7 ~]#  pip3 install psycopg2==2.8.6 

# Co mot cach de cai dat nhu the nay
[root@centos7 ~]#  pip3 install psycopg2-binary===2.8.6
# Hoặc cài kiểu này
[root@centos7 ~]#  pip3 install psycopg2-binary

# cai version nay la 2.9.5
[root@centos7 ~]#   pip install psycopg2


[root@centos7 ~]# deactivate

```

## 5. Tạo user odoo15 để chạy ứng dụng mbf-1erp

```sh

[root@centos7 ~]# useradd -m -d /opt/PYTHON/src/mbf-1erp -U -r -s /bin/bash odoo15
# vao /var/lib/pgsql/data/pg_hba.conf 
# sua lai xac thuc md5 
# restart lai service postgresql
# doi mat khau user odoo15 trong database

# chuyển đổi quyền sở hữu thư mục mã nguồn và các thành phần cho odoo15
[root@centos7 ~]# chown odoo15:odoo15 -Rf /opt/PYTHON/src

[root@centos7 ~]# su - odoo15
 
# Soạn thảo file cấu hình để chạy odoo15
[odoo15-bash]$ nano /opt/PYTHON/src/mbf-1erp/cfg/odoo15.conf

```

## 6. Edit with content for odoo15.conf

```conf

[options]
; Đường dẫn mã nguồn các gói module của ứng dụng 1erp (bao gồm core base, các module addons phiên bản CE, và module addons phát triển)
addons_path = /opt/PYTHON/src/mbf-1erp/addons, /opt/PYTHON/src/mbf-1erp/odoo/addons, /opt/PYTHON/src/mbf-
15-addons
; Mật khẩu đã được mã hóa chỗi cho csdl
admin_passwd = $pbkdf2-sha512$25000$XqtVas35P6e09r53DoGwVg$.52yewj7suoJyN7XHA8bYcE1nJSe6lUqSS6IzSfPG3xJTD
v8xyXrdnTT8udun.cC5I0WoD1H3klljPFlMB4oCQ
; Đường dẫn để chứa dữ liệu filestore, session, của ứng dụng 1erp
data_dir = /opt/PYTHON/src/mbf-1erp/data
; Đường dẫn ghi logfile khi ứng dụng chạy, để kiểm soát các logfile lỗi, debug...
logfile = /opt/PYTHON/src/mbf-1erp/logs

; Khai báo máy chủ cơ sở dữ liệu, user, mật khẩu truy cập cơ sở dữ liệu postgresql từ 9.3 trở lên
db_host = localhost
db_user = odoo15
db_password = Mobifone1ErpEcontract
db_maxconn = 64
db_name = False
db_port = 5432
db_sslmode = prefer
db_template = template0

# port
xmlrpc = True
xmlrpc_port = 8069
longpolling_port = 8072


# Chi loc csdl co domain
dbfilter = ^%h$
# set proxy_mode = True for multi database
proxy_mode = True

# cau hinh may chu dung cho 60 user dong thoi
limit_memory_hard = 1677721600
limit_memory_soft = 629145600
limit_request = 8192
limit_time_cpu = 600
limit_time_real = 1200
max_cron_threads = 1
workers = 8

osv_memory_age_limit = False
osv_memory_count_limit = False

```

## 7. Create service in centos

```sh
# # disable service
# sudo systemctl stop odoo15
# sudo systemctl disable odoo15
# sudo systemctl daemon-reload
# sudo ls -l /lib/systemd/system/
# sudo ls -l /etc/systemd/system/

[root@centos7 ~]# nano /etc/systemd/system/1erp.service

```

## 8. Edit content for service

```conf

[Unit]
Description=Mobifone 1Erp for SME
Requires=postgresql.service
After=network.target postgresql.service

[Service]
Type=simple
SyslogIdentifier=1erp
PermissionsStartOnly=true
User=odoo15
Group=odoo15
# do chdir before running the service
WorkingDirectory=/opt/PYTHON/src/mbf-1erp/
ExecStart=/opt/PYTHON/src/mbf-1erp/mbf-odoo15-venv/bin/python3 ./odoo-bin -c ./cfg/odoo15.conf
StandardOutput=journal+console
# limit CPU and RAM quota for our service
#CPUAccounting=true
#CPUQuota=30%
#MemoryAccounting=true
#MemoryLimit=500M

[Install]
WantedBy=multi-user.target

```

## 9. Reload daemon systemd to update command

```sh

[root@centos7 ~]# systemctl daemon-reload

```

## 10. Khở động dịch vụ 1erp

```sh

[root@centos7 ~]# systemctl enable --now 1erp

[root@centos7 ~]# systemctl status 1erp

[root@centos7 ~]# systemctl start 1erp

[root@centos7 ~]# systemctl restart 1erp

[root@centos7 ~]# systemctl stop 1erp

# Disable service in Odoo
[root@centos7 ~]# systemctl stop 1erp
[root@centos7 ~]# systemctl disable 1erp
[root@centos7 ~]# systemctl daemon-reload

```

## 11. --------------- EXTRA -------------------

### RUN MANUNAL for test and dev

```sh

[root@centos7 ~]# su - odoo15

[odoo15-bash]$ source mbf-odoo15-venv/bin/activate

[odoo15-bash]$ python3 ./odoo-bin -c ./cfg/odoo15.conf -d 1erp -i base

```

### Kiểm tra cơ sở dữ liệu

```sh
[root@centos7 ~]# su - odoo15
[odoo15-bash]$ psql -U odoo15 -d postgres -W

# Xem các user và quyền truy cập
postgres=# \du

# Xem các database đã tạo
postgres=# \l

# Xóa cơ sở dữ liệu rác 
postgres=# drop database "odoo15";
postgres=# drop database "odoo15-2";
postgres=# drop database "odoo15-3";
postgres=# drop database "odoo15-noweb";

# Xem tất cả các bảng trong cơ sở dữ liệu
postgres=# \dt

# Kết nối qua cơ sở dữ liệu khác
postgres=# \c <tên cơ sở dữ liệu khác>

# Thoát ra khỏi cơ sở dữ liệu
postgres=# \q 

```

### Kiểm tra các dịch vụ đang chạy trên máy chủ linux

```sh

[root@centos7 ~]# nginx -t

```

## 12. Go to web http://localhost:8069 for config odoo db and app


## 13. Cấu hình máy chủ nginx để lòi ra cho bên ngoài port 80, 443

```sh

[root@centos7 ~]# cd /etc/nginx/conf.d

[root@centos7 ~]# nano hopdongdientu.mobifone-econtract.vn.conf

```

