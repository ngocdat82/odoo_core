# 1. Update system:
```sh

sudo apt update -y && apt upgrade -y

```

# 2. Install python3 and others

```sh

$ sudo apt install python3-pip  wget python3-dev python3-venv python3-wheel libxml2-dev libpq-dev libjpeg8-dev liblcms2-dev libxslt1-dev zlib1g-dev libsasl2-dev libldap2-dev build-essential git libssl-dev libffi-dev libmysqlclient-dev libjpeg-dev libblas-dev libatlas-base-dev -y

```

# 3. Install Postgresql

```sh

sudo apt install postgresql -y

```

# 4. Create user in Postgresql

```sh

sudo su - postgres -c "createuser -s odoo15"

```

# 5. Create system user

```sh

sudo useradd -m -d /opt/PYTHON/src/odoo15.0 -U -r -s /bin/bash odoo15

```


# 6. Install for html to pdf

```sh

sudo apt-get install wkhtmltopdf -y

wkhtmltopdf --version

#view version 0.12.6 or 0.16.6 is ok

```

# 7. Switch user odoo15 and git clone source code from github

```sh

su - odoo15

git clone https://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@github.com/mbf-odoo/mbf-odoo --depth 1 --branch 15/mbf/master /opt/PYTHON/src/mbf-odoo15

```

# 8. Switch to path and install virtual environment of python

```sh

cd ~/PYTHON/src/mbf-odoo15

python3 -m venv mbf-odoo15-venv

source mbf-odoo15-venv/bin/activate

pip3 install wheel
pip3 install -r requirements.txt

deactivate

```

# 9. Create custom-addons path for private dev

```sh

git clone https://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@github.com/mbf-odoo/mbf-15-addons --depth 1 --branch 15/mbf/master /opt/PYTHON/src/mbf-15-addons

exit

```


# 10. Create config for odoo

```sh

sudo nano ~/PYTHON/src/odoo15.0/odoo15-ubuntu.conf

```

# 11. Edit with content for odoo15.conf

```conf

[options]
; This is the password that allows database operations:
admin_passwd = <your password>
db_host = False
db_port = False
db_user = odoo15
db_password = False
xmlrpc_port = 8069
logfile = /opt/PYTHON/src/odoo15.0/logs/odoo15.log
addons_path = /opt/PYTHON/src/odoo15.0/logs/odoo/addons,/opt/PYTHON/src/odoo15.0/logs/custom-addons

```


# 12. Create log path and grant privillegs


# 13. Create service in ubuntu-22.04

```sh

# disable service
sudo systemctl stop odoo15
sudo systemctl disable odoo15
sudo systemctl daemon-reload
sudo ls -l /lib/systemd/system/
sudo ls -l /etc/systemd/system/


sudo nano /etc/systemd/system/odoo15.service

```

# 14. Edit content for service

```conf

[Unit]
Description=Odoo15 of ERP for SME
Requires=postgresql.service
After=network.target postgresql.service

[Service]
Type=simple
SyslogIdentifier=odoo15
PermissionsStartOnly=true
User=your-user
Group=your-group
# do chdir before running the service
WorkingDirectory=/opt/PYTHON/src/mbf-odoo15/
ExecStart=/opt/PYTHON/src/mbf-odoo15/mbf-odoo15-venv/bin/python3 ./odoo-bin -c ./cfg/odoo15-ubuntu.conf
StandardOutput=journal+console

[Install]
WantedBy=multi-user.target

```


```conf

[Unit]
Description=Odoo15 by Cuongdq for SME
Requires=postgresql.service
After=network.target postgresql.service

[Service]
Type=simple
SyslogIdentifier=odoo15
PermissionsStartOnly=true
User=cuongdq
Group=cuongdq
# do chdir before running the service
WorkingDirectory=/opt/PYTHON/src/mbf-odoo/
ExecStart=/opt/PYTHON/src/mbf-odoo/mbf-odoo15-venv/bin/python3 ./odoo-bin -c ./cfg/odoo15-ubuntu.conf
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

sudo systemctl enable --now odoo15

sudo systemctl status odoo15

sudo systemctl start odoo15

sudo systemctl stop odoo15

# Disable service in Odoo
sudo systemctl stop odoo15
sudo systemctl disable odoo15
sudo systemctl daemon-reload

```

# --------------- EXTRA -------------------

# RUN MANUNAL for test and dev

```sh

source mbf-odoo15-venv/bin/activate

./odoo-bin -c ./odoo15-dev.conf -d odoo15 -i base

```

# Go to web http://localhost:8069 for config odoo db and app
