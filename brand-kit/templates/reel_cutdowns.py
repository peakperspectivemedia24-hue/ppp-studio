import sys,subprocess,os
sys.path.insert(0,"/home/claude/ppp-studio/brand-kit")
import reel3 as R
from brand import *
W,H,FPS,DUR=1080,1920,30,20.0
new,stack_center,punch=R.new,R.stack_center,R.punch
def sub(d,t,y,fill,size=46):
    f=I("Bold",size); b=ink(d,t,f); d.text(((W-b[2])//2,y),t,font=f,fill=fill)
SHOTS=[("THE HERO FILM","wide, for your website and YouTube"),("VERTICAL CUTS","9:16 reels, framed on the day"),("THE STILLS","photographed alongside, not screenshots"),("THE LOOP","a silent 10-second clip for stall screens")]
def frame(t):
    if t<1.3:
        im,d=new(INK); stack_center(d,[("ONE SHOOT.",None),("MANY USES.",None)],[CREAM,RED],punch(t))
    elif t<3.3:
        im,d=new(CREAM); lt=t-1.3; stack_center(d,[("PLAN THEM",None),("BEFORE WE ROLL.",None)],[INK,RED],punch(lt)*0.8)
    elif t<15.3:
        i=int((t-3.3)//3.0); lt=(t-3.3)-i*3.0
        bg,fg,ac=[(INK,CREAM,RED),(CREAM,INK,RED),(RED,CREAM,INK),(INK,CREAM,RED)][i]
        im,d=new(bg); h,s=SHOTS[i]
        f=A(260); b=ink(d,f"0{i+1}",f); d.text(((W-b[2])//2-b[0],330),f"0{i+1}",font=f,fill=ac)
        y=stack_center(d,[(h,None)],[fg],punch(lt,0.2,0.12),yoff=60)
        if lt>0.5: sub(d,s,y+40,fg,44)
        d.rectangle([R.M,H-260,R.M+int((W-2*R.M)*min(1,lt/3.0)),H-248],fill=ac)
    elif t<17.3:
        im,d=new(CREAM); lt=t-15.3; stack_center(d,[("TELL US WHERE",None),("IT WILL LIVE.",None)],[INK,RED],punch(lt))
    else:
        im,d=new(CREAM); lt=t-17.3
        k=ease(lt/0.4); m=mark(int(lerp(220,400,k))); im.paste(m,((W-m.size[0])//2,260),m)
        d=ImageDraw.Draw(im)
        y=stack_center(d,[("CORPORATE FILMS",None)],[INK],punch(lt,0.2,0.08)*0.8,yoff=200)
        d.rectangle([R.M,y+60,W-R.M,y+200],fill=RED); f=I("Bold",58); l="DM us  ·  +91 98738 77010"; b=ink(d,l,f); d.text(((W-b[2])//2,y+130-b[3]//2-4),l,font=f,fill=CREAM)
        sub(d,"Peak Perspective Productions LLP",y+250,INK,32)
    return im
out="/home/claude/ppp-studio/media/reels/marketing-cutdowns-v1/"; os.makedirs(out,exist_ok=True)
cmd=["ffmpeg","-y","-loglevel","error","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-","-i","/home/claude/ppp-studio/brand-kit/out/beat3.wav","-c:v","libx264","-pix_fmt","yuv420p","-crf","18","-preset","medium","-c:a","aac","-b:a","192k","-t",str(DUR),"-movflags","+faststart",out+"reel.mp4"]
p=subprocess.Popen(cmd,stdin=subprocess.PIPE)
for n in range(int(DUR*FPS)): p.stdin.write(frame(n/FPS).tobytes())
p.stdin.close(); p.wait()
for i,tt in enumerate([0.6,2.2,4.5,7.5,10.5,13.5,16.0,18.8]): frame(tt).resize((270,480)).save(f"/tmp/claude-0/rf_{i}.png")
from PIL import Image
s=Image.new("RGB",(270*4,480*2))
for i in range(8): s.paste(Image.open(f"/tmp/claude-0/rf_{i}.png"),((i%4)*270,(i//4)*480))
s.save("/tmp/claude-0/reel_sheet.png"); print("reel ok")
