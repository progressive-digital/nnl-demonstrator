(function(){
  var root=document.documentElement, store={
    get:function(k){try{return localStorage.getItem(k)}catch(e){return null}},
    set:function(k,v){try{localStorage.setItem(k,v)}catch(e){}}
  };
  // Schriftgröße + Kontrast (persistiert je Besucher)
  var zoom=parseFloat(store.get('nnl-zoom')||'1');
  function applyZoom(){root.style.setProperty('--zoom',zoom)}
  applyZoom();
  if(store.get('nnl-kontrast')==='hoch')root.setAttribute('data-contrast','hoch');
  document.addEventListener('click',function(ev){
    var b=ev.target.closest('[data-a11y]');if(!b)return;
    var a=b.getAttribute('data-a11y');
    if(a==='plus'){zoom=Math.min(1.5,+(zoom+0.125).toFixed(3));applyZoom();store.set('nnl-zoom',zoom)}
    if(a==='minus'){zoom=Math.max(0.875,+(zoom-0.125).toFixed(3));applyZoom();store.set('nnl-zoom',zoom)}
    if(a==='kontrast'){var on=root.getAttribute('data-contrast')!=='hoch';
      if(on)root.setAttribute('data-contrast','hoch');else root.removeAttribute('data-contrast');
      store.set('nnl-kontrast',on?'hoch':'normal');b.setAttribute('aria-pressed',on)}
    if(a==='vorlesen'){
      if(!('speechSynthesis' in window)){alert('Ihr Browser unterstützt die Vorlesefunktion nicht.');return}
      if(speechSynthesis.speaking){speechSynthesis.cancel();b.setAttribute('aria-pressed','false');return}
      var main=document.getElementById('inhalt');var u=new SpeechSynthesisUtterance(main.innerText);
      u.lang=root.lang==='en'?'en-GB':'de-DE';u.onend=function(){b.setAttribute('aria-pressed','false')};
      speechSynthesis.speak(u);b.setAttribute('aria-pressed','true')}
  });
  document.querySelectorAll('[data-a11y="kontrast"]').forEach(function(b){b.setAttribute('aria-pressed',root.getAttribute('data-contrast')==='hoch')});

  // Mobile Navigation
  var kopf=document.querySelector('.kopf'),mb=document.querySelector('.menu-btn');
  if(mb){mb.addEventListener('click',function(){var o=kopf.classList.toggle('offen');mb.setAttribute('aria-expanded',o)})}
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&kopf.classList.contains('offen')){kopf.classList.remove('offen');mb.setAttribute('aria-expanded','false');mb.focus()}});

  // Suche (Demonstrator: clientseitig über Seitentitel/Stichworte)
  var idx=window.NNL_SUCHINDEX||[];
  document.querySelectorAll('form.suche').forEach(function(f){
    f.addEventListener('submit',function(e){e.preventDefault();
      var q=(f.q.value||'').toLowerCase().trim();if(!q)return;
      var hit=idx.find(function(p){return (p.t+' '+p.k).toLowerCase().indexOf(q)>-1});
      if(hit){location.href=f.getAttribute('data-base')+hit.u}
      else{var m=f.parentNode.querySelector('.suche-meldung');if(m){m.textContent='Keine Treffer für „'+f.q.value+'“ im Demonstrator.'}}
    })});

  // Veranstaltungsfilter
  var filter=document.querySelector('.filter');
  if(filter){filter.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
    filter.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});
    var k=b.getAttribute('data-filter');var n=0;
    document.querySelectorAll('.termine--liste .termin').forEach(function(t){var s=(k==='alle'||t.getAttribute('data-gebiet')===k);t.hidden=!s;if(s)n++});
    var st=document.getElementById('filter-status');if(st)st.textContent=n+' Termine angezeigt';
  })}
})();
