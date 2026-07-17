const CACHE='jupiter-v1';
const PRECACHE=[
  'index.html','arbre.html','revisions.html',
  'mobile.html','editeur.html','deposer.html',
  'manifest.json','icon-192.png','icon-512.png'
];
self.addEventListener('install',e=>{
  e.waitUntil(caches.open(CACHE).then(c=>c.addAll(PRECACHE)).then(()=>self.skipWaiting()));
});
self.addEventListener('activate',e=>{
  e.waitUntil(caches.keys().then(ks=>Promise.all(
    ks.filter(k=>k!==CACHE).map(k=>caches.delete(k))
  )).then(()=>self.clients.claim()));
});
self.addEventListener('fetch',e=>{
  if(e.request.url.endsWith('.json')){
    e.respondWith(fetch(e.request).catch(()=>caches.match(e.request)));
    return;
  }
  e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request).then(res=>{
    caches.open(CACHE).then(c=>c.put(e.request,res.clone()));
    return res;
  })));
});
