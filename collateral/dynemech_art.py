import sys,os,math
HERE_C=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,os.path.join(HERE_C,"..","brand-kit"))
from brand import *
from PIL import Image, ImageDraw, ImageFilter
AS=os.path.join(HERE_C,"dynemech_assets"); os.makedirs(AS,exist_ok=True)
S=2  # supersample
def iso(x,y,z,ox,oy,k):  # isometric projection
    return (ox+(x-y)*math.cos(math.radians(30))*k, oy+(x+y)*math.sin(math.radians(30))*k - z*k)
def shade(c,f): return tuple(max(0,min(255,int(v*f))) for v in c)
def box(d,x,y,z,w,l,h,col,P,edge=None):
    p=lambda a,b,c:P(a,b,c)
    top=[p(x,y,z+h),p(x+w,y,z+h),p(x+w,y+l,z+h),p(x,y+l,z+h)]
    left=[p(x,y+l,z),p(x+w,y+l,z),p(x+w,y+l,z+h),p(x,y+l,z+h)]
    right=[p(x+w,y,z),p(x+w,y+l,z),p(x+w,y+l,z+h),p(x+w,y,z+h)]
    d.polygon(right,fill=shade(col,0.72)); d.polygon(left,fill=shade(col,0.88)); d.polygon(top,fill=col)
    if edge:
        for poly in (top,left,right): d.line(poly+[poly[0]],fill=edge,width=2*S)
# ---------- HERO: textile machine on Dynemech-style mounts, dark bg
W,H=1654*S,1450*S
im=Image.new("RGB",(W,H),(18,18,18)); d=ImageDraw.Draw(im)
# floor glow
g=Image.new("RGB",(W,H),(0,0,0)); gd=ImageDraw.Draw(g)
gd.ellipse([W*0.12,H*0.48,W*0.95,H*1.02],fill=(70,32,30)); g=g.filter(ImageFilter.GaussianBlur(160*S))
im=Image.blend(im,Image.composite(g,im,Image.new("L",(W,H),255)),0.9); d=ImageDraw.Draw(im)
ox,oy,k=W*0.50,H*0.36,4.9*S
P=lambda x,y,z:iso(x,y,z,ox,oy,k)
# floor grid
for i in range(-60,221,20):
    d.line([P(i,-60,0),P(i,220,0)],fill=(45,40,38),width=1*S); d.line([P(-60,i,0),P(220,i,0)],fill=(45,40,38),width=1*S)
# mounts (4) under machine
mounts=[(0,0),(140,0),(0,60),(140,60)]
for mx,my in mounts:
    box(d,mx-6,my-6,0,22,22,4,(40,40,40),P)            # base plate
    box(d,mx-4,my-4,4,18,18,6,(200,35,40),P)           # red elastomer
    box(d,mx-6,my-6,10,22,22,3,(150,150,150),P)        # top plate
    box(d,mx+3,my+3,13,4,4,6,(190,190,190),P)          # stud
# machine body: long frame
box(d,-8,-8,19,170,86,6,(70,72,76),P,edge=(30,30,30))
box(d,0,0,25,154,70,48,(232,224,210),P,edge=(120,112,100))
box(d,0,0,73,154,70,4,(60,60,62),P)
# spindles row on top
for i in range(10):
    for j in (12,46):
        box(d,8+i*14.5,j,77,7,7,22,(200,195,185),P)
        box(d,8+i*14.5,j,99,7,7,6,(198,35,40),P)
# control panel
box(d,154,10,30,8,30,36,(35,35,38),P)
pts=[P(162,14,58),P(162,36,58),P(162,36,40),P(162,14,40)]; d.polygon(pts,fill=(60,180,160))
# stability waves (subtle red arcs left of machine)
cx,cy=P(-30,30,40)
for r,a in ((60,160),(95,110),(130,60)):
    rr=r*S; d.arc([cx-rr,cy-rr,cx+rr,cy+rr],100,260,fill=(198,35,40,),width=4*S)
cx,cy=P(160,110,10)
im=im.resize((W//S,H//S),Image.LANCZOS); im.save(os.path.join(AS,"hero.jpg"),quality=94)
# ---------- STAND PLAN: Hall 17 Stall F2, isometric, cream bg
W,H=1414*S,700*S
im=Image.new("RGB",(W,H),(252,243,228)); d=ImageDraw.Draw(im)
ox,oy,k=W*0.42,H*0.24,5.0*S
P=lambda x,y,z:iso(x,y,z,ox,oy,k)
box(d,0,0,0,100,70,2,(205,195,178),P)        # floor
box(d,0,-2,2,100,2,40,(250,246,238),P,edge=(200,190,175))   # back wall
box(d,-2,0,2,2,70,40,(245,240,230),P,edge=(200,190,175))    # side wall
d.text(P(30,0,36),"",fill=INK)
box(d,10,10,2,30,16,14,(26,26,26),P)          # display table
for i in range(4): box(d,13+i*7,14,16,4,4,3,(198,35,40),P)  # mounts on table
box(d,55,8,2,34,22,10,(220,214,200),P,edge=(160,150,135))  # demo machine plinth
box(d,58,11,12,28,16,16,(120,124,130),P)      # demo machine
box(d,15,45,2,18,10,16,(198,35,40),P)         # counter
# cameras
def cam(x,y,n,col=(198,35,40)):
    cx,cy=P(x,y,8); r=30*S
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=col,outline=(255,255,255),width=4*S)
    f=I("Bold",34*S); tw=d.textlength(str(n),font=f); d.text((cx-tw/2,cy-24*S),str(n),font=f,fill=(255,255,255))
cam(30,62,1); cam(92,30,2); cam(70,62,3); cam(-14,30,4,(26,26,26))
im=im.resize((W//S,H//S),Image.LANCZOS); im.save(os.path.join(AS,"standplan.jpg"),quality=94)
print("ok")
