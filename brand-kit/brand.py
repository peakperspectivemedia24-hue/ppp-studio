from PIL import Image, ImageDraw, ImageFont
import numpy as np, math
from functools import lru_cache
CREAM=(252,243,228); INK=(26,26,26); RED=(198,35,40)
ANTON="/home/claude/brand/node_modules/@fontsource/anton/files/anton-latin-400-normal.woff"
INTER="/usr/share/fonts/opentype/inter/Inter-%s.otf"
@lru_cache(maxsize=None)
def A(s): return ImageFont.truetype(ANTON,int(s))
@lru_cache(maxsize=None)
def I(w,s): return ImageFont.truetype(INTER%w,int(s))
def ease(x): x=max(0,min(1,x)); return 1-(1-x)**3
def lerp(a,b,t): return a+(b-a)*t
def ink(d,t,f): return d.textbbox((0,0),t,font=f)
_SC=ImageDraw.Draw(Image.new("RGB",(10,10)))
def fit_size(d,t,w,maxs=2000): return _fit(t,w,maxs)
@lru_cache(maxsize=None)
def _fit(t,w,maxs):
    lo,hi=10,maxs
    while lo<hi-1:
        m=(lo+hi)//2; b=ink(_SC,t,A(m))
        if b[2]-b[0]<=w: lo=m
        else: hi=m
    return lo
def anton_line(d,t,x,y,w,fill,size=None,align="left"):
    s=size or fit_size(d,t,w); f=A(s); b=ink(d,t,f); tw_=b[2]-b[0]; th=b[3]-b[1]
    xx=x if align=="left" else x+(w-tw_)//2 if align=="center" else x+w-tw_
    d.text((xx-b[0],y-b[1]),t,font=f,fill=fill)
    return th,s
def wrap(d,t,f,maxw):
    out=[];cur=""
    for w in t.split():
        x=(cur+" "+w).strip()
        if ink(d,x,f)[2]<=maxw: cur=x
        else: out.append(cur);cur=w
    if cur: out.append(cur)
    return out
# --- logo mark -------------------------------------------------
_src=np.asarray(Image.open("/home/claude/brand/logo.jpg").convert("RGB")).astype(float)
_bg=np.array([252,243,228.])
_dist=np.sqrt(((_src-_bg)**2).sum(2))
_alpha=np.clip((_dist-30)/70,0,1)
_isred=((_src[...,0]-_src[...,2])>55)
ys,xs=np.where(_alpha>0.5); _BB=(xs.min()-6,ys.min()-6,xs.max()+6,ys.max()+6)
def mark(height,body=INK,accent=RED):
    h,w=_alpha.shape
    out=np.zeros((h,w,4),np.uint8)
    for m,c in ((~_isred,body),(_isred,accent)):
        out[...,0][m]=c[0];out[...,1][m]=c[1];out[...,2][m]=c[2]
    out[...,3]=(_alpha*255).astype(np.uint8)
    im=Image.fromarray(out,"RGBA").crop(_BB)
    r=height/im.size[1]
    return im.resize((int(im.size[0]*r),height),Image.LANCZOS)
def arc(d,cx,cy,r,th,start,end,fill):
    d.arc([cx-r,cy-r,cx+r,cy+r],start,end,fill=fill,width=th)

def tile(h,pad=0.2):
    t=Image.new("RGBA",(int(h*0.86),h),(0,0,0,0)); d=ImageDraw.Draw(t)
    d.rounded_rectangle([0,0,t.size[0]-1,h-1],radius=int(h*0.14),fill=CREAM+(255,))
    m=mark(int(h*(1-2*pad))); t.paste(m,((t.size[0]-m.size[0])//2,(h-m.size[1])//2),m); return t
