(function(){
"use strict";
const $=(s,c=document)=>c.querySelector(s), $$=(s,c=document)=>[...c.querySelectorAll(s)];
const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
const FINE=matchMedia('(hover:hover) and (pointer:fine)').matches;
const root=document.documentElement;
if(RM) root.classList.add('rm');
const G=window.gsap, ST=window.ScrollTrigger;
if(G&&ST) G.registerPlugin(ST);
const YEARS=new Date().getFullYear()-1999;
$$('[data-years]').forEach(el=>el.textContent=YEARS);
$$('[data-year]').forEach(el=>el.textContent=new Date().getFullYear());

/* ---------- smooth scroll ---------- */
let lenis=null;
if(!RM && window.Lenis){
  lenis=new Lenis({duration:1.15,easing:t=>Math.min(1,1.001-Math.pow(2,-10*t)),smoothWheel:true});
  if(G&&ST){lenis.on('scroll',ST.update);G.ticker.add(t=>lenis.raf(t*1000));G.ticker.lagSmoothing(0);}
  else{(function raf(t){lenis.raf(t);requestAnimationFrame(raf)})(0);}
}
$$('a[href^="#"]').forEach(a=>a.addEventListener('click',e=>{const t=$(a.getAttribute('href'));if(!t)return;e.preventDefault();lenis?lenis.scrollTo(t,{offset:-70}):t.scrollIntoView({behavior:'smooth'});}));

/* ---------- curtain (intro + page transitions) ---------- */
const cur=$('.curtain'); const yr=$('.curtain .yr');
function lift(intro){
  root.classList.remove('intro','pt');
  if(!cur) return;
  cur.classList.add('cover');
  if(!G||RM){cur.classList.remove('cover');heroIn();return;}
  const tl=G.timeline({onComplete:()=>{cur.classList.remove('cover');G.set(cur,{clearProps:'all'});}});
  if(intro&&yr){const o={v:1999};tl.to(o,{v:new Date().getFullYear(),duration:1.1,ease:'power2.inOut',onUpdate:()=>yr.textContent=Math.round(o.v)});}
  tl.to(cur,{yPercent:-100,duration:.95,ease:'expo.inOut'},intro?'+=.15':0).add(heroIn,'-=.55');
}
let introShown=false;
try{introShown=sessionStorage.getItem('sai-intro')==='1';sessionStorage.setItem('sai-intro','1');}catch(e){}
const fromNav=root.classList.contains('pt');
if(yr) yr.hidden=!root.classList.contains('intro');

function go(href){
  if(!G||RM||!cur){location.href=href;return;}
  if(yr) yr.hidden=true;
  try{sessionStorage.setItem('sai-pt','1')}catch(e){}
  G.fromTo(cur,{yPercent:100},{yPercent:0,duration:.75,ease:'expo.inOut',onStart:()=>cur.classList.add('cover'),onComplete:()=>location.href=href});
}
$$('a[data-page]').forEach(a=>a.addEventListener('click',e=>{if(e.metaKey||e.ctrlKey||e.shiftKey||a.target==='_blank')return;e.preventDefault();go(a.getAttribute('href'));}));
addEventListener('pageshow',e=>{if(e.persisted&&cur){cur.classList.remove('cover');if(G)G.set(cur,{clearProps:'all'});}});

/* ---------- hero entrance ---------- */
let heroDone=false;
function heroIn(){
  if(heroDone)return;heroDone=true;
  if(!G||RM)return;
  G.from('.hero .ln>span',{yPercent:115,duration:1.3,ease:'expo.out',stagger:.09});
  G.from('.hero .eyebrow,.hero .hero-foot>*,.hero .stat',{y:30,opacity:0,duration:1.1,ease:'expo.out',stagger:.07,delay:.25});
  G.from('.hero-media img',{scale:1.18,duration:2.4,ease:'expo.out'});
}

/* ---------- nav ---------- */
const nav=$('.nav'); let lastY=0;
function onScroll(y){
  nav.classList.toggle('solid',y>60);
  if(!root.classList.contains('menu-open')) nav.classList.toggle('hide',y>lastY&&y>400);
  lastY=y;
}
if(lenis) lenis.on('scroll',({scroll})=>onScroll(scroll)); else addEventListener('scroll',()=>onScroll(scrollY),{passive:true});
onScroll(scrollY);
const burger=$('.burger');
burger&&burger.addEventListener('click',()=>{const o=root.classList.toggle('menu-open');burger.setAttribute('aria-expanded',o);o?lenis?.stop():lenis?.start();nav.classList.remove('hide');});

/* ---------- reveals ---------- */
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}}),{threshold:.15,rootMargin:'0px 0px -6% 0px'});
$$('.rv').forEach(el=>io.observe(el));

/* ---------- counters ---------- */
const cio=new IntersectionObserver(es=>es.forEach(e=>{if(!e.isIntersecting)return;cio.unobserve(e.target);const el=e.target,end=parseFloat(el.dataset.count||el.textContent),dec=(el.dataset.dec|0);
  if(!G||RM){el.textContent=end.toFixed(dec);return;}const o={v:0};G.to(o,{v:end,duration:2,ease:'power3.out',delay:.4,onUpdate:()=>el.textContent=o.v.toFixed(dec)});}),{threshold:.6});
$$('[data-count]').forEach(el=>{if(el.hasAttribute('data-years'))el.dataset.count=YEARS;cio.observe(el)});

if(G&&ST&&!RM){
  /* hero parallax */
  $$('.hero-media img').forEach(img=>G.to(img,{yPercent:12,ease:'none',scrollTrigger:{trigger:img.closest('.hero'),start:'top top',end:'bottom top',scrub:true}}));
  /* statement words */
  $$('.statement').forEach(st=>{
    const walk=n=>[...n.childNodes].forEach(c=>{if(c.nodeType===3){const f=document.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(w=>{if(!w)return;if(/^\s+$/.test(w)){f.appendChild(document.createTextNode(w));}else{const s=document.createElement('span');s.className='w';s.textContent=w;f.appendChild(s);}});c.replaceWith(f);}else walk(c);});
    walk(st);
    G.to($$('.w',st),{opacity:1,stagger:.1,ease:'none',scrollTrigger:{trigger:st,start:'top 80%',end:'bottom 45%',scrub:.6}});
  });
  /* expanding photo */
  $$('.expand figure').forEach(f=>{
    G.fromTo(f,{clipPath:'inset(0% 6% round 28px)'},{clipPath:'inset(0% 0% round 0px)',ease:'none',scrollTrigger:{trigger:f,start:'top 85%',end:'top 15%',scrub:true}});
    G.fromTo($('img',f),{yPercent:-12},{yPercent:0,ease:'none',scrollTrigger:{trigger:f,start:'top bottom',end:'bottom top',scrub:true}});
  });
  /* framed photo parallax */
  $$('.frame img,.band .bg img').forEach(img=>G.fromTo(img,{yPercent:-8},{yPercent:4,ease:'none',scrollTrigger:{trigger:img.parentElement,start:'top bottom',end:'bottom top',scrub:true}}));
  /* horizontal gallery */
  const mm=G.matchMedia();
  mm.add('(min-width:901px)',()=>{
    $$('.hscroll').forEach(h=>{const tr=$('.track',h);
      G.to(tr,{x:()=>-(tr.scrollWidth-innerWidth),ease:'none',scrollTrigger:{trigger:h,start:'center center',end:()=>'+='+(tr.scrollWidth-innerWidth),pin:true,scrub:.8,invalidateOnRefresh:true,anticipatePin:1}});
    });
  });
  /* timeline */
  $$('.tl').forEach(tl=>{
    const fill=$('.tl-fill',tl);G.set(fill,{'--p':0});
    G.to(fill,{'--p':1,ease:'none',scrollTrigger:{trigger:tl,start:'top 65%',end:'bottom 65%',scrub:true}});
    $$('.tl-item',tl).forEach(it=>ST.create({trigger:it,start:'top 65%',onEnter:()=>it.classList.add('on'),onLeaveBack:()=>it.classList.remove('on')}));
  });
  /* wordmark rise */
  $$('.wordmark').forEach(w=>G.from($$('span',w),{yPercent:60,opacity:0,stagger:.04,duration:1.2,ease:'expo.out',scrollTrigger:{trigger:w,start:'top 95%'}}));
  addEventListener('load',()=>ST.refresh());
  if(document.fonts) document.fonts.ready.then(()=>ST.refresh());
}else{
  $$('.tl-item').forEach(i=>i.classList.add('on'));
}

/* ---------- service row image peek ---------- */
const peek=$('.peek');
if(peek&&FINE&&!RM){
  let x=0,y=0,px=0,py=0,on=false;
  addEventListener('pointermove',e=>{x=e.clientX;y=e.clientY;});
  (function lp(){px+=(x-px)*.14;py+=(y-py)*.14;peek.style.left=px+'px';peek.style.top=py+'px';requestAnimationFrame(lp);})();
  $$('.row[data-img]').forEach(r=>{
    r.addEventListener('pointerenter',()=>{peek.classList.add('on');$$('img',peek).forEach(i=>i.classList.toggle('on',i.dataset.key===r.dataset.img));});
    r.addEventListener('pointerleave',()=>peek.classList.remove('on'));
  });
}

/* ---------- magnetic buttons + cursor ---------- */
if(FINE&&!RM){
  $$('.btn,.fab').forEach(b=>{
    b.addEventListener('pointermove',e=>{const r=b.getBoundingClientRect();b.style.setProperty('--mx',((e.clientX-r.left-r.width/2)*.22)+'px');b.style.setProperty('--my',((e.clientY-r.top-r.height/2)*.3)+'px');});
    b.addEventListener('pointerleave',()=>{b.style.setProperty('--mx','0px');b.style.setProperty('--my','0px');});
  });
  const c=document.createElement('div');c.className='cur';c.innerHTML='<i></i><b></b>';document.body.appendChild(c);
  const dot=$('i',c),ring=$('b',c);let mx=-100,my=-100,rx=-100,ry=-100;
  addEventListener('pointermove',e=>{mx=e.clientX;my=e.clientY;dot.style.transform=`translate(${mx}px,${my}px)`;});
  (function lp(){rx+=(mx-rx)*.16;ry+=(my-ry)*.16;ring.style.transform=`translate(${rx}px,${ry}px)`;requestAnimationFrame(lp);})();
  document.addEventListener('pointerover',e=>c.classList.toggle('big',!!e.target.closest('a,button,label,.card,.panel')));
  document.addEventListener('pointerleave',()=>c.style.opacity=0);document.addEventListener('pointerenter',()=>c.style.opacity=1);
}

/* ---------- wordmark letters ---------- */
$$('.wordmark').forEach(w=>{const t=w.textContent.trim();w.innerHTML=[...t].map(ch=>ch===' '?'<span>&nbsp;</span>':'<span>'+ch+'</span>').join('');});

/* ---------- enquiry form -> WhatsApp ---------- */
const form=$('#enquiry');
if(form){
  const WA='919512280270';
  form.addEventListener('submit',e=>{
    e.preventDefault();
    const v=n=>(form.elements[n]?.value||'').trim();
    const err=$('#enq-err');
    if(!v('name')||v('phone').replace(/\D/g,'').length<10){err.textContent='Please enter your full name and a 10-digit phone number so we can call you back.';return;}
    err.textContent='';
    const type=(form.querySelector('input[name=vtype]:checked')||{}).value||'';
    const lines=[`Hello Sai Auto Consultant,`,`Name: ${v('name')}`,`Phone: ${v('phone')}`];
    if(v('email'))lines.push(`Email: ${v('email')}`);
    lines.push(`Interested in: ${v('interest')}`);if(type)lines.push(`Vehicle type: ${type}`);if(v('message'))lines.push(`Message: ${v('message')}`);
    const text=lines.join('\n');
    $('#enq-text').textContent=text;
    $('#enq-wa').href='https://wa.me/'+WA+'?text='+encodeURIComponent(text);
    $('#enq-ready').hidden=false;
  });
  $('#enq-copy').addEventListener('click',()=>{const b=$('#enq-copy'),t=$('#enq-text');
    navigator.clipboard.writeText(t.textContent).then(()=>b.textContent='Copied',()=>{const s=getSelection(),r=document.createRange();r.selectNodeContents(t);s.removeAllRanges();s.addRange(r);b.textContent='Text selected';});});
}

/* ---------- start ---------- */
const introFlag=root.classList.contains('intro');
function start(){ if(introFlag||fromNav) lift(introFlag); else heroIn(); }
if(document.readyState==='complete') start(); else addEventListener('load',start);
setTimeout(()=>{if(root.classList.contains('intro')||root.classList.contains('pt')){root.classList.remove('intro','pt');heroIn();}},4000);
})();
