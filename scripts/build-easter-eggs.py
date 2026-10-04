"""Build the profile's decorative desk buddy and expandable treasure-room artwork."""
from pathlib import Path
import base64

assets = Path(__file__).resolve().parents[1] / 'assets'
avatar = base64.b64encode((assets / 'tiger-avatar.png').read_bytes()).decode()
css = '''<style>
.float{animation:float 4s cubic-bezier(.77,0,.175,1) infinite}
.spark{animation:spark 3s ease-in-out infinite}.late{animation-delay:-1.5s}
.cursor{animation:cursor 1s steps(2,end) infinite}
.stage{opacity:0;animation:stage 24s linear infinite}.s2{animation-delay:6s}.s3{animation-delay:12s}.s4{animation-delay:18s}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}
@keyframes spark{0%,100%{opacity:.15}50%{opacity:1}}
@keyframes cursor{0%,49%{opacity:1}50%,100%{opacity:0}}
@keyframes stage{0%,23%{opacity:1}25%,100%{opacity:0}}
@media(prefers-reduced-motion:reduce){.float,.spark,.cursor,.stage{animation:none}.stage{opacity:0}.s1{opacity:1}.spark{opacity:.6}}
</style>'''
buddy = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="840" height="170" viewBox="0 0 840 170" role="img" aria-label="Animated desk buddy: code, debug, take a break, and dream. A decorative loop, not a live status.">{css}
<rect x="2" y="2" width="836" height="166" fill="#111c2c" stroke="#34445a" stroke-width="2"/>
<path d="M2 30V2H30M810 168H838V140" fill="none" stroke="#f5d77a" stroke-width="3"/>
<g class="float"><image x="28" y="18" width="132" height="132" xlink:href="data:image/png;base64,{avatar}"/></g>
<path d="M184 24V146" stroke="#34445a"/>
<g font-family="monospace"><text x="212" y="34" fill="#9aafc7" font-size="12" letter-spacing="2">FEARNOT'S DESK BUDDY</text>
<g class="stage s1"><text x="212" y="79" fill="#f5d77a" font-size="26" font-weight="bold">MAKE A LITTLE MAGIC.</text><text x="212" y="111" fill="#e6d9b8" font-size="15">$ turn_ideas_into_code()</text><rect class="cursor" x="449" y="98" width="9" height="16" fill="#f5d77a"/></g>
<g class="stage s2"><text x="212" y="79" fill="#f5d77a" font-size="26" font-weight="bold">ONE MORE BUG...</text><text x="212" y="111" fill="#e6d9b8" font-size="15">$ print("why are you like this?")</text></g>
<g class="stage s3"><text x="212" y="79" fill="#f5d77a" font-size="26" font-weight="bold">SAVE. STRETCH. SIP.</text><text x="212" y="111" fill="#e6d9b8" font-size="15">$ take_a_break()  # humans need this too</text></g>
<g class="stage s4"><text x="212" y="79" fill="#f5d77a" font-size="26" font-weight="bold">DREAM IN PIXELS.</text><text x="212" y="111" fill="#e6d9b8" font-size="15">$ sleep()  # tomorrow: another tiny adventure</text><text class="spark" x="144" y="30" fill="#f5d77a" font-size="18">z</text></g>
<text x="212" y="146" fill="#9aafc7" font-size="11">CODE / DEBUG / RECHARGE / REPEAT</text></g>
<g fill="#f5d77a"><rect class="spark" x="778" y="27" width="7" height="7"/><rect class="spark late" x="792" y="27" width="7" height="7"/></g>
</svg>'''
(assets / 'desk-buddy.svg').write_text(buddy)

parts=[f'''<svg xmlns="http://www.w3.org/2000/svg" width="840" height="270" viewBox="0 0 840 270" role="img" aria-label="Secret room with three treasure chests. Chest A reads 01000001, B reads 01000010, C reads 01000011. Find the binary ASCII code for C.">{css}<rect x="2" y="2" width="836" height="266" fill="#101a2b" stroke="#34445a" stroke-width="2"/><path d="M2 42H838" stroke="#34445a"/><text x="24" y="28" fill="#f5d77a" font-family="monospace" font-size="15" font-weight="bold" letter-spacing="2">SECRET ROOM / THE BINARY KEY</text><text x="24" y="68" fill="#e6d9b8" font-family="monospace" font-size="13">The key is in the chest whose binary ASCII label spells C.</text><path d="M24 222H816" stroke="#34445a" stroke-width="2"/>''']
for i,label in enumerate(['A','B','C']):
    x=125+i*270
    parts.append(f'''<g><text x="{x+25}" y="105" text-anchor="middle" fill="#9aafc7" font-family="monospace" font-size="15">{65+i:08b}</text><g class="float" style="animation-delay:{-i*1.3}s"><path d="M{x-24} 150V128H{x-14}V118H{x+64}V128H{x+74}V150Z" fill="#b98938" stroke="#f5d77a" stroke-width="3"/><path d="M{x-24} 150H{x+74}V201H{x-24}Z" fill="#6c4930" stroke="#f5d77a" stroke-width="3"/><path d="M{x-8} 121V199M{x+58} 121V199M{x-24} 151H{x+74}" stroke="#e4b852" stroke-width="5"/><rect x="{x+16}" y="143" width="18" height="25" fill="#f5d77a"/><rect x="{x+23}" y="150" width="4" height="10" fill="#111c2c"/></g><text x="{x+25}" y="247" text-anchor="middle" fill="#f5d77a" font-family="monospace" font-size="16" font-weight="bold">CHEST {label}</text></g>''')
parts.append('<g fill="#f5d77a"><rect class="spark" x="56" y="116" width="5" height="5"/><rect class="spark late" x="770" y="135" width="5" height="5"/></g></svg>')
(assets / 'secret-room.svg').write_text(''.join(parts))
print('Built desk buddy and binary treasure room.')
