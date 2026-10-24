
document.addEventListener('DOMContentLoaded',function(){
  var t=document.querySelector('.menu-toggle'),n=document.querySelector('.nav');
  if(t&&n){t.addEventListener('click',function(){n.classList.toggle('open')});}
  var y=document.getElementById('year');if(y){y.textContent=new Date().getFullYear();}
  var f=document.getElementById('prodFilter');
  if(f){f.addEventListener('input',function(){
    var q=f.value.toLowerCase();
    document.querySelectorAll('.prod-card').forEach(function(c){
      c.style.display=c.textContent.toLowerCase().indexOf(q)>-1?'':'none';
    });
  });}
  var params=new URLSearchParams(location.search),slug=params.get('product');
  if(slug){var sel=document.getElementById('f_product');
    if(sel){for(var i=0;i<sel.options.length;i++){if(sel.options[i].value===slug){sel.selectedIndex=i;break;}}}}
});
