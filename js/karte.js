(function(){
  var el=document.getElementById('karte');if(!el||!window.L)return;
  var en=document.documentElement.lang==='en';
  var map=L.map(el,{scrollWheelZoom:false,zoomSnap:0.25});
  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{maxZoom:18,
    attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>-Mitwirkende (ODbL)'}).addTo(map);
  var farben={'Wildnisgebiet Königsbrücker Heide':'#003c32','Gohrischheide und Elbniederterrasse Zeithain':'#8a5a8c'};
  var flaechen={},alle=L.featureGroup().addTo(map);
  var pfadStil={color:'#c77700',weight:4,opacity:.95,dashArray:'1 0'};
  var turm=L.divIcon({className:'',html:'<svg width="34" height="34" viewBox="0 0 34 34" aria-hidden="true"><circle cx="17" cy="17" r="15" fill="#ffc842" stroke="#003c32" stroke-width="3"/><path d="M12 25l3-13h4l3 13M14 18h6" stroke="#003c32" stroke-width="2.4" fill="none"/></svg>',iconSize:[34,34],iconAnchor:[17,17]});
  fetch(el.getAttribute('data-src')).then(function(r){return r.json()}).then(function(g){
    L.geoJSON(g,{
      filter:function(f){return f.properties.kind==='area'},
      style:function(f){var c=farben[f.properties.name]||'#003c32';return{color:c,weight:3,fillColor:c,fillOpacity:.18}},
      onEachFeature:function(f,l){flaechen[f.properties.name]=l;alle.addLayer(l);
        l.bindTooltip(f.properties.name,{sticky:true});
        l.on('click',function(){map.flyToBounds(l.getBounds(),{padding:[20,20],duration:.8})})}
    }).addTo(map);
    L.geoJSON(g,{filter:function(f){return f.properties.kind==='route'},style:function(){return pfadStil},
      onEachFeature:function(f,l){l.bindPopup('<h3>'+f.properties.name+'</h3><p>'+(en?'Visitor trail (route data: OpenStreetMap).':'Besucherpfad (Verlauf: OpenStreetMap). Beschreibung, Faltblatt und Wanderkarte folgen auf der Pfadseite.')+'</p><a class="pfeil" href="'+(en?'../':'')+'wildnisgebiet.html">'+(en?'Read more':'Mehr erfahren …')+'</a>')}}).addTo(map);
    L.geoJSON(g,{filter:function(f){return f.properties.kind==='poi'},
      pointToLayer:function(f,ll){return L.marker(ll,{icon:turm,title:f.properties.name,keyboard:true})},
      onEachFeature:function(f,l){l.bindPopup('<h3>'+f.properties.name+'</h3><p>'+f.properties.text+'</p><a class="pfeil" href="'+(en?'../':'')+'veranstaltungen.html">'+(en?'Guided tours':'Führungen &amp; Termine')+'</a>')}}).addTo(map);
    map.fitBounds(alle.getBounds(),{padding:[20,20]});
    document.querySelectorAll('[data-zoom-gebiet]').forEach(function(b){b.addEventListener('click',function(){
      var n=b.getAttribute('data-zoom-gebiet');
      if(n==='alle')map.flyToBounds(alle.getBounds(),{padding:[20,20],duration:.8});
      else if(flaechen[n])map.flyToBounds(flaechen[n].getBounds(),{padding:[20,20],duration:.8});
      el.focus({preventScroll:true});
    })});
  });
})();
