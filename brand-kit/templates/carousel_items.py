import sys,os,subprocess
sys.path.insert(0,"/home/claude/ppp-studio/brand-kit")
from brand import *
R="/home/claude/ppp-studio/"
W,H=1080,1350; M=80; CW=W-2*M
GREY=(95,95,95)
def canvas(bg): im=Image.new("RGB",(W,H),bg); return im,ImageDraw.Draw(im)
def footer(im,d,n,N,fg):
    m=mark(54) if fg==INK else tile(60); im.paste(m,(M,H-M-m.size[1]),m)
    d.text((M+m.size[0]+22,H-M-36),"Peak Perspective Productions LLP",font=I("Bold",24),fill=fg)
    if N:
        t=f"{n}/{N}"; d.text((W-M-ink(d,t,I("Bold",24))[2],H-M-36),t,font=I("Bold",24),fill=fg)
def lines(d,ls,y,fill,size=None,gap=20):
    for t in ls:
        sz=min(size,fit_size(d,t,CW)) if size else None
        th,s=anton_line(d,t,M,y,CW,fill,size=sz); y+=th+gap
    return y
def para(d,txt,y,f,fill,maxw=CW,lh=1.4):
    for l in wrap(d,txt,f,maxw): d.text((M,y),l,font=f,fill=fill); y+=int(f.size*lh)
    return y
def carousel(slug,cover,items,cta,kicker):
    out=R+f"media/carousels/{slug}/"; os.makedirs(out,exist_ok=True); N=len(items)+2; imgs=[]
    im,d=canvas(CREAM)
    d.text((M,M+10),kicker,font=I("Bold",34),fill=RED)
    y=lines(d,cover[0],M+150,INK,size=cover[2])
    d.rectangle([M,y+30,M+180,y+44],fill=RED)
    para(d,cover[1],y+90,I("Bold",42),INK)
    footer(im,d,1,N,INK); imgs.append(im)
    themes=[(RED,CREAM,INK),(INK,CREAM,RED),(CREAM,INK,RED),(INK,CREAM,RED)]
    for i,(head,body) in enumerate(items):
        bg,fg,ac=themes[i%4]; im,d=canvas(bg)
        th,_=anton_line(d,f"0{i+1}",M-6,M+20,400,ac if bg!=RED else INK,size=260)
        y=lines(d,head,M+20+th+70,fg,size=150)
        para(d,body,y+40,I("Medium",40),fg if bg==RED else (fg if bg==INK else GREY))
        footer(im,d,i+2,N,fg); imgs.append(im)
    im,d=canvas(RED)
    t=tile(230); im.paste(t,(M,M+10),t)
    y=lines(d,cta,M+300,CREAM,size=150,gap=24)
    d.rectangle([M,y+50,W-M,y+50+160],fill=INK)
    s="DM us  ·  +91 98738 77010"; f=I("Bold",50); b=ink(d,s,f)
    d.text(((W-b[2])//2,y+50+80-b[3]//2-6),s,font=f,fill=CREAM)
    footer(im,d,N,N,CREAM); imgs.append(im)
    for k,im in enumerate(imgs): im.save(out+f"slide_{k+1}.jpg",quality=92)
    imgs[0].save(out+f"{slug.rsplit('-v',1)[0]}-carousel.pdf",save_all=True,append_images=imgs[1:],resolution=150)
    sheet=Image.new("RGB",(360*3,450*((N+2)//3)),INK)
    for k,im in enumerate(imgs): sheet.paste(im.resize((360,450)),((k%3)*360,(k//3)*450))
    sheet.save(f"/tmp/claude-0/sheet_{slug}.png")
os.makedirs("/tmp/claude-0",exist_ok=True)
carousel("factory-shoot-day-v1",(["FACTORY","SHOOT DAY."],"4 things to sort the day before the crew arrives.",170),
 [(["CLEAR","THE FLOOR."],"Walkways and the area around the key machines free of clutter, cartons and scrap. Every clear metre is a usable shot."),
  (["TELL US WHAT","IS RUNNING."],"Which lines run, at what time. Machines in motion sell; machines switched off look like a photo."),
  (["ACCESS AND","SAFETY."],"Gate passes, PPE sizes and the zones we may not enter, agreed in advance so the first hour isn't lost."),
  (["ONE PERSON","WHO KNOWS IT."],"Someone who can explain the process in plain words, on camera or off. That voice makes the film.")],
 ["SHOW THE","FACTORY BEFORE","THE VISIT."],"For manufacturers & exporters")
carousel("exhibitor-questions-v1",(["BEFORE YOU","BOOK AN","EXHIBITION","VIDEOGRAPHER"],"Ask these 4 questions.",150),
 [(["WHO EDITS","DURING THE SHOW?"],"If nobody edits on site, your reels arrive after the buyers have gone home."),
  (["DO THEY KNOW","THE HALL RULES?"],"Gate passes, filming permissions and power points vary by venue. Surprises cost you show hours."),
  (["WHICH CUT-DOWNS","DO YOU GET?"],"A hero film, short reels and a stall loop are three different edits. Agree all three upfront."),
  (["WHOSE MUSIC,","WHOSE FILES?"],"Licensed music and the raw footage should be yours to reuse after the show.")],
 ["PLAN YOUR","COVERAGE","EARLY."],"For exhibitors")
# single image
out=R+"media/images/restaurant-first-bite-v1/"; os.makedirs(out,exist_ok=True)
im,d=canvas(INK)
d.text((M,M+10),"For restaurants & cafés",font=I("Bold",34),fill=RED)
y=lines(d,["THE FIRST","BITE HAPPENS","ON A PHONE."],M+170,CREAM,size=190,gap=24)
d.rectangle([M,y+30,M+180,y+44],fill=RED)
para(d,"Menu films and kitchen reels that sell your food before anyone walks in.",y+90,I("Bold",42),CREAM)
footer(im,d,0,0,CREAM); im.save(out+"image.jpg",quality=92); im.save("/tmp/claude-0/sheet_image.png")
print("ok")
