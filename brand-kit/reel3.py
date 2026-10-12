import sys,subprocess; import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from brand import *
W,H,FPS,DUR=1080,1920,30,20.0; M=70; CW=W-2*M
SS=3
def punch(lt,span=0.16,amt=0.14): return 1+amt*(1-ease(lt/span))
def new(bg): im=Image.new("RGB",(W,H),bg); return im,ImageDraw.Draw(im)
def stack_center(d,lines,fills,scale=1.0,yoff=0,gapf=0.14,width=CW):
    items=[]
    for t,sz in lines:
        s=(sz or fit_size(d,t,width))*scale; b=ink(d,t,A(s)); items.append((t,s,b))
    tot=sum(b[3]-b[1] for _,_,b in items)+sum(int(s*gapf) for _,s,_ in items[:-1])
    y=(H-tot)//2+yoff; global LAST_TOP; LAST_TOP=y
    for (t,s,b),fill in zip(items,fills):
        w=b[2]-b[0]; d.text(((W-w)//2-b[0],y-b[1]),t,font=A(s),fill=fill); y+=(b[3]-b[1])+int(s*gapf)
    return y
def center_text(d,t,f,y,fill):
    b=ink(d,t,f); d.text(((W-b[2])//2,y),t,font=f,fill=fill)
def aa_rrect(w,h,r,fill):
    L=Image.new("RGBA",(w*SS,h*SS),(0,0,0,0)); ImageDraw.Draw(L).rounded_rectangle([0,0,w*SS-1,h*SS-1],radius=r*SS,fill=fill+(255,))
    return L.resize((w,h),Image.LANCZOS)
def paste_rrect(im,x,y,w,h,r,fill):
    p=aa_rrect(w,h,r,fill); im.paste(p,(int(x),int(y)),p)
def ring(im,cx,cy,r,th,p,col,track):
    S=(2*r+th*2+8); L=Image.new("RGBA",(S*SS,S*SS),(0,0,0,0)); d=ImageDraw.Draw(L); c=S*SS//2; R=r*SS
    d.ellipse([c-R,c-R,c+R,c+R],outline=track+(255,),width=th*SS)
    if p>0.003: d.arc([c-R,c-R,c+R,c+R],-90,-90+360*p,fill=col+(255,),width=th*SS)
    L=L.resize((S,S),Image.LANCZOS); im.paste(L,(cx-S//2,cy-S//2),L)
# ---- feed cards (built once) -------------------------------------------------
CWD,CHT=860,900
GRAY=(222,210,190)
def make_card(winner=False):
    c=aa_rrect(CWD,CHT,44,CREAM); d=ImageDraw.Draw(c)
    # header
    if winner:
        t=tile(86); c.paste(t,(40,36),t); 
        d.text((150,48),"Peak Perspective Productions LLP",font=I("Bold",34),fill=INK); d.text((150,92),"Delhi-NCR",font=I("Medium",28),fill=(110,110,110))
    else:
        d.ellipse([40,40,116,116],fill=GRAY); d.rounded_rectangle([140,48,440,70],radius=11,fill=GRAY); d.rounded_rectangle([140,86,320,104],radius=9,fill=GRAY)
    img=aa_rrect(CWD-80,560,30,RED if winner else GRAY); c.paste(img,(40,150),img)
    if winner:
        d2=ImageDraw.Draw(c); b=ink(d2,"STOP.",A(300)); d2.text((40+(CWD-80-b[2])//2-b[0],150+(560-(b[3]-b[1]))//2-b[1]),"STOP.",font=A(300),fill=CREAM)
        d.text((40,740),"The one they remember.",font=I("Bold",44),fill=INK)
    else:
        d.rounded_rectangle([40,740,CWD-160,764],radius=12,fill=GRAY); d.rounded_rectangle([40,790,CWD-340,812],radius=11,fill=GRAY)
    return c
CARD=make_card(False); WIN=make_card(True)
PITCH=940; D=6*PITCH
SERV=["FILMS","PHOTOS","REELS","SOCIAL","PRINT","AI ADS","CAMPAIGNS","STORIES"]
FORS=["STARTUPS","RESTAURANTS","FASHION","FOUNDERS","EXHIBITORS","SCHOOLS"]
def fmt(v): return f"{int(round(v))}K" if v<1000 else f"{v/1000:.1f}M"
def frame(t):
    if t<0.5:
        im,d=new(INK); stack_center(d,[("YOU GET",None)],[CREAM],punch(t))
    elif t<1.0:
        im,d=new(INK); lt=t-0.5; stack_center(d,[("3 SECONDS.",None)],[RED],punch(lt))
    elif t<2.5:
        im,d=new(CREAM); lt=t-1.0; i=int(lt//0.5); dl=lt-i*0.5
        ring(im,540,880,330,38,1-lt/1.5,RED,(236,224,204)); d=ImageDraw.Draw(im)
        s=640*punch(dl,0.14,0.12); b=ink(d,str(3-i),A(s)); d.text((540-(b[0]+b[2])//2,880-(b[1]+b[3])//2),str(3-i),font=A(s),fill=INK)
    elif t<5.0:
        im,d=new(INK); lt=t-2.5
        u=min(1,lt/2.0); e=1-(1-u)**3
        for i in range(8):
            y=420+(i-6)*PITCH+D*(1-e)
            if -CHT<y<H:
                src=WIN if i==6 else CARD; im.paste(src,((W-CWD)//2,int(y)),src)
        d=ImageDraw.Draw(im); d.rectangle([0,0,W,380],fill=INK)
        if lt<2.0: stack_center(d,[("EVERYONE",None),("SCROLLS.",None)],[CREAM,CREAM],0.5,yoff=-720,width=CW)
        else: stack_center(d,[("UNTIL SOMETHING",None),("STOPS THEM.",None)],[CREAM,RED],0.38,yoff=-720,width=CW)
    elif t<9.0:
        i=int((t-5.0)//0.5); lt=(t-5.0)-i*0.5
        bgc,fg=[(CREAM,INK),(INK,CREAM),(RED,CREAM)][i%3]
        if SERV[i]=="AI ADS": bgc,fg=INK,RED
        im,d=new(bgc)
        words=SERV[i].split(" ") if i!=5 else ["AI ADS"]
        y0=stack_center(d,[(w,None) for w in words],[fg]*len(words),punch(lt),yoff=30)
        f=I("Bold",46); b=ink(d,"we make",f); d.text(((W-b[2])//2,LAST_TOP-84),"we make",font=f,fill=fg)
    elif t<14.0:
        im,d=new(CREAM); lt=t-9.0
        stack_center(d,[("REAL",None),("NUMBERS.",None)],[INK,INK],0.52*punch(lt,0.2,0.1),yoff=-640,width=CW)
        base=1500; hmax=620; x1,x2,bw=210,630,240
        d=ImageDraw.Draw(im); d.rectangle([140,base,940,base+7],fill=INK)
        h1=max(10,int(hmax*100/3500))
        g1=ease((lt-0.2)/0.4); bh1=int(h1*g1)
        if bh1>0: paste_rrect(im,x1,base-bh1,bw,bh1,6 if bh1>12 else 3,INK)
        g2=ease((lt-0.9)/1.8); bh2=int(hmax*g2)
        if bh2>0: paste_rrect(im,x2,base-bh2,bw,bh2,10,RED)
        d=ImageDraw.Draw(im)
        v1=100; v2=lerp(100,3500,g2)
        f=A(120); b=ink(d,fmt(v1),f); d.text((x1+(bw-b[2])//2-b[0],base-bh1-30-(b[3]-b[1])-b[1]),fmt(v1),font=f,fill=INK)
        tt=fmt(v2); b=ink(d,tt,A(150)); d.text((x2+(bw-(b[2]-b[0]))//2-b[0]-0,base-bh2-36-(b[3]-b[1])-b[1]),tt,font=A(150),fill=RED)
        f=I("Bold",36)
        for x,l in ((x1,"Before"),(x2,"12 days later")):
            b=ink(d,l,f); d.text((x+(bw-b[2])//2,base+36),l,font=f,fill=INK)
        if lt>2.5:
            k=punch(lt-2.5,0.25,0.35); s=300*k; b=ink(d,"35X",A(s)); d.text((140-b[0],700-b[1]),"35X",font=A(s),fill=RED)
            d.text((148,700+(b[3]-b[1])+26),"the reach, roughly",font=I("Bold",40),fill=INK)
        if lt>3.2:
            f=I("Medium",32)
            for j,l in enumerate(["Asian Fencing Championship · Bharat Mandapam","35+ countries · social reach · our result on one event"]):
                b=ink(d,l,f); d.text(((W-b[2])//2,1668+j*46),l,font=f,fill=(70,70,70))
    elif t<17.0:
        i=int((t-14.0)//0.5); lt=(t-14.0)-i*0.5
        bgc,fg=[(INK,CREAM),(RED,CREAM),(CREAM,INK)][i%3]
        im,d=new(bgc)
        stack_center(d,[(FORS[i],None)],[fg],punch(lt),yoff=40)
        f=I("Bold",46); b=ink(d,"made for",f); d.text(((W-b[2])//2,LAST_TOP-84),"made for",font=f,fill=fg)
    else:
        im,d=new(CREAM); lt=t-17.0
        k=ease(lt/0.4); mh=int(lerp(220,430,k)); m=mark(mh); im.paste(m,((W-m.size[0])//2,230),m)
        d=ImageDraw.Draw(im)
        y=stack_center(d,[("YOUR TURN.",None)],[INK],punch(lt,0.2,0.08),yoff=210)
        d.rectangle([M,y+60,W-M,y+60+140],fill=RED); f=I("Bold",58); l="DM us  ·  +91 98738 77010"; b=ink(d,l,f); d.text(((W-b[2])//2,y+60+70-b[3]//2-4),l,font=f,fill=CREAM)
        f2=I("Bold",32); l2="Peak Perspective Productions LLP"; b=ink(d,l2,f2); d.text(((W-b[2])//2,y+250),l2,font=f2,fill=INK)
    return im
if __name__=="__main__":
    cmd=["ffmpeg","-y","-loglevel","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-","-i","out/beat3.wav","-c:v","libx264","-pix_fmt","yuv420p","-crf","16","-preset","medium","-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart","out/ppp_brand_reel_v3.mp4"]
    p=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    for n in range(int(DUR*FPS)): p.stdin.write(frame(n/FPS).tobytes())
    p.stdin.close(); p.wait(); print("done")
