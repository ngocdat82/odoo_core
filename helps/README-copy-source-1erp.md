# Cài đặt source máy chủ dev các phiên bản chạy

## Các site 15 phòng PM3 phát triển trên máy chủ
- www.1erp.vn
- demo.1erp.vn
- dev3.1erp.vn

## Site sổ tay Đảng viên
- sotaydangvien.1erp.vn

## Các site demo test thử khi dev và chức năng

### I. KHO MÃ NGUỒN GỐC CÓ CHỈNH SỬA TITLE VÀ LOGO 15:
```sh

# - demo-15-ce.1erp.vn
$ git clone https://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@github.com/mbf-odoo/mbf-odoo.git --depth 5 --branch 15/mbf/develop mbf-1erp-15
# hoặc từ kho gitlab của nội bộ - kiêm tra mạng nội bộ dns: 
$ git clone https://gitlab.mobifone.vn/trung-tam-cntt/phong-ptpm3/erp-sme/mbf-odoo.git --depth 5 --branch 15/mbf/develop mbf-1erp-15

# - demo-15-ee.1erp.vn
$ git clone https://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@github.com/mbf-odoo/mbf-odoo.git --depth 5 --branch 15/mbf/develop mbf-1erp-15-ee
# hoặc từ kho gitlab của nội bộ - kiêm tra mạng nội bộ dns: 
$ git clone https://gitlab.mobifone.vn/trung-tam-cntt/phong-ptpm3/erp-sme/mbf-odoo.git --depth 5 --branch 15/mbf/develop mbf-1erp-15-ee

```

### II. KHO ENTERPRISE 15 gốc:
```sh
$ git clone https://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@github.com/mbf-odoo/odoo-enterprise-15.0.git --depth 5 --branch develop enterprise-15.0
# hoặc từ kho gitlab của nội bộ - kiêm tra mạng nội bộ dns: 
$ git clone https://gitlab.mobifone.vn/trung-tam-cntt/phong-ptpm3/erp-sme/enterprise-15.0.git --depth 5 --branch develop enterprise-15.0


```

### III. KHO MÃ NGUỒN ODOO 16 CÓ CHỈNH SỬA LOGO VÀ TITLE:
```sh
# - demo-16-ce.1erp.vn
$ git clone https://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@github.com/mbf-odoo/mbf-odoo.git --depth 5 --branch 16/mbf/develop mbf-1erp-16
# hoặc từ kho gitlab của nội bộ - kiêm tra mạng nội bộ dns: 
$ git clone https://gitlab.mobifone.vn/trung-tam-cntt/phong-ptpm3/erp-sme/mbf-odoo.git --depth 5 --branch 16/mbf/develop mbf-1erp-16

# - demo-16-ee.1erp.vn
$ git clone https://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@github.com/mbf-odoo/mbf-odoo.git --depth 5 --branch 16/mbf/develop mbf-1erp-16-ee
# hoặc từ kho gitlab của nội bộ - kiêm tra mạng nội bộ dns: 
$ git clone https://gitlab.mobifone.vn/trung-tam-cntt/phong-ptpm3/erp-sme/mbf-odoo.git --depth 5 --branch 16/mbf/develop mbf-1erp-16-ee

```
### IV. KHO ENTERPRISE 16:
```sh
$ git clone https://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@github.com/mbf-odoo/odoo-enterprise-16.0.git --depth 5 --branch develop enterprise-16.0
# hoặc từ kho gitlab của nội bộ - kiêm tra mạng nội bộ dns: 
$ git clone https://gitlab.mobifone.vn/trung-tam-cntt/phong-ptpm3/erp-sme/enterprise-16.0.git --depth 5 --branch develop enterprise-16.0

```


## KHO ADDONS CỦA MOBIFONE LẬP TRÌNH

### 1. KHO ADDONS MÃ MẪU ĐỂ HỌC TẬP
```sh

$ git clone https://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@github.com/mbf-odoo/odoo-sample-addons.git
# hoặc từ kho gitlab của nội bộ - kiêm tra mạng nội bộ dns: 
$ git clone https://gitlab.mobifone.vn/trung-tam-cntt/phong-ptpm3/erp-sme/odoo-sample-addons.git

```

### 2. KHO ADDONS PHÁT TRIỂN 1ERP 15
```sh

$ git clone https://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@github.com/mbf-odoo/mbf-15-addons.git --branch develop mbf-15-addons
# hoặc từ kho gitlab của nội bộ - kiêm tra mạng nội bộ dns: 
$ git clone https://gitlab.mobifone.vn/trung-tam-cntt/phong-ptpm3/erp-sme/mbf-15-addons.git --branch develop mbf-15-addons

```

### 3. KHO ADDONS PHÁT TRIỂN 1ERP 16
```sh

$ git clone https://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@github.com/mbf-odoo/mbf-16-addons.git --branch develop mbf-16-addons
# hoặc từ kho gitlab của nội bộ - kiêm tra mạng nội bộ dns: 
$ git clone https://gitlab.mobifone.vn/trung-tam-cntt/phong-ptpm3/erp-sme/mbf-16-addons.git --branch develop mbf-16-addons

```


### 4. KHO NODEJS KẾT HỢP NGINX và ODOO

```sh

$ git clone https://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@github.com/mbf-odoo/mbf-nodejs-sso.git --branch stdv/no-db
# hoặc từ kho gitlab của nội bộ - kiêm tra mạng nội bộ dns: 
$ git clone https://gitlab.mobifone.vn/trung-tam-cntt/phong-ptpm3/erp-sme/mbf-nodejs-sso.git --branch stdv/no-db

```


### 5. KHO SỔ TAY ĐẢNG VIÊN

```sh

$ git clone https://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@github.com/mbf-odoo/mbf-stdv-15-addons.git --branch stdv/mobifone
# hoặc từ kho gitlab của nội bộ - kiêm tra mạng nội bộ dns: 
$ git clone https://gitlab.mobifone.vn/trung-tam-cntt/phong-ptpm3/erp-sme/mbf-stdv-15-addons.git --branch stdv/mobifone

```
