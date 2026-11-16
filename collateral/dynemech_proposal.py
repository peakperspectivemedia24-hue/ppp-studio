import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","brand-kit"))
from brand import *
from PIL import Image, ImageDraw
PRICE=os.environ.get("PRICE","")   # e.g. "45,000"
W,H=1654,2339; M=120
def page():
    im=Image.new("RGB",(W,H),CREAM); return im,ImageDraw.Draw(im)
def para(d,t,x,y,w,f,fill=INK,lh=1.45):
    for ln in wrap(d,t,f,w):
        d.text((x,y),ln,font=f,fill=fill); y+=int(f.size*lh)
    return y
def logo(im):
    lg=Image.open(os.path.join(HERE,"logo.jpg")).convert("RGB"); r=190/lg.height
    lg=lg.resize((int(lg.width*r),190)); im.paste(lg,(W-M-lg.width,M-20))
def footer(d,n):
    d.rectangle((0,H-110,W,H),fill=INK)
    d.text((M,H-78),"Peak Perspective Productions LLP  ·  RK Puram, New Delhi  ·  info@peakperspectiveproductions.com  ·  +91 98738 77010",font=I("Medium",26),fill=CREAM)
def label(d,t,y): d.text((M,y),t,font=I("SemiBold",34),fill=RED); return y+64
def bullet(d,a,b,y,x=M):
    d.rectangle((x,y+16,x+14,y+30),fill=RED)
    d.text((x+40,y),a,font=I("Bold",37),fill=INK); y+=52
    if b: y=para(d,b,x+40,y,W-x-M-40,I("Regular",33))
    return y+20
pages=[]
# ---------- page 1
im,d=page(); logo(im)
d.text((M,M),"PROPOSAL  ·  INDIA ITME 2026",font=I("SemiBold",34),fill=RED)
d.text((M,M+52),"Prepared for Dynemech Systems Pvt. Ltd.",font=I("Medium",34),fill=INK)
y=M+150
for t in ["MAKE VIBRATION","CONTROL VISIBLE","AT ITME."]:
    h,_=anton_line(d,t,M,y,W-2*M-240,INK,size=128); y+=h+22
d.rectangle((M,y+20,M+160,y+32),fill=RED); y+=80
y=label(d,"THE CHALLENGE",y)
y=para(d,"An anti-vibration mount is one of the hardest products to sell from a stand. A visiting mill owner sees a rubber-and-steel part on a table. What it actually does, a machine levelled in minutes, running steadier and quieter, with less load passed into the floor, only shows when it is installed and running. A brochure lists those benefits; it doesn't let the buyer see them.",M,y,W-2*M,I("Regular",37))
y+=40
y=label(d,"OUR APPROACH",y)
y=para(d,"We cover one full day of India ITME at Hall 17, Stall F2 with a crew that films your products, your demonstrations and your conversations with buyers. Your engineers explain the mounts on camera, and we cut it into a stand highlight film, short reels and product clips your sales team can keep sending to buyers long after the show closes.",M,y,W-2*M,I("Regular",37))
y+=50
d.rectangle((M,y,W-M,y+300),fill=INK)
rows=[("Event","India ITME 2026, India Expo Centre & Mart, Greater Noida"),("Show dates","4 – 9 December 2026"),("Your stand","Hall 17, Stall F2"),("Coverage","One full show day of your choice")]
yy=y+40
for a,b in rows:
    d.text((M+50,yy),a.upper(),font=I("SemiBold",28),fill=RED); d.text((M+380,yy-4),b,font=I("Medium",33),fill=CREAM); yy+=60
footer(d,1); pages.append(im)
# ---------- page 2
im,d=page(); logo(im)
d.text((M,M),"SCOPE OF WORK",font=I("SemiBold",34),fill=RED)
y=M+70
for t in ["ONE DAY.","EVERYTHING YOU NEED."]:
    h,_=anton_line(d,t,M,y,W-2*M-240,INK,size=110); y+=h+22
d.rectangle((M,y+20,M+160,y+32),fill=RED); y+=80
y=label(d,"BEFORE THE SHOW",y)
y=bullet(d,"Discovery call and shot list","A 20-minute call with your team on products, hero items and key messages, followed by a written shot list and plan for the day, shared for your approval.",y)
y+=10
y=label(d,"ON THE DAY",y)
y=bullet(d,"Professional crew on the stand","Director, cinema cameraman (Sony FX3), photographer and an on-site editor, with gimbal, wireless mics and lighting.",y)
y=bullet(d,"Product and demonstration filming","Close-ups of mounts, pads and levelling elements, plus any live demonstration you run at the stand.",y)
y=bullet(d,"Engineer and leadership interviews","Short on-camera explanations of how the mounts work and where they are used.",y)
y=bullet(d,"Buyer moments","Visitor conversations and stand activity through the day (with visitors' consent).",y)
y+=10
y=label(d,"DELIVERABLES",y)
dl=[("1 stand highlight film","60–90 seconds, for your website, YouTube and LinkedIn."),
("4 short reels (9:16)","One delivered the same evening; three within 5 working days."),
("2 product explainer clips","An engineer explaining the mounts, for WhatsApp and sales follow-ups."),
("30 edited photographs","Stand, products, team and visitor moments.")]
for a,b in dl: y=bullet(d,a,b,y)
footer(d,2); pages.append(im)
# ---------- page 3
im,d=page(); logo(im)
d.text((M,M),"INVESTMENT & NEXT STEPS",font=I("SemiBold",34),fill=RED)
y=M+70
h,_=anton_line(d,"THE INVESTMENT",M,y,W-2*M-240,INK,size=110); y+=h+40
d.rectangle((M,y,W-M,y+300),fill=INK)
d.text((M+50,y+40),"ONE-DAY ITME COVERAGE  ·  ALL-INCLUSIVE",font=I("SemiBold",30),fill=RED)
amt=f"₹ {PRICE}" if PRICE else "₹ ________"
d.text((M+50,y+90),amt,font=I("Bold",100),fill=CREAM)
d.text((M+50,y+232),"Crew, equipment, travel to Greater Noida, editing and all deliverables listed. No additional taxes.",font=I("Medium",28),fill=CREAM)
y+=360
y=label(d,"PAYMENT",y)
y=bullet(d,"60% advance on confirmation",None,y)
y=bullet(d,"40% balance on delivery of final edits",None,y)
y+=10
y=label(d,"TIMELINE",y)
y=bullet(d,"Discovery call and shot list","Within 2 days of confirmation.",y)
y=bullet(d,"Same-day reel","Delivered on the evening of your coverage day.",y)
y=bullet(d,"All final deliverables","Within 5 working days of the coverage day, with one round of revisions included.",y)
y+=10
y=label(d,"WHY PEAK PERSPECTIVE",y)
y=para(d,"We are a Delhi-NCR team that handles creative, production and post-production under one roof. We handled media and social content at the Senior Asian Fencing Championship 2026 at Bharat Mandapam (35+ countries), where social reach grew from roughly 100K to 3.5M in about 12 days.",M,y,W-2*M,I("Regular",34))
y+=40
d.rectangle((M,y,M+160,y+12),fill=RED); y+=40
d.text((M,y),"To confirm, reply to this email or call +91 98738 77010.",font=I("Bold",36),fill=INK); y+=70
d.text((M,y),"Shiven Kumar  ·  Founder, Peak Perspective Productions LLP",font=I("Medium",33),fill=INK)
d.text((M,y+50),"www.peakperspectiveproductions.com",font=I("Medium",33),fill=RED)
footer(d,3); pages.append(im)
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"Peak_Perspective_Proposal_Dynemech_ITME_2026.pdf")
pages[0].save(out,save_all=True,append_images=pages[1:],resolution=200)
for i,p in enumerate(pages): p.resize((551,780)).save(f"/tmp/claude-0/dp_{i}.png")
s=Image.new("RGB",(551*3,780),"white")
for i in range(3): s.paste(Image.open(f"/tmp/claude-0/dp_{i}.png"),(i*551,0))
s.save("/tmp/claude-0/dp_sheet.png"); print(out)
