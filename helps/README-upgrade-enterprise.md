# NÂNG CẤP MÁY CHỦ ODOO CE THÀNH EE

1. Shutdown your server

2. Backup your community database

3. Update the --addons-path parameter of your launch command (see Source Install)

4. Install the web_enterprise module by using

- $ -d <database_name> -i web_enterprise --stop-after-init
Depending on the size of your database, this may take some time.

```sh

$ source mbf-odoo15-venv/bin/activate

(mbf-odoo15-venv)$ ./odoo-bin -c ./cfg/odoo15-ubuntu.conf -d mobifone.ddns.net -i web_enterprise --stop-after-init
(mbf-odoo15-venv)$ ./odoo-bin -c ./cfg/odoo15-ubuntu.conf -d cuongdq.no-ip.info -i web_enterprise --stop-after-init

```

## CÀI ĐẶT NÂNG CẤP TRÊN WIN

- Kiểm tra tham số cài đặt của odoo trên win ở dịch vụ, tìm python, và gọi đúng file python đã cài là được

```sh

$

> & 'C:\Program Files\Odoo 15.0.20220905\python\python.exe' ./odoo-bin -c ./cfg/odoo15-cuongdq-24.36.conf -d debug-36 -i web_enterprise --stop-after-init

```

5. Restart your server with the updated addons path of point 3. You should be able to connect to your instance. You can then link your database with your Odoo Enterprise Subscription by entering the code you received by e-mail in the form input