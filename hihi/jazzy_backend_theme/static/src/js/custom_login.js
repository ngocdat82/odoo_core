$(document).ready(function () {
  if ($(".for-login div").hasClass("oe_website_login_container") === true) {
    $(".for-login").append(`<div class="login_img_container">
        <div class="login_img">
            <img src="/jazzy_backend_theme/static/src/img/image_main_login.png"/>
        </div>
    </div>`);
    $(".for-login").addClass("for-login-wrapper");
    $(".for-login").css({
      margin: "auto",
      "box-shadow": "0px 0px 45px 10px rgb(0 0 0 / 37%)",
      "border-radius": "10px",
      "margin-top": "15px",
      "margin-bottom": "15px",
    });
  }

  if ($(".login_logo")) {
    const url = window.location.href; // Lấy URL hiện tại

    if (/(\.1erp|1erp\.vn)/.test(url)) {
        // Thực hiện hành động nếu URL chứa '.1erp' hoặc 1erp.vn
        $(".login_logo").append(`
          <div class="login_logo_box">
            <img src="/jazzy_backend_theme/static/src/img/1erp_logo.jpg"/>
          </div>
        `)
    } else if (/(\.1pos|1pos\.vn)/.test(url)) {
        // Thực hiện hành động nếu URL chứa '.1pos' hoặc 1pos.vn
        $(".login_logo").append(`
          <div class="login_logo_box">
            <img src="/jazzy_backend_theme/static/src/img/1POS_Logo-14.png"/>
          </div>
        `)
    } else {
      //  Đối với site không có .1pos hoặc .1erp
      $(".login_logo").append(`
        <div class="login_logo_box">
          <img src="/jazzy_backend_theme/static/src/img/1erp_logo.jpg"/>
        </div>
      `)
    }
  }

});
