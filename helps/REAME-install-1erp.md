# HƯỚNG DẪN CÀI ĐẶT CÁC THÀNH PHẦN ĐỂ CHẠY 1ERP 15

## 1. Update system:
```sh

sudo apt update -y && apt upgrade -y

```

## 2. Install python3 and others

```sh

$ sudo apt install python3-pip  wget python3-dev python3-venv python3-wheel libxml2-dev libpq-dev libjpeg8-dev liblcms2-dev libxslt1-dev zlib1g-dev libsasl2-dev libldap2-dev build-essential git libssl-dev libffi-dev libmysqlclient-dev libjpeg-dev libblas-dev libatlas-base-dev -y

```

```sh

sudo apt-get install wkhtmltopdf -y

wkhtmltopdf --version

#view version 0.12.6 or 0.16.6 is ok

```

## 3. Tạo một môi trường ảo độc lập để cài đặt các thành phần chạy cho 1erp

```sh

cd /opt/1erp

python3 -m venv mbf-1erp-15-venv

source mbf-1erp-15-venv/bin/activate

pip3 install wheel
pip3 install -r /opt/1erp/mbf-1erp-15/requirements.txt

deactivate

```


## 4. Tạo file cấu hình để chạy môi trường phát triển tại /opt/1erp/cfg/1erp-sotaydangvien.conf

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

## 5. Để chạy chương trình của 1erp thì dùng lệnh

```sh
# Chạy trên source của release
# $ cd /home/erp/mbf-1erp-15
$ cd /opt/1erp/mbf-1erp-15

# Chạy trên source của máy gốc, kích hoạt môi trường ảo đã cài cho odoo trong máy ảo
$ source /opt/1erp/mbf-1erp15-venv/bin/activate

# Nếu chạy ở môi trường ảo ở trong máy ảo mà source ở bên ngoài thì phải gọi python3 ở trong môi trường ảo
$ python3 ./odoo-bin -c /opt/1erp/cfg/1erp-sotaydangvien.conf

# Hoac chay truc tiep bang duong dan tuyet doi
$ /opt/1erp/mbf-1erp15-venv/bin/python3 /opt/1erp/mbf-1erp-15/odoo-bin -c /opt/1erp/cfg/1erp-sotaydangvien.conf

# Chay tren may 249
$ /opt/1erp/mbf-1erp-15-venv/bin/python3 /opt/1erp/stdv/mbf-1erp-15/odoo-bin -c /opt/1erp/stdv/cfg/1erp-sotaydangvien.conf

```

## 6. TẠO SERVICE ĐỂ CHẠY DỊCH VỤ TRONG UBUNTU


```sh

$ sudo nano /etc/systemd/system/stdv15.service

```

## 7. Edit content for service

```conf

[Unit]
Description=1Erp 15 of ERP for SME
Requires=postgresql.service
After=network.target postgresql.service

[Service]
Type=simple
SyslogIdentifier=1erp15
PermissionsStartOnly=true
User=erp15
Group=erp15
# do chdir before running the service
WorkingDirectory=/opt/1erp/mbf-1erp-15/
ExecStart=/opt/1erp/mbf-1erp15-venv/bin/python3 ./odoo-bin -c /opt/1erp/cfg/1erp-sotaydangvien.conf
StandardOutput=journal+console
# limit CPU and RAM quota for our service
#CPUAccounting=true
#CPUQuota=30%
#MemoryAccounting=true
#MemoryLimit=500M

[Install]
WantedBy=multi-user.target

```


# 16. Reload daemon systemd to update command

```sh

sudo systemctl daemon-reload

```

# 17. Enable and start odoo

```sh

sudo systemctl enable --now 1erp15

sudo systemctl status 1erp15

sudo systemctl start 1erp15

sudo systemctl restart 1erp15

sudo systemctl stop 1erp15

# Disable service in Odoo
sudo systemctl stop 1erp15
sudo systemctl disable 1erp15
sudo systemctl daemon-reload

```