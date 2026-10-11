import numpy as np, wave
SR=44100; DUR=20.0; N=int(SR*DUR); rng=np.random.default_rng(11)
out=np.zeros(N)
def add(sig,t0,g=1.0):
    i=int(t0*SR); n=min(len(sig),N-i)
    if n>0 and i>=0: out[i:i+n]+=sig[:n]*g
def noise(n): return rng.standard_normal(n)
def kick():
    t=np.arange(int(0.3*SR))/SR; f=48+120*np.exp(-t*30); ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*np.exp(-t*8.5)
def clap():
    t=np.arange(int(0.2*SR))/SR; n=np.diff(noise(len(t)),prepend=0); return n*np.exp(-t*26)*0.5
def hat(o=False):
    L=0.12 if o else 0.045; t=np.arange(int(L*SR))/SR; n=np.diff(noise(len(t)),prepend=0); return n*np.exp(-t*(40 if o else 95))*0.22
def bass(f,dur):
    t=np.arange(int(dur*SR))/SR; return np.tanh(2.4*np.sin(2*np.pi*f*t))*np.exp(-t*3.2)*0.42
def boom(L=1.2):
    t=np.arange(int(L*SR))/SR; return (np.sin(2*np.pi*36*t)*np.exp(-t*2.8)+0.35*np.diff(noise(len(t)),prepend=0)*np.exp(-t*9))*1.0
def tick(f=1500):
    t=np.arange(int(0.07*SR))/SR; return np.sin(2*np.pi*f*t)*np.exp(-t*55)*0.7
def whoosh(L):
    n=int(L*SR); t=np.arange(n)/SR; x=noise(n); y=np.zeros(n); a=0.02; 
    for i in range(1,n):
        c=0.02+0.5*(i/n)**2; y[i]=y[i-1]+c*(x[i]-y[i-1])
    return y*np.sin(np.pi*np.clip(t/L,0,1))**1.5*1.4
def riser(L,f0,f1,g):
    n=int(L*SR); t=np.arange(n)/SR; f=f0+(f1-f0)*(t/L)**2; ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*(t/L)**1.5*g
beat=0.5
notes=[55,55,65.4,49,55,55,73.4,49]
for b in range(int(DUR/beat)):
    t0=b*beat
    if t0>=1.0:
        add(kick(),t0,0.95)
        if b%2==1: add(clap(),t0,0.7)
        add(hat(),t0+0.25,0.8)
        if b%4==3: add(hat(True),t0+0.25,0.6)
    if t0>=5.0 and not (14.0<=t0<17.0 and False): add(bass(notes[b%8],0.5),t0,0.8)
add(boom(),0.0,0.9); add(boom(),1.0,0.5)
for tt,f in ((1.0,1500),(1.5,1500),(2.0,2000)): add(tick(f),tt,0.8)
add(whoosh(2.0),2.5,0.9)
add(boom(),4.5,0.7)
add(boom(1.4),9.0,0.95)
add(riser(2.0,300,1400,0.18),9.5)
add(boom(1.4),11.5,1.0)
add(boom(),14.0,0.6); add(boom(1.6),17.0,1.0)
add(riser(1.0,200,1600,0.2),16.0)
out=np.tanh(out*0.9)
fade=np.ones(N); k=int(0.6*SR); fade[-k:]=np.linspace(1,0,k); out*=fade
out=out/np.max(np.abs(out))*0.89
w=wave.open("out/beat3.wav","wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((out*32767).astype(np.int16).tobytes()); w.close(); print("audio3 ok")
