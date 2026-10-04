"""Compose a self-contained SVG scene and animated tool inventory for GitHub."""
from pathlib import Path
import base64
import re

assets = Path(__file__).resolve().parents[1] / 'assets'
scene = base64.b64encode((assets / 'pixel-workshop.png').read_bytes()).decode()
header = '''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1086" height="424" viewBox="0 0 1086 424" role="img" aria-label="Fearnot's animated pixel workshop: twinkling stars, warm lamplight, rising steam and a welcome terminal">
<style>
.glow{animation:breathe 5s ease-in-out infinite}
.star{animation:twinkle 4s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
.star.b{animation-delay:-1.3s}.star.c{animation-delay:-2.6s}
.steam{animation:steam 5s linear infinite}.steam.b{animation-delay:-2.5s}
.meteor{animation:meteor 12s linear infinite;opacity:0}
.typing{animation:typing 14s steps(40,end) infinite}
.caret-track{animation:caret-track 14s steps(37,end) infinite}
.caret{animation:blink 1.2s steps(2,end) infinite}
@keyframes breathe{0%,100%{opacity:.03}50%{opacity:.18}}
@keyframes twinkle{0%,100%{opacity:.12}50%{opacity:.9}}
@keyframes steam{0%{transform:translate(0,4px);opacity:0}25%{opacity:.28}65%{transform:translate(3px,-13px);opacity:.18}100%{transform:translate(-2px,-26px);opacity:0}}
@keyframes meteor{0%,72%,100%{opacity:0;transform:translate(0,0)}75%{opacity:.8}85%{opacity:0;transform:translate(-105px,45px)}}
@keyframes typing{0%,8%{clip-path:inset(0 100% 0 0)}48%,90%{clip-path:inset(0 0 0 0)}100%{clip-path:inset(0 100% 0 0)}}
@keyframes caret-track{0%,8%{transform:translateX(0)}48%,90%{transform:translateX(355px)}100%{transform:translateX(0)}}
@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}
@media(prefers-reduced-motion:reduce){.glow,.star,.steam,.meteor,.typing,.caret,.caret-track{animation:none}.glow{opacity:.06}.star{opacity:.45}.steam,.meteor{opacity:0}.typing{clip-path:none}.caret-track{transform:translateX(355px)}}
</style>
<image width="1086" height="362" xlink:href="data:image/png;base64,IMAGE_DATA"/>
<path class="glow" d="M622 144L568 238L688 238L646 145Z" fill="#ffd678"/>
<g fill="#fff1b0"><path class="star" d="M619 12h4v7h7v4h-7v7h-4v-7h-7v-4h7z"/><path class="star b" d="M815 21h3v5h5v3h-5v5h-3v-5h-5v-3h5z"/><path class="star c" d="M936 27h3v5h5v3h-5v5h-3v-5h-5v-3h5z"/></g>
<path class="meteor" d="M848 36l-16 7m19-8-3 1" stroke="#ffebaa" stroke-width="3"/>
<g fill="none" stroke="#ffeac0" stroke-width="3"><path class="steam" d="M890 275v-6h4v-8h-4v-5"/><path class="steam b" d="M900 276v-6h-4v-7h4v-5"/></g>
<path d="M0 362H1086V424H0Z" fill="#101a2b"/>
<path d="M0 363H1086" stroke="#34445a" stroke-width="2"/>
<text x="24" y="400" fill="#f5d77a" font-family="monospace" font-size="16">fearnot@workshop:~$</text>
<g class="typing"><text x="224" y="400" fill="#e6d9b8" font-family="monospace" font-size="16">Welcome to my little corner of GitHub.</text></g><g class="caret-track"><rect class="caret" x="224" y="385" width="8" height="18" fill="#f5d77a"/></g>
<g fill="#f5d77a" opacity=".5"><rect x="1022" y="386" width="8" height="8"/><rect x="1036" y="386" width="8" height="8"/><rect x="1050" y="386" width="8" height="8"/></g>
</svg>'''.replace('IMAGE_DATA', scene)
(assets / 'pixel-workshop-animated.svg').write_text(header)

for filename,names in [('languages-animated',['python','typescript','html5','css3']),('tools-animated',['react','docker','nginx'])]:
    labels={'python':'PYTHON','typescript':'TYPESCRIPT','html5':'HTML','css3':'CSS','react':'REACT','docker':'DOCKER','nginx':'NGINX'}
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{len(names)*104}" height="126" viewBox="0 0 {len(names)*104} 126" role="img" aria-label="{", ".join(labels[n] for n in names)}"><style>.signal{{animation:signal 7s cubic-bezier(.77,0,.175,1) infinite}}@keyframes signal{{0%,22%,100%{{opacity:.12}}7%,14%{{opacity:1}}}}@media(prefers-reduced-motion:reduce){{.signal{{animation:none;opacity:.6}}}}</style>']
    for i,name in enumerate(names):
        x=i*104
        icon=(assets/(name+'.svg')).read_text()
        icon=re.sub(r'<svg\b[^>]*>',f'<svg x="{x+27}" y="21" width="46" height="46" viewBox="0 0 128 128">',icon,count=1)
        delay=(i+(4 if filename=='tools-animated' else 0))*.7
        parts.append(f'<rect x="{x+4}" y="4" width="92" height="104" fill="#111c2c" stroke="#34445a" stroke-width="2"/>{icon}<text x="{x+50}" y="92" text-anchor="middle" font-family="monospace" font-size="11" font-weight="bold" fill="#e6d9b8">{labels[name]}</text><g class="signal" style="animation-delay:{delay:g}s"><path d="M{x+4} 22V4H{x+22}" fill="none" stroke="#f5d77a" stroke-width="3"/><rect x="{x+21}" y="115" width="58" height="3" fill="#f5d77a"/></g>')
    parts.append('</svg>')
    (assets/(filename+'.svg')).write_text(''.join(parts))
print('Built animated workshop and seven tool slots.')
