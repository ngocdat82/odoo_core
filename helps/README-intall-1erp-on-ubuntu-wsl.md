# CÀI ĐẶT MÁY ẢO WSL UBUNTU 22.04

## 1. Cài đặt nâng cấp win11 bảng home sang bảng enterprise

Để có một hệ điều hành Ubuntu trên Win chạy nhẹ nhàng như máy thật, không tốn dung lượng, tài nguyên CPU và RAM như các máy ảo. Môi trường WSL 2 là trình (Window Subsystem for Linux 2) của Window cung cấp môi trường cài đặt nhẹ nhàng, cho ta ngay máy ảo Ubuntu như thật chạy trên cùng nền tảng window. 

Điều kiện:
Nâng cấp window home lên bản profestional (Lâm có file cài) 
Phải mở tính năng máy ảo trên window
Cài đặt wsl 2
Cập nhập pack fix lỗi wsl 
Vào kho ứng dụng của window lấy bản linux ưng ý (như ubuntu)

Kết quả sử dụng lệnh PS > wsl --list --verbose 
 NAME                   STATE           VERSION
* Ubuntu-22.04           Running         2

Tài liệu tham khảo"

https://xuanthulab.net/gioi-thieu-va-cai-dat-wsl-tren-windows.html

https://www.c-sharpcorner.com/article/how-to-install-windows-subsystem-for-linux-wsl2-on-windows-11/


## 2. Cài đặt csdl postgres trên window, lưu ý nhớ mật khẩu quản trị để tạo user có quyền CREATEDB là có thể sử dụng được rồi, không cần quyền superuser
- Cài đặt cơ sở dữ liệu Postgres lên môi trường thật, hoặc một docker sao cho có user để tương tác csdl
- Cài đặt cơ sở dữ liệu postgres trên một docker hoặc máy thật, sao cho có thể kết nối được user csdl tạo csdl, update, insert, delete, ...
- Chỉnh sửa file pg_hba.conf trên máy chủ csdl postgres sao cho user admin csdl có thể tạo được user sử dụng trong odoo

```sh

$ psql -U postgres -d postgres

postgres=# \du
postgres=# \l

# Tạo user database cho erp15 
postgres # CREATE USER erp15 WITH PASSWORD '1234';


postgres # ALTER USER erp15 WITH CREATEDB;
postgres # ALTER USER erp15 WITH LOGIN;

# Hoặc đổi mật khẩu mặt định bằng lệnh
postgres # ALTER USER erp15 WITH PASSWORD '1234';

# Tạo csdl nếu cần nếu không thì không cần
postgres # CREATE DATABASE erp15 WITH ENCODING 'UTF8';

# Xem file config của postgres ở đâu sửa
postgres # show config_file;


# Từ máy client có thể kết nối đến csdl thông qua lệnh
$ psql -h 10.24.191.36 -p 5432 -U erp15 -d postgres -W
# md5bbff928afd1d9de3d8735e221147d1d4
# Xem cấu hình file khai bên dưới

```

### Xem file đã khai C:\Program Files\PostgreSQL\14\data\pg_hba.conf

```conf

# TYPE  DATABASE        USER            ADDRESS                 METHOD
# "local" is for Unix domain socket connections only
local   all             all                                     trust

# IPv4 local connections:
host    all             erp15           10.24.191.0/24          md5


```

```sh
# Từ máy client có thể kết nối đến csdl thông qua lệnh
$ psql -h 10.24.191.36 -p 5432 -U erp15 -d postgres -W
# md5bbff928afd1d9de3d8735e221147d1d4
# Xem cấu hình file khai bên dưới

```

## 2. Cài đặt Postgresql client lên máy chủ ubuntu để có thể kết nối được với csdl ở trên
```sh

$ sudo apt install postgresql-client

$ psql -h 10.24.191.36 -d odoo15 -U postgres -W

```

## 2. Cài đặt các môi trường phát triển của Odoo trên ubuntu

```sh

# 1. Tạo user erp trên hệ điều hành từ root

# 2. Gán user cho quyền sudo trên ubuntu

# 3. Chuyển sang user erp để thao tác

# 4. Cài đặt các thành phần của odoo trên môi trường ubuntu
$ sudo apt update -y && apt upgrade -y

$ sudo add-apt-repository ppa:deadsnakes/ppa

$ sudo apt install python3.10

$ python3 --version

$ sudo apt install python3-pip  wget python3-dev python3-venv python3-wheel libxml2-dev libpq-dev libjpeg8-dev liblcms2-dev libxslt1-dev zlib1g-dev libsasl2-dev libldap2-dev build-essential git libssl-dev libffi-dev libmysqlclient-dev libjpeg-dev libblas-dev libatlas-base-dev -y

$ sudo apt-get install wkhtmltopdf -y

$ wkhtmltopdf --version

```

## 3. KHO GIT ĐỂ LẤY VỀ CÀI ĐẶT BẢN RELEASE

```sh
# cd /home/erp
# 

# Từ gitlab
$ git clone https://gitlab.mobifone.vn/trung-tam-cntt/phong-ptpm3/erp-sme/mbf-odoo.git --depth 5 --branch 15/mbf/release/1.0 mbf-1erp-15

# Từ github
$ git clone https://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@github.com/mbf-odoo/mbf-odoo.git --depth 5 --branch 15/mbf/release/1.0 mbf-1erp-15

# cd đến thư mục của mã nguồn để chạy
$ cd /home/erp/mbf-1erp-15

```


## 4. KHO GIT ĐỂ LẤY VỀ CÀI ĐẶT BẢN RELEASE

```sh
# cd /home/erp
# 

# Từ gitlab
$ git clone  https://gitlab.mobifone.vn/trung-tam-cntt/phong-ptpm3/erp-sme/mbf-15-addons.git --depth 5 --branch 15/mbf/release/1.0 mbf-15-addons

# Từ github
$ git clone https://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@github.com/mbf-odoo/mbf-15-addons.git --depth 5 --branch 15/mbf/release/1.0 mbf-15-addons

# cd đến thư mục của mã nguồn để chạy
$ cd /home/erp/mbf-1erp-15

```

## 5. TẠO MÔI TRƯỜNG ẢO CỦA PYTHON để cài đặt các thành phần của Odoo yêu cầu

```sh

$ cd /home/erp/mbf-1erp-15

$ python3 -m venv mbf-odoo15-venv

$ source mbf-odoo15-venv/bin/activate

$ pip3 install wheel
$ pip3 install -r requirements.txt


# Thoát môi trường ảo nếu cần
$ deactivate

```

## 6. Tạo file cấu hình để chạy môi trường phát triển

```conf

[options]
[options]
# thay doi duong dan goc
addons_path = /opt/1erp/mbf-1erp-15/addons, /opt/1erp/mbf-1erp-15/odoo/addons, /opt/1erp/mbf-stdv-15-addons

# Thay doi duong dan luu du lieu
data_dir = /opt/1erp/datastores

# Thay doi duong dan luu logfile
logfile = /opt/1erp/logs/erp15-sotaydangvien

# Mat khau nay co the thay the tren trang admin de ma hoa csdl
admin_passwd = u
# 

# Từ máy ảo truy cập được database thông qua lệnh
# psql

db_host = ip
db_maxconn = 64
db_name = False
db_port = 5432
db_sslmode = prefer
db_template = template0
db_user = u
db_password = p

# Chi loc csdl co domain
# dbfilter = ^%h$
# set proxy_mode = True for multi database
proxy_mode = True

# cho phep hoac khong liet ke /web/database/manager
list_db = True
log_db = False
# warning , debug
# log_db_level = warning
# :INFO , :DEBUG -- Xem toan bo log xu ly cua tat ca cac module cua odoo
# log_handler = :INFO
# info, debug
log_level = info


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


xmlrpc = True
xmlrpc_port = 8069
longpolling_port = 8072

```

## 6. Chạy dịch vụ bên trong máy ảo

```sh

$ cd /home/erp/mbf-1erp-15

$ source mbf-odoo15-venv/bin/activate

$ ./odoo-bin -c /mnt/c/1ERP/cfg/1erp.conf -d 1erp-1 -i base

```


## 7. Chạy dịch vụ bên trong máy ảo với source từ máy ngoài

```sh
# Chạy trên source của release
# $ cd /home/erp/mbf-1erp-15
$ cd mnt/c/1ERP/1erp-src/mbf-1erp-15

# Chạy trên source của máy gốc, kích hoạt môi trường ảo đã cài cho odoo trong máy ảo
$ source /home/erp/mbf-1erp-15/mbf-odoo15-venv/bin/activate

# Nếu chạy ở môi trường ảo ở trong máy ảo mà source ở bên ngoài thì phải gọi python3 ở trong môi trường ảo
$ python3 ./odoo-bin -c /mnt/c/1ERP/cfg/1erp.conf

```

## 8. Mở port proxy từ máy ảo wsl đến cho bên trong mạng LAN có thể truy cập được

- Trên máy ảo wsl (ubuntu) gõ lệnh:
```sh
$ ip addr | grep eth0
#  eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
#  inet 172.20.131.144/20 brd 172.20.143.255 scope global eth0
```

- Trên máy host (máy window) chạy power shell với quyền admin và chạy lệnh:
```sh
> netsh interface portproxy add v4tov4 listenport=8069 listenaddress=0.0.0.0 connectport=8069 connectaddress=172.20.131.144

> netsh interface portproxy add v4tov4 listenport=8072 listenaddress=0.0.0.0 connectport=8072 connectaddress=172.20.131.144
```

- Bây giờ đứng ở bất kỳ máy nào trong mạng LAN có thể truy cập được port 8069 và 8072 trên máy ảo wsl (linux) - tức là truy cập web trong máy ảo là được.