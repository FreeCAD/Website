/* Script to detect User Agent and order corresponding download options. */

document.addEventListener("DOMContentLoaded", function () {
  var userAgent = window.navigator.userAgent.toLowerCase();
  var windowsDiv = document.getElementById('windows');
  var macDiv = document.getElementById('mac');
  var linuxDiv = document.getElementById('linux');

  if (userAgent.includes('win')) {
    windowsDiv.style.order = '3';
  } else if (userAgent.includes('mac')) {
    macDiv.style.order = '2';
  } else if (userAgent.includes('lin')) {
    linuxDiv.style.order = '1';
  }
});