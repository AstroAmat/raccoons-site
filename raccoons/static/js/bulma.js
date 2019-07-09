"use strict";

var $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll(".navbar-burger"), 0);

if ($navbarBurgers.length > 0) {
  $navbarBurgers.forEach(function (el) {
    el.addEventListener("click", function () {
      var target = el.dataset.target;
      var $target = document.getElementById(target);
      el.classList.toggle("is-active");
      $target.classList.toggle("is-active");
    });
  });
}

var $notification;

(document.querySelectorAll(".notification .delete") || []).forEach(function ($delete) {
  $notification = $delete.parentNode;
  $delete.addEventListener("click", function () {
    $notification.parentNode.removeChild($notification);
  });
});