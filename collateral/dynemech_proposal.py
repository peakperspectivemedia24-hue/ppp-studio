import sys,os,math
HERE_C=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HERE_C,"..","brand-kit"))
from brand import *
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
AS=os.path.join(HERE_C,"dynemech_assets")
W,H=1654,2339; M=120; CW=W-2*M
GREY=(105,100,95); LINE=(214,205,190); SOFT=(240,230,212)
def page(bg=CREAM):
    im=Image.new("RGB",(W,H),bg); return im,ImageDraw.Draw(im)
def para(d,t,x,y,w,f,fill=INK,lh=1.45):
    for ln in wrap(d,t,f,w): d.text((x,y),ln,font=f,fill=fill); y+=int(f.size*lh)
    return y
def logo(im,x=None,y=None,h=150,on_dark=False):
    if on_dark:
        t=tile(h); im.paste(t,(W-M-t.size[0] if x is None else x,(M-20) if y is None else y),t); return
    lg=Image.open(os.path.join(HERE,"logo.jpg")).convert("RGB"); r=h/lg.height
    lg=lg.resize((int(lg.width*r),h)); im.paste(lg,(W-M-lg.width if x is None else x,(M-20) if y is None else y))
def footer(d,n,dark=False):
    d.line([M,H-120,W-M,H-120],fill=(70,70,70) if dark else LINE,width=2)
    c=(170,165,155) if dark else GREY
    d.text((M,H-95),"Peak Perspective Productions LLP  ×  Dynemech Systems Pvt. Ltd.  ·  India ITME 2026",font=I("Medium",26),fill=c)
    t=f"{n:02d}"; d.text((W-M-d.textlength(t,font=I("Bold",26)),H-95),t,font=I("Bold",26),fill=RED)
def kicker(d,t,y,col=RED): d.text((M,y),t,font=I("SemiBold",32),fill=col); return y+58
def head(d,lines,y,size=118,col=INK,maxw=None):
    for t in lines:
        h,_=anton_line(d,t,M,y,maxw or CW-200,col,size=size); y+=h+20
    d.rectangle((M,y+18,M+160,y+30),fill=RED); return y+76
def bullet(d,a,b,y,x=M,w=None,fa=36,fb=32,col=INK,bcol=GREY):
    w=w or (W-M-x)
    d.rectangle((x,y+15,x+14,y+29),fill=RED)
    yy=para(d,a,x+38,y,w-38,I("Bold",fa),fill=col,lh=1.3)
    if b: yy=para(d,b,x+38,yy+4,w-38,I("Regular",fb),fill=bcol)
    return yy+22
def photo(path,w,h):
    im=Image.open(path).convert("RGB"); r=max(w/im.width,h/im.height)
    im=im.resize((int(im.width*r)+1,int(im.height*r)+1),Image.LANCZOS)
    x=(im.width-w)//2; y=(im.height-h)//2; return im.crop((x,y,x+w,y+h))
def has(n): return os.path.exists(os.path.join(AS,n))
pages=[]

# ---------- 1 COVER
im,d=page(INK)
if has("hero.jpg"):
    ph=photo(os.path.join(AS,"hero.jpg"),W,1450); ph=ImageEnhance.Brightness(ph).enhance(0.8)
    im.paste(ph,(0,0))
    g=Image.new("L",(1,1450))
    for yy in range(1450): g.putpixel((0,yy),int(255*max(0,(yy-850)/600)**1.4))
    im.paste(Image.new("RGB",(W,1450),INK),(0,0),g.resize((W,1450)))
    top=Image.new("L",(1,300))
    for yy in range(300): top.putpixel((0,yy),int(200*(1-yy/300)))
    im.paste(Image.new("RGB",(W,300),INK),(0,0),top.resize((W,300)))
d=ImageDraw.Draw(im)
logo(im,M,M-30,150,on_dark=True)
d.text((W-M-d.textlength("CONTENT PROPOSAL",font=I("SemiBold",30)),M+20),"CONTENT PROPOSAL",font=I("SemiBold",30),fill=CREAM)
y=1260
d.text((M,y),"PREPARED FOR DYNEMECH SYSTEMS PVT. LTD.",font=I("SemiBold",32),fill=RED); y+=70
for t in ["ENGINEERED EQUILIBRIUM,","ON CAMERA."]:
    h,_=anton_line(d,t,M,y,CW,CREAM,size=150); y+=h+24
y+=20
y=para(d,"How we would turn Dynemech's stand at India ITME 2026 into films and reels that show buyers what your mounts do, and keep selling long after the show closes.",M,y,CW-150,I("Regular",38),fill=(225,218,205))
y=H-330
d.line([M,y,W-M,y],fill=(70,70,70),width=2); y+=40
cols=[("EVENT","India ITME 2026"),("DATES","4 – 9 Dec 2026"),("STAND","Hall 17 · Stall F2"),("FOR","Ms Kirti Singh")]
cw=CW//4
for i,(a,b) in enumerate(cols):
    d.text((M+i*cw,y),a,font=I("SemiBold",26),fill=RED); d.text((M+i*cw,y+44),b,font=I("Bold",32),fill=CREAM)
d.text((M,H-110),"Peak Perspective Productions LLP  ·  New Delhi  ·  16 November 2026",font=I("Medium",26),fill=(150,145,135))
pages.append(im)

# ---------- 2 WHAT WE UNDERSTOOD
im,d=page(); logo(im)
y=kicker(d,"01  ·  WHAT WE UNDERSTOOD",M)
y=head(d,["A PRODUCT YOU","CAN'T SEE WORKING."],y+10)
y=para(d,"Since 2000, Dynemech has built one of India's widest ranges of vibration-control products: wedge and levelling mounts, sandwich and shock mounts, air springs, machine base mounts and anti-vibration platforms, made at your units in Rai Industrial Area, Sonepat. Textile machinery is one of your core applications: your own customers credit Dynemech mounts with steadier spinning machines, higher productivity and lower maintenance.",M,y,CW,I("Regular",35))
y+=40
# waveform graphic
bx,by,bw,bh=M,y,CW,470
d.rounded_rectangle([bx,by,bx+bw,by+bh],radius=28,fill=INK)
d.text((bx+50,by+40),"WHAT THE BUYER NEVER SEES ON A STAND",font=I("SemiBold",28),fill=RED)
mid=by+bh//2+30; half=bw//2
def wave(x0,x1,amp,col,seed):
    pts=[]
    for x in range(x0,x1,3):
        t=(x-x0)/30.0
        v=amp*(math.sin(t*1.7)+0.55*math.sin(t*4.3+seed)+0.3*math.sin(t*9.1+2*seed))/1.85
        pts.append((x,mid+v))
    d.line(pts,fill=col,width=5)
wave(bx+60,bx+half-40,120,(230,90,85),1)
wave(bx+half+40,bx+bw-60,18,(120,215,190),2)
d.line([bx+half,by+100,bx+half,by+bh-40],fill=(80,80,80),width=2)
d.text((bx+60,by+bh-70),"Machine on the floor: vibration, noise, wear",font=I("Medium",26),fill=(200,195,185))
d.text((bx+half+40,by+bh-70),"On Dynemech mounts: steady, levelled, quiet",font=I("Medium",26),fill=(200,195,185))
d.text((bx+bw-300,by+bh+14),"Illustrative, not measured data",font=I("Regular",22),fill=GREY)
y=by+bh+70
y=kicker(d,"THE CHALLENGE AT ITME",y)
y=para(d,"ITME brings spinning, weaving and processing mill owners from across India and abroad to Greater Noida for six days. At Hall 17, Stall F2 they will see mounts and pads on a table, not a loom running steadier or a frame levelled in minutes. The benefit that wins the order is exactly the part a stand can't show.",M,y,CW,I("Regular",35))
y+=30
y=kicker(d,"OUR OBJECTIVE",y)
y=para(d,"Capture what Dynemech's engineers explain best, show the mounts in action wherever your stand allows it, and hand your sales team content they can send to every buyer they meet at ITME.",M,y,CW,I("Bold",35))
footer(d,2); pages.append(im)

# ---------- 3 CREATIVE IDEAS
im,d=page(); logo(im)
y=kicker(d,"02  ·  CREATIVE DIRECTION",M)
y=head(d,["FOUR IDEAS, BUILT","FOR YOUR STAND."],y+10)
if has("macro.jpg"):
    ph=photo(os.path.join(AS,"macro.jpg"),CW,560); im.paste(ph,(M,y)); d=ImageDraw.Draw(im)
    d.rectangle([M,y+560-70,M+620,y+560],fill=INK); d.text((M+30,y+560-55),"Concept visual: the product-film look we would aim for",font=I("Medium",24),fill=CREAM)
    y+=610
ideas=[("01","THE STEADY TEST","If a machine is running on your stand, we film the classic proof: a coin standing on edge or a full glass of water on the frame, on Dynemech mounts. A 15-second visual that needs no explanation and stops the scroll."),
("02","ENGINEER'S MINUTE","One mount, one minute. Your engineer explains a single product (a wedge mount, a levelling element, an air spring): where it goes, what problem it solves and on which machines. Ideal for WhatsApp follow-ups."),
("03","BUYERS' VOICE","Short conversations with mill owners and engineers who visit the stand: the vibration problems they face on the shop floor. Real buyers talking builds trust faster than any brochure (filmed only with consent)."),
("04","THE STAND STORY","A 60–90 second highlight film of Dynemech at ITME: the stand, the products, your team and the buyer traffic, cut for LinkedIn, YouTube and your website.")]
colw=(CW-60)//2
for i,(n,t,b) in enumerate(ideas):
    cx=M+(i%2)*(colw+60); cy=y+(i//2)*520
    d.rounded_rectangle([cx,cy,cx+colw,cy+480],radius=24,fill=SOFT)
    anton_line(d,n,cx+36,cy+30,200,RED,size=80)
    d.text((cx+150,cy+52),t,font=I("Bold",34),fill=INK)
    para(d,b,cx+36,cy+150,colw-72,I("Regular",31),fill=(60,58,55))
y+=2*520+30
y=kicker(d,"HOW ONE REEL COMES TOGETHER  ·  THE STEADY TEST",y)
frames=[("0–3 s","THE HOOK","A full glass on a running machine. Not a ripple."),
("3–10 s","THE REVEAL","Camera tilts down to the Dynemech mounts underneath."),
("10–25 s","THE WHY","Your engineer, in one line, on how the mount does it."),
("25–30 s","THE CALL","Hall 17 · Stall F2, and your logo.")]
fw=(CW-3*30)//4; fh=510
for i,(t,a,b) in enumerate(frames):
    fx=M+i*(fw+30)
    d.rounded_rectangle([fx,y,fx+fw,y+fh],radius=30,fill=INK)
    d.rounded_rectangle([fx+16,y+16,fx+fw-16,y+300],radius=18,fill=(46,46,48))
    cxm=fx+fw//2
    if i==0:
        d.rectangle([cxm-34,y+110,cxm+34,y+230],outline=CREAM,width=4); d.rectangle([cxm-30,y+140,cxm+30,y+226],fill=(90,170,200))
        d.rectangle([fx+40,y+230,fx+fw-40,y+262],fill=(120,124,130))
    elif i==1:
        d.rectangle([fx+40,y+90,fx+fw-40,y+150],fill=(120,124,130))
        for mx in (fx+60,fx+fw-120):
            d.rectangle([mx,y+150,mx+60,y+168],fill=(150,150,150)); d.rectangle([mx+6,y+168,mx+54,y+206],fill=RED); d.rectangle([mx,y+206,mx+60,y+222],fill=(40,40,40))
    elif i==2:
        d.ellipse([cxm-40,y+80,cxm+40,y+160],fill=(200,190,175)); d.rounded_rectangle([cxm-75,y+170,cxm+75,y+300],radius=40,fill=(200,190,175))
        d.rectangle([fx+30,y+236,fx+fw-30,y+270],fill=RED)
    else:
        lg=tile(110); im.paste(lg,(cxm-55,y+70),lg); d=ImageDraw.Draw(im)
        d.text((cxm-d.textlength("HALL 17 · F2",font=I("Bold",28))/2,y+215),"HALL 17 · F2",font=I("Bold",28),fill=CREAM)
    d.text((fx+28,y+318),t,font=I("SemiBold",24),fill=RED)
    d.text((fx+28,y+350),a,font=I("Bold",28),fill=CREAM)
    para(d,b,fx+28,y+390,fw-50,I("Regular",22),fill=(200,195,185),lh=1.35)
footer(d,3); pages.append(im)

# ---------- 4 HOW THE DAY RUNS
im,d=page(); logo(im)
y=kicker(d,"03  ·  ON THE GROUND",M)
y=head(d,["HOW A COVERAGE","DAY RUNS."],y+10)
if has("standplan.jpg"):
    sp=Image.open(os.path.join(AS,"standplan.jpg")); sp=sp.resize((int(sp.width*0.82),int(sp.height*0.82)))
    im.paste(sp,(M-40,y-10)); d=ImageDraw.Draw(im)
    lx2=M+sp.width-120; ly=y+30
    d.text((lx2,ly),"HALL 17 · STALL F2",font=I("SemiBold",26),fill=RED); ly+=50
    for n,t,dark in [("1","Product table: macro shots",False),("2","Demo machine (if running)",False),("3","Roaming camera: visitors",False),("4","Interview corner",True)]:
        d.ellipse([lx2,ly,lx2+40,ly+40],fill=INK if dark else RED); d.text((lx2+13,ly+4),n,font=I("Bold",26),fill=CREAM)
        d.text((lx2+56,ly+4),t,font=I("Medium",27),fill=INK); ly+=58
    d.text((lx2,ly+8),"Illustrative. We map your real stand",font=I("Regular",23),fill=GREY)
    d.text((lx2,ly+38),"on the discovery call.",font=I("Regular",23),fill=GREY)
    y+=int(sp.height)+10
# timeline
sched=[("09:30","Set-up","Crew in, lights and audio set, stand detail shots before visitors arrive"),
("10:30","Product films","Close-ups of mounts, pads and levelling elements; any live demo"),
("12:00","Engineer's Minute","Short on-camera explanations with your technical team"),
("14:00","Buyers' Voice","Visitor conversations and stand activity at peak footfall"),
("16:30","Leadership","A short interview with Dynemech's leadership on the brand"),
("18:00","Wrap and backup","Footage and photos backed up on two drives before we leave the hall")]
lx=M+190
d.line([lx,y+20,lx,y+len(sched)*128-60],fill=RED,width=4)
for i,(t,a,b) in enumerate(sched):
    yy=y+i*128
    d.text((M,yy),t,font=I("Bold",36),fill=INK)
    d.ellipse([lx-13,yy+10,lx+13,yy+36],fill=RED)
    d.text((lx+45,yy-2),a,font=I("Bold",34),fill=INK)
    d.text((lx+45,yy+46),b,font=I("Regular",28),fill=GREY)
y+=len(sched)*128+20
d.rounded_rectangle([M,y,W-M,y+250],radius=24,fill=INK)
d.text((M+50,y+36),"YOUR CREW ON THE DAY",font=I("SemiBold",28),fill=RED)
crew=["Director / producer","Cinema camera operator and photographer (Sony FX3)"]
for i,c in enumerate(crew):
    cx=M+50; cy=y+100+i*62
    d.rectangle([cx,cy+12,cx+12,cy+24],fill=RED); d.text((cx+30,cy),c,font=I("Medium",32),fill=CREAM)
footer(d,4); pages.append(im)

# ---------- 5 WHAT YOU GET + PROCESS
im,d=page(); logo(im)
y=kicker(d,"04  ·  WHAT YOU GET",M)
y=head(d,["CONTENT THAT","OUTLIVES THE SHOW."],y+10)
types=[("Stand highlight film","60–90 sec · 16:9 · website, YouTube, LinkedIn"),
("Reels","30–45 sec · 9:16 · Instagram, LinkedIn, YouTube Shorts"),
("Engineer explainers","45–60 sec · product by product · WhatsApp and sales emails"),
("Buyers' Voice cut","Short testimonial-style compilation (2-day package)"),
("Edited photographs","Stand, products, team and visitors, colour-graded")]
for a,b in types: y=bullet(d,a,b,y)
y+=20
y=kicker(d,"FROM YES TO DELIVERY",y)
steps=[("01","Confirm","Package chosen, 60% advance"),("02","Discovery call","20 min with your team; hero products and key messages"),("03","Shot list","Written plan for the day(s), approved by you"),("04","Coverage","Crew on your stand at ITME"),("05","Same day","Footage backed up on two drives"),("06","Within 5 working days","All final edits, one revision round included")]
sw=(CW-50)//3
for i,(n,a,b) in enumerate(steps):
    cx=M+(i%3)*(sw+25); cy=y+(i//3)*300
    d.rounded_rectangle([cx,cy,cx+sw,cy+270],radius=20,fill=SOFT)
    anton_line(d,n,cx+28,cy+22,120,RED,size=64)
    para(d,a,cx+28,cy+110,sw-56,I("Bold",32))
    para(d,b,cx+28,cy+160,sw-56,I("Regular",26),fill=GREY)
y+=620
y=kicker(d,"WHY PEAK PERSPECTIVE",y)
y=para(d,"One Delhi-NCR team handles creative, production and post-production under one roof, so the people who plan your shoot are the people who edit it. We handled media and social content at the Senior Asian Fencing Championship 2026 at Bharat Mandapam (35+ countries), where social reach grew from roughly 100K to 3.5M in about 12 days. Our work: www.peakperspectiveproductions.com",M,y,CW,I("Regular",32))
footer(d,5); pages.append(im)

# ---------- 6 INVESTMENT (last)
im,d=page(); logo(im)
y=kicker(d,"05  ·  INVESTMENT",M)
y=head(d,["CHOOSE YOUR","COVERAGE."],y+10)
pk=[("1-DAY COVERAGE","₹ 50,000","One full show day of your choice",
     ["6 creative assets","Professional headshots of your team present on the day","Full-day photography of the stand, products and visitors","All raw images handed over","A focused, complete option on its own"],False),
    ("2-DAY COVERAGE","₹ 80,000","Two show days of your choice",
     ["12 creative assets: edited videos and carousels","Buyers' Voice compilation within the edited videos","Full photography across both days","Full team photography and headshots","All raw images handed over"],True)]
pw=(CW-50)//2; ph_=980
for i,(t,p,s,items,rec) in enumerate(pk):
    cx=M+i*(pw+50); bg=INK if rec else SOFT; fg=CREAM if rec else INK; sub=(200,195,185) if rec else GREY
    d.rounded_rectangle([cx,y,cx+pw,y+ph_],radius=28,fill=bg)
    if rec:
        d.rounded_rectangle([cx+pw-300,y-24,cx+pw-36,y+30],radius=14,fill=RED)
        d.text((cx+pw-280,y-14),"RECOMMENDED",font=I("Bold",26),fill=CREAM)
    d.text((cx+44,y+56),t,font=I("SemiBold",30),fill=RED)
    d.text((cx+44,y+110),p,font=I("Bold",92),fill=fg)
    d.text((cx+44,y+235),"All-inclusive",font=I("Medium",28),fill=sub)
    d.text((cx+44,y+280),s,font=I("Medium",28),fill=sub)
    d.line([cx+44,y+345,cx+pw-44,y+345],fill=(80,80,80) if rec else LINE,width=2)
    yy=y+380
    for j,it in enumerate(items):
        f=I("Bold",32) if j==0 else I("Regular",30)
        d.rectangle([cx+44,yy+14,cx+56,yy+26],fill=RED)
        yy=para(d,it,cx+76,yy,pw-120,f,fill=fg,lh=1.3)+18
y+=ph_+60
y=kicker(d,"BOTH PACKAGES INCLUDE",y)
y=para(d,"Discovery call and written shot list · director and a cinema camera operator who also handles all photography · equipment (Sony FX3, gimbal, wireless audio, lighting) · travel to India Expo Centre & Mart · editing, colour, captions and licensed music · one revision round · final files in every format you need. No additional taxes.",M,y,CW,I("Regular",31))
y+=24
y=kicker(d,"PAYMENT",y)
y=para(d,"60% advance on confirmation · 40% on delivery of final edits.",M,y,CW,I("Regular",31))
y+=40
d.rectangle((M,y,M+160,y+12),fill=RED); y+=40
d.text((M,y),"To confirm your package, reply to this email or call +91 98738 77010.",font=I("Bold",34),fill=INK); y+=64
d.text((M,y),"Shiven Kumar  ·  Founder, Peak Perspective Productions LLP  ·  www.peakperspectiveproductions.com",font=I("Medium",28),fill=GREY)
footer(d,6); pages.append(im)

out=os.path.join(HERE_C,"Peak_Perspective_Proposal_Dynemech_ITME_2026.pdf")
pages[0].save(out,save_all=True,append_images=pages[1:],resolution=200)
for i,p in enumerate(pages): p.resize((551,780)).save(f"/tmp/claude-0/dp_{i}.png")
s=Image.new("RGB",(551*3,780*2),"white")
for i in range(len(pages)): s.paste(Image.open(f"/tmp/claude-0/dp_{i}.png"),((i%3)*551,(i//3)*780))
s.save("/tmp/claude-0/dp_sheet.png"); print(out)
