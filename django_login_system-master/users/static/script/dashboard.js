// jQuery
// Required jquery for Dashboard 

$(function () {
     var currentdate = new Date();
     var datetime = "Now: " + currentdate.getDate() + "/"
          + (currentdate.getMonth() + 1) + "/"
          + currentdate.getFullYear() + " @ "
          + currentdate.getHours() + ":"
          + currentdate.getMinutes() + ":"
          + currentdate.getSeconds();

     var greeting = $(".greeting");
     greeting.text();

     if (currentdate.getHours() < 12) {
          greeting.text("Good Morning ");
     }
     else if (currentdate.getHours() > 11 && currentdate.getHours() < 17) {
          greeting.text("Good Afternoon ");
     }
     else if (currentdate.getHours() > 16 && currentdate.getHours() < 19) {
          greeting.text("Good Evening ");
     }
     else {
          greeting.text("Good Night ");
     }

     // user profile image
     function readURL(input) {
          if (input.files && input.files[0]) {
               var reader = new FileReader();
               reader.onload = function (e) {
                    $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                    $('#imagePreview').hide();
                    $('#imagePreview').fadeIn(650);
               }
               reader.readAsDataURL(input.files[0]);
          }
     }
     $("#imageUpload").change(function () {
          readURL(this);
     });


     // when click on information edit button
     var edit = $(".right-container .edit-info");
     edit.click(function () {
          $(this).slideUp(500);
          $(".right-container .info .user-info").slideUp(500);
          $(".right-container .info form").css("display", "block");
          get_values();
     });

     // when click on cancel butttom in form.
     var form_cancel = $(".right-container .info form .cancel-btn");
     form_cancel.click(function () {
          $(".right-container .info form").css("display", "none");
          $(".right-container .info .user-info").slideToggle();
          $(".right-container .edit-info").slideToggle();
     })

     // when click on save btn form
     var form_submit = $(".right-container .info form .submit-btn");
     form_submit.click(function () {
          $(".right-container .info form").css("display", "none");
          $(".right-container .info .user-info").fadeIn();
          $(".right-container .edit-info").slideToggle();

          var firstname = $(".right-container .info form .firstname").val();
          var lastname = $(".right-container .info form .lastname").val();
          var email = $(".right-container .info form .email").val()
          var about = $(".right-container .info form .bio").text();
          var skills = $(".right-container .info form .skill").text();

          $(".right-container .info .user-info .name").text(firstname + " " + lastname);
          $(".right-container .info .user-info .email").text(email);
          $(".right-container .info .user-info .about").text(about);
          $(".right-container .info .user-info .skills ul li").text(skills);

          
     });

});

function get_values() {
     var name = $(".right-container .info .user-info .name").text();
     var email = $(".right-container .info .user-info .email").text();
     var about = $(".right-container .info .user-info .about").text();
     var skills = $(".right-container .info .user-info .skills ul li").text();
     set_values(name, email, about, skills);
}
function set_values(name, email, about, skills) {
     var name = name;
     var email = email;
     var about = about;
     var skills = skills;

     var namearr = name.split(" ");
     $(".right-container .info form .firstname").val(namearr[0]);
     $(".right-container .info form .lastname").val(namearr[1]);
     $(".right-container .info form .email").val(email);
     $(".right-container .info form .bio").text(about);
     $(".right-container .info form .skill").text(skills);

}

function view_box() {
     // for open the post-viewer
     $(".center-container .items-section .all-itms .itm-card .itm-img")
     .click(function () {
          $(".view-wrapper").removeClass("close");
     });
     jqset
     // for closing the post-viewer
     $(".view-wrapper .inner-wrapper .close")
     .click(function () {
          $(".view-wrapper").addClass("close");
     });
}