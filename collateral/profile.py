import sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","brand-kit"))
from brand import *
from PIL import Image, ImageDraw
W,H=1654,2339; M=120
def page():
    im=Image.new("RGB",(W,H),CREAM); return im,ImageDraw.Draw(im)
def para(d,t,x,y,w,f,fill=INK,lh=1.45):
    for ln in wrap(d,t,f,w):
        d.text((x,y),ln,font=f,fill=fill); y+=int(f.size*lh)
    return y
def logo(im):
    lg=Image.open(os.path.join(HERE,"logo.jpg")).convert("RGB"); r=200/lg.height
    lg=lg.resize((int(lg.width*r),200)); im.paste(lg,(W-M-lg.width,M-20))
def footer(d):
    d.rectangle((0,H-110,W,H),fill=INK)
    d.text((M,H-78),"Peak Perspective Productions LLP  ·  Delhi-NCR  ·  info@peakperspectiveproductions.com  ·  +91 98738 77010",font=I("Medium",27),fill=CREAM)
# page 1
im,d=page(); logo(im)
d.text((M,M),"COMPANY PROFILE",font=I("SemiBold",34),fill=RED)
y=M+70
for t in ["WE MAKE WHAT YOU","SELL UNDERSTOOD."]:
    h,_=anton_line(d,t,M,y,W-2*M-260,INK,size=120); y+=h+24
d.rectangle((M,y+20,M+160,y+32),fill=RED); y+=80
y=para(d,"Peak Perspective Productions LLP is a Delhi-NCR digital marketing and media production company. We plan, shoot and deliver full campaigns under one roof: film, photography, social media, print and concept-led AI-assisted ad films. For exhibitors, that means content that keeps working long after the show closes.",M,y,W-2*M,I("Regular",40))
y+=50
d.text((M,y),"WHAT WE DO",font=I("SemiBold",34),fill=RED); y+=70
svc=[("Exhibition & event coverage","Multi-camera video, photography, same-day reels and a highlight film."),
("Product & machine films","Process, cycle and application films that explain what a sample cannot."),
("Corporate & founder films","Leadership interviews and factory stories for buyers and investors."),
("Social media & digital","Reels, carousels, LinkedIn content and campaign management."),
("Print & creative design","Brochures, catalogues and booth creatives in one visual language."),
("AI-assisted ad films","Concept-led films where AI genuinely serves the idea.")]
for a,b in svc:
    d.rectangle((M,y+14,M+14,y+28),fill=RED)
    d.text((M+40,y),a,font=I("Bold",38),fill=INK); y+=52
    y=para(d,b,M+40,y,W-2*M-40,I("Regular",34))+22
y+=30
d.rectangle((M,y,W-M,y+370),fill=INK)
d.text((M+50,y+40),"RECENT WORK",font=I("SemiBold",32),fill=RED)
anton_line(d,"100K TO 3.5M SOCIAL REACH IN 12 DAYS",M+50,y+100,W-2*M-100,CREAM,size=74)
para(d,"Senior Asian Fencing Championship 2026, Bharat Mandapam, New Delhi (35+ countries): media production and social content. Our result on one event, not a guarantee.",M+50,y+200,W-2*M-100,I("Regular",32),fill=CREAM)
footer(d); p1=im
# page 2
im,d=page(); logo(im)
d.text((M,M),"PREPARED FOR ARETE 22 LTD.  ·  ALUCAST 2026",font=I("SemiBold",34),fill=RED)
y=M+70
for t in ["THREE IDEAS FOR","ARETE AT ALUCAST"]:
    h,_=anton_line(d,t,M,y,W-2*M-260,INK,size=110); y+=h+24
d.rectangle((M,y+20,M+160,y+32),fill=RED); y+=80
ideas=[("01","WHEEL-TO-FACTORY FILM (60–90 sec)","Before the show, we film one wheel's journey in your plant: casting, heat treatment, machining, painting and testing, with your engineer explaining each stage. It plays on loop at the stand and becomes the film your sales team sends to OEM buyers afterwards."),
("02","THE TEST BENCH SERIES (reels)","Short vertical clips of your quality checks, such as impact, radial fatigue and X-ray inspection, each answering one buyer question. They are posted before ALUCAST to bring visitors to the stand, then reused in follow-up emails."),
("03","ON-GROUND COVERAGE + SAME-DAY CONTENT","Photo and video at your stand across 10–12 December: product close-ups, visitor conversations and a leadership interview, with reels delivered the same day for LinkedIn and a highlight film after the show.")]
for n,t,b in ideas:
    anton_line(d,n,M,y,200,RED,size=110)
    d.text((M+200,y+8),t,font=I("Bold",40),fill=INK)
    y=para(d,b,M+200,y+70,W-2*M-200,I("Regular",35))+60
y+=10
d.text((M,y),"HOW WE WORK",font=I("SemiBold",34),fill=RED); y+=64
y=para(d,"A short call to understand which buyers you want to meet at ALUCAST → a written scope with deliverables and timeline → pre-show shoot at your plant → show coverage → edits delivered. One team handles all of it.",M,y,W-2*M,I("Regular",35))
y+=50
d.rectangle((M,y,W-M,y+200),fill=RED)
anton_line(d,"LET'S TALK THIS WEEK",M+50,y+40,W-2*M-100,CREAM,size=70)
d.text((M+50,y+130),"Shiven Kumar, Founder  ·  +91 98738 77010  ·  info@peakperspectiveproductions.com",font=I("Medium",32),fill=CREAM)
footer(d)
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"Peak_Perspective_Productions_Profile_Arete_ALUCAST.pdf")
p1.save(out,save_all=True,append_images=[im],resolution=200)
p1.save("/tmp/p1.png"); im.save("/tmp/p2.png"); print(out)
