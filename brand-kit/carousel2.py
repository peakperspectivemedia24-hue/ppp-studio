import sys; import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from brand import *
import os
W,H=1080,1350; M=70; CW=W-2*M
os.makedirs("out/carousel",exist_ok=True)
def canvas(bgc): im=Image.new("RGB",(W,H),bgc); return im,ImageDraw.Draw(im)
def footer(im,d,n,fg,body,accent,swipe=True):
    m=mark(54) if fg==INK else tile(60); im.paste(m,(M,H-M-(54 if fg==INK else 60)),m)
    d.text((M+m.size[0]+22,H-M-34),"Peak Perspective Productions LLP",font=I("Bold",24),fill=fg)
    t=f"{n}/6"; d.text((W-M-d.textbbox((0,0),t,font=I("Bold",24))[2],H-M-34),t,font=I("Bold",24),fill=fg)
def stack(d,lines,y,fills,gap=26,size_override=None):
    for (t,*opt),fill in zip(lines,fills):
        th,s=anton_line(d,t,M,y,CW,fill,size=opt[0] if opt else None); y+=th+gap
    return y
def deco_arc(d,cx,cy,r,th,fill,a0=270,a1=90): arc(d,cx,cy,r,th,a0,a1,fill)
# 1 cover
im,d=canvas(CREAM)
y=M+10
y=stack(d,[("500 BOOTHS.",),("BUYERS REMEMBER",)],y+130,[INK,INK],gap=22)
th,s=anton_line(d,"3.",M-8,y+10,CW+20,RED,size=640)
f=I("Bold",46)
for i,l in enumerate(["Make yours","one of them."]): d.text((560,y+10+th-140+i*62),l,font=f,fill=INK)
footer(im,d,1,INK,INK,RED); im.save("out/carousel/v2_1.png")
# 2 red
im,d=canvas(RED)
y=M+40
y=stack(d,[("NOBODY",190),("READS A",190),("SPEC SHEET",190),("AT A TRADE",190),("FAIR.",190)],y,[CREAM]*5,gap=22)
f=I("Bold",40); yy=y+36
for l in wrap(d,"A 30-second film does the talking while your team talks to someone else.",f,CW-40):
    d.text((M,yy),l,font=f,fill=CREAM); yy+=56
footer(im,d,2,CREAM,CREAM,INK); im.save("out/carousel/v2_2.png")
# 3 black list
im,d=canvas(INK)
d.text((M,M+6),"What we make",font=I("Bold",34),fill=RED)
items=["PRODUCT FILMS","FOUNDER STORIES","SAME-DAY REELS","AI AD FILMS","PHOTO + PRINT","SOCIAL MEDIA"]
y=M+90
for i,t in enumerate(items):
    d.line([M,y,W-M,y],fill=(70,70,70),width=3)
    th,s=anton_line(d,t,M,y+34,CW,RED if t=="AI AD FILMS" else CREAM,size=118)
    y+=th+34+34
footer(im,d,3,CREAM,CREAM,RED); im.save("out/carousel/v2_3.png")
# 4 proof
im,d=canvas(CREAM)
d.text((M,M+6),"Asian Fencing Championship",font=I("Bold",34),fill=INK)
d.text((M,M+52),"Bharat Mandapam · 35+ countries",font=I("Medium",30),fill=(90,90,90))
th,s=anton_line(d,"FROM 100K TO",M,260,CW,INK,size=170)
th2,s2=anton_line(d,"3.5M",M-12,260+th+40,CW+30,RED)
y=260+th+40+th2+50
th3,_=anton_line(d,"REACH IN 12 DAYS.",M,y,CW,INK,size=118)
f=I("Medium",30); 
for i,l in enumerate(wrap(d,"Our result on one event. Yours will depend on your brief, your audience and your budget.",f,CW)):
    d.text((M,y+th3+36+i*44),l,font=f,fill=(90,90,90))
footer(im,d,4,INK,INK,RED); im.save("out/carousel/v2_4.png")
# 5 timeline
im,d=canvas(CREAM)
d.text((M,M+6),"How an event becomes content",font=I("Bold",34),fill=RED)
rows=[("BEFORE","Teasers and stories that build the crowd."),("DURING","Cameras on the floor. Nothing missed."),("SAME NIGHT","Edited reels posted while the show is still on."),("AFTER","The film you keep using long after.")]
x0=M+30; y=M+130; step=250
d.line([x0,y+34,x0,y+step*3+34],fill=INK,width=8)
for i,(a,b) in enumerate(rows):
    yy=y+i*step
    d.ellipse([x0-30,yy+4,x0+30,yy+64],fill=RED if i==2 else INK)
    anton_line(d,a,x0+70,yy,CW-100,INK,size=120)
    d.text((x0+74,yy+150),b,font=I("Bold",34),fill=(60,60,60))
footer(im,d,5,INK,INK,RED); im.save("out/carousel/v2_5.png")
# 6 CTA
im,d=canvas(RED)
m=tile(250); im.paste(m,(M,M+10),m)
y=M+290
y=stack(d,[("TALK TO US",),("BEFORE THE",),("STALL GOES UP.",)],y,[CREAM]*3,gap=26)
d.rectangle([M,y+50,W-M,y+50+170],fill=INK)
t="DM us  ·  +91 98738 77010"; f=I("Bold",52); b=ink(d,t,f)
d.text(((W-b[2])//2,y+50+85-b[3]//2-6),t,font=f,fill=CREAM)
footer(im,d,6,CREAM,CREAM,INK); im.save("out/carousel/v2_6.png")
s=Image.new("RGB",(1080,900))
for i in range(6): s.paste(Image.open(f"out/carousel/v2_{i+1}.png").resize((360,450)),((i%3)*360,(i//3)*450))
s.save("out/contact_v2.png")
