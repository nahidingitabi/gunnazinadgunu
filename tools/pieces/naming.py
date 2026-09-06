#!/usr/bin/env python3
"""Per-piece candidate names, ranked by how natural the name is for the picture.

Rank 0 is what an ordinary person would write first. The ranks are the whole point:
the feasibility test alone says yes to everything, so the discriminator has to be
"which answer needs the least far-fetched naming", not "which answer is possible".

Piece 6 is FEASTABLES on the user's identification.
"""
import re
def L(s): return re.sub(r'[^A-Z]','',s.upper())

# piece key -> (red index, blue index, [names in rank order])
PIECES = {
 'calendar': (2, 4, ['calendar','calendar page','desk calendar','spiral calendar',
                     'tear off calendar','notepad','christmas','december','date',
                     'advent calendar']),
 'gnome':    (2,11, ['santas helper','garden gnome','christmas elf','christmas gnome',
                     'elf on the shelf','gingerbread man','father christmas','garden dwarf',
                     'roller skate','snowboarder','christmas elves']),
 'africa':   (4, 8, ['continent','map of africa','african continent','silhouette',
                     'potted plant','thatching','houseplant','africa and plant','seedling',
                     'greenery','shrubbery','african bush','savannah','madagascar']),
 'bow':      (5, 7, ['glasses','butterfly','eyeglasses','spectacles','sunglasses',
                     'hair bow','ribbon bow','gift bow','shoelace','reading glasses',
                     'infinity']),
 'oman':     (6, 5, ['flag of oman','oman flag','flag oman','omani flag','muscat',
                     'sultanate of oman','the flag of oman']),
 'feast':    (6, 6, ['feastables','feastables bar','feastable','chocolate bar','chocolate',
                     'mrbeast bar','candy bar']),
 # measured: white-balanced #BF7B65, 28.8 from Twemoji brown square #C1694F and 89.1
 # from red square #DD2E44 -- so brown square leads
 'rect':     (6, 8, ['brown square','rectangle','red rectangle','terracotta','maroon square',
                     'brown rectangle','red square','closed book','notebook','red brick',
                     'brick wall','chocolate bar','front door','red carpet','textbook',
                     'orange square']),
 'frames':   (7, 1, ['mosquito net','file cabinet','filing cabinet','picture frame',
                     'framed picture','windows','window pane','window screen','card index',
                     'mosquito','solar panel','two windows','bookcase','drawers',
                     'chest of drawers']),
 'barn':     (7, 4, ['american barn','american flag','flag united states','united states',
                     'america','farmhouse','stars and stripes','us flag and barn',
                     'old glory']),
 'chart':    (8, 9, ['column chart','chart decreasing','down arrow','decreasing chart',
                     'downwards arrow','chart increasing','bar chart down','arrow and chart',
                     'statistics','histogram']),
 'snow':     (9, 5, ['cloud with snow','snow cloud','snowflake','snowstorm','snow shower',
                     'snowing cloud','light snow','snowy cloud']),
 'joy':      (10,14,['face with tears of joy','tears of joy emoji','laughing crying face',
                     'crying laughing face','tears of joy face','laughing with tears',
                     'rolling on the floor laughing','laughing face with tears']),
 'eagle':    (7, 9, ['bald eagle','bubo ascalaphus','golden eagle','pharaoh eagle owl',
                     'american eagle','stone eagle','rock and eagle','eagle and rock',
                     'gold and eagle','egg and eagle','nugget and eagle']),
 'p14':      (7, None, ['swimsuit','one piece swimsuit','bathing suit','swimwear','swimming',
                     'tank top','arrowhead','spearhead','plumb bob']),
}
ORDER = list(PIECES)

def options():
    """piece -> list of (rank, name, redLetter, blueLetter or None); impossible names dropped"""
    out = {}
    for k,(ri,bi,names) in PIECES.items():
        lst=[]
        for rank,nm in enumerate(names):
            c=L(nm)
            if len(c) < ri: continue
            if bi is not None and len(c) < bi: continue
            lst.append((rank, nm, c[ri-1], c[bi-1] if bi else None))
        if not lst: raise SystemExit('no viable name for '+k)
        out[k]=lst
    return out

if __name__=='__main__':
    for k,lst in options().items():
        ri,bi,_=PIECES[k]
        print('%-9s r%-2s b%-3s  %s'%(k,ri,bi if bi else '?',
              '  '.join('%s=%s/%s'%(n.split()[0][:9],r,b or '?') for _,n,r,b in lst[:6])))
