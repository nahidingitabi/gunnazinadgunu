#!/usr/bin/env python3
"""Find frames where the puzzle cards are largest: detect white card blobs
(b*<16 & L>135) and report the biggest single blob per frame."""
import sys,cv2,numpy as np,json,glob
U='/root/.claude/uploads/84fa90fa-750b-5180-b6a9-f390607e1640'
cm=json.load(open('clipmap.json'))
CID=sys.argv[1]; STEP=float(sys.argv[2]) if len(sys.argv)>2 else 0.5
src=glob.glob(f'{U}/{CID}*')[0]; off=cm[CID]['offset']; dur=cm[CID]['dur']
cap=cv2.VideoCapture(src); fps=cap.get(cv2.CAP_PROP_FPS)
n=int(cap.get(cv2.CAP_PROP_FRAME_COUNT)); step=max(1,int(round(STEP*fps)))
res=[]; fn=0
while fn<n:
    cap.set(cv2.CAP_PROP_POS_FRAMES,fn); ok,fr=cap.read()
    if not ok: break
    lab=cv2.cvtColor(fr,cv2.COLOR_BGR2LAB)
    m=((lab[:,:,2].astype(np.int16)-128<16)&(lab[:,:,0]>135)).astype(np.uint8)
    m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    nn,lb,st,ce=cv2.connectedComponentsWithStats(m,8)
    good=[(int(st[k,4]),int(ce[k][0]),int(ce[k][1])) for k in range(1,nn)
          if 400<st[k,4]<9000 and 0.25<st[k,2]/max(st[k,3],1)<4.0]
    if good:
        good.sort(reverse=True)
        res.append((good[0][0],round(off+fn/fps,2),len(good),good[0][1],good[0][2]))
    fn+=step
res.sort(reverse=True)
print(f'{CID}  frames sampled every {STEP}s')
for a,t,k,cx,cy in res[:12]:
    print(f'  t={t:8.2f}  biggest card blob={a:5d}px  cards={k:2d}  centre=({cx},{cy})')
