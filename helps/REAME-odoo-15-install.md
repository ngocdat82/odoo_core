# TÀI LIỆU CÀI ĐẶT MÃ NGUỒN ODOO 15

## Mô tả phiên bản và nhánh

- Mã nguồn odoo15 đã được chỉnh sửa các logo, title của Mobifone trên phiên bản CE tại nhánh 15/mbf/master
- Và khi phát triển để chạy thử và sẽ rẽ nhánh chạy ở nhánh 15/mbf/develop và nhánh này được rẽ từ nhánh 15/mbf/master
- Các đặc điểm chỉnh sửa trên mã nguồn gốc được rẻ nhánh ra với tiếp đầu ngữ là 15/mbf/feature/xxxx
- Mỗi khi có sự cập nhập fixbug của kho gốc của Odoo, techlead có nhiệm vụ pull nhánh 15.0 từ odoo và merge vào nhánh 15/mbf/develop và test chạy thử
- Khi ổn định không có lỗi thì merge nhánh 15/mbf/devlop vào nhánh 15/mbf/master để lưu trữ.
- Khi cài đặt để chạy trên môi trường phát triển sẽ pull nhánh 15/mbf/master để cài đặt trên các máy chủ để chạy
- Phiên bản xuất bản ổn định là thuộc nhánh 15/mbf/release/1.0

## KHO GIT ĐỂ LẤY VỀ CÀI ĐẶT BẢN RELASE

```sh

# Từ gitlab
$ git clone https://gitlab.mobifone.vn/trung-tam-cntt/phong-ptpm3/erp-sme/mbf-odoo.git --depth 5 --branch 15/mbf/release/1.0 mbf-1erp-15

# Từ github
$ git clone https://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@github.com/mbf-odoo/mbf-odoo.git --depth 5 --branch 15/mbf/release/1.0 mbf-1erp-15

```


