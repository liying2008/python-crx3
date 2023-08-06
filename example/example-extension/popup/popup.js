function showCurrentTime() {
  alert(new Date())
}

window.addEventListener('DOMContentLoaded', function () {
  const showTimeBtn = document.getElementById('button1');
  showTimeBtn.addEventListener('click', showCurrentTime);
});
