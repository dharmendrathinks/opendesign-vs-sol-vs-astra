from PIL import Image
from collections import deque
im=Image.open('source-screen.png').convert('RGBA')
# Coordinates are in the target 393 x 852 CSS-pixel space. Only artwork is cropped.
def crop(name,box,kind):
    box=tuple(round(v*3) for v in box)
    out=im.crop(box); p=out.load(); w,h=out.size
    def background(x,y):
        r,g,b,a=p[x,y]
        if kind=='blue': return 65<r<157 and 120<g<194 and 170<b<240 and 27<g-r<73 and 25<b-g<75
        return r>140 and g>218 and b>211 and g-r>12 and abs(g-b)<30
    q=deque()
    for x in range(w):
        if background(x,0): q.append((x,0))
        if background(x,h-1): q.append((x,h-1))
    for y in range(h):
        if background(0,y): q.append((0,y))
        if background(w-1,y): q.append((w-1,y))
    seen=set(q)
    while q:
        x,y=q.popleft();p[x,y]=(0,0,0,0)
        for xx,yy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 0<=xx<w and 0<=yy<h and (xx,yy) not in seen and background(xx,yy):
                seen.add((xx,yy));q.append((xx,yy))
    out.save('assets/'+name+'.png')
crop('rudraksha',(23,616,118,692),'blue')
crop('prasad',(149,494,251,568),'blue')
crop('costume',(272,492,377,568),'blue')
crop('fasting',(149,619,246,694),'blue')
crop('temple',(270,619,379,693),'blue')
crop('krishna',(255,359,393,448),'aqua')
crop('peacock-feather',(216,372,267,415),'aqua')
