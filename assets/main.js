// Mobile nav toggle
(function(){
  var t = document.getElementById('navToggle'), n = document.getElementById('nav');
  if(!t || !n) return;
  t.addEventListener('click', function(){
    var open = n.classList.toggle('open');
    t.setAttribute('aria-expanded', open ? 'true' : 'false');
    t.innerHTML = open ? '&times;' : '&#9776;';
  });
})();
