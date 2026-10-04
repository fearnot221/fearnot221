"""Build a choreographed 24-second desk-buddy animation."""
from pathlib import Path
import base64

assets = Path(__file__).resolve().parents[1] / 'assets'
avatar = base64.b64encode((assets / 'tiger-avatar.png').read_bytes()).decode()
css = '''<style>
.pet{transform-origin:94px 144px;animation:pet 24s cubic-bezier(.77,0,.175,1) infinite}
.dream{animation:dream 3s linear infinite}.dream.b{animation-delay:-1.5s}
.bug{animation:bug 3s steps(12,end) infinite}
.code{animation:code 2.4s cubic-bezier(.23,1,.32,1) infinite}
.breath{animation:breath 4s ease-in-out infinite}
@keyframes pet{0%,4%,12%,20%,26%,36%,46%,54%,68%,100%{transform:translateY(0) rotate(0deg)}8%,16%,30%,40%{transform:translateY(-2px) rotate(-1deg)}58%{transform:translateY(-7px) rotate(2deg)}76%,88%{transform:translateY(3px) rotate(-3deg)}82%,94%{transform:translateY(1px) rotate(-2deg)}}
@keyframes dream{0%{transform:translate(0,6px);opacity:0}20%{opacity:.8}100%{transform:translate(9px,-23px);opacity:0}}
@keyframes bug{0%,100%{transform:translateX(0)}50%{transform:translateX(70px)}}
@keyframes code{0%{transform:translateY(3px);opacity:0}20%{opacity:.8}100%{transform:translateY(-18px);opacity:0}}
@keyframes breath{0%,100%{opacity:.2}50%{opacity:.6}}
.spark{animation:spark 3s ease-in-out infinite}.late{animation-delay:-1.5s}
.cursor{animation:cursor 1s steps(2,end) infinite}
.stage{opacity:0;animation:stage 24s linear infinite}.s2{animation-delay:6s}.s3{animation-delay:12s}.s4{animation-delay:18s}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px)}}
@keyframes spark{0%,100%{opacity:.15}50%{opacity:1}}
@keyframes cursor{0%,49%{opacity:1}50%,100%{opacity:0}}
@keyframes stage{0%{opacity:0}1%,23%{opacity:1}24%,100%{opacity:0}}
@media(prefers-reduced-motion:reduce){.pet,.dream,.bug,.code,.breath,.spark,.cursor,.stage{animation:none}.stage{opacity:0}.s1{opacity:1}.spark{opacity:.6}.dream,.code{display:none}}
</style>'''
buddy = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="840" height="170" viewBox="0 0 840 170" role="img" aria-label="Animated desk buddy: code, debug, take a break, and dream. A decorative loop, not a live status.">{css}
<rect x="2" y="2" width="836" height="166" fill="#111c2c" stroke="#34445a" stroke-width="2"/>
<path d="M2 30V2H30M810 168H838V140" fill="none" stroke="#f5d77a" stroke-width="3"/>
<g class="pet"><image x="28" y="18" width="132" height="132" xlink:href="data:image/png;base64,{avatar}"/></g>
<path d="M184 24V146" stroke="#34445a"/>
<g font-family="monospace"><text x="212" y="34" fill="#9aafc7" font-size="12" letter-spacing="2">FEARNOT'S DESK BUDDY</text>
<g class="stage s1"><text class="code" x="124" y="43" fill="#f5d77a" font-size="16">&lt;/&gt;</text><text x="212" y="79" fill="#f5d77a" font-size="26" font-weight="bold">MAKE A LITTLE MAGIC.</text><text x="212" y="111" fill="#e6d9b8" font-size="15">$ turn_ideas_into_code()</text><rect class="cursor" x="449" y="98" width="9" height="16" fill="#f5d77a"/></g>
<g class="stage s2"><g class="bug" fill="#f5d77a"><rect x="30" y="146" width="10" height="6"/><path d="M28 144h2v10h-2zM40 144h2v10h-2z"/></g><text x="212" y="79" fill="#f5d77a" font-size="26" font-weight="bold">ONE MORE BUG...</text><text x="212" y="111" fill="#e6d9b8" font-size="15">$ print("why are you like this?")</text></g>
<g class="stage s3"><g class="dream" fill="none" stroke="#e6d9b8" stroke-width="2"><path d="M145 55v-7h4v-7h-4v-5"/></g><text x="212" y="79" fill="#f5d77a" font-size="26" font-weight="bold">SAVE. STRETCH. SIP.</text><text x="212" y="111" fill="#e6d9b8" font-size="15">$ take_a_break()  # humans need this too</text></g>
<g class="stage s4"><text x="212" y="79" fill="#f5d77a" font-size="26" font-weight="bold">DREAM IN PIXELS.</text><text x="212" y="111" fill="#e6d9b8" font-size="15">$ sleep()  # tomorrow: another tiny adventure</text><text class="dream" x="140" y="43" fill="#f5d77a" font-size="16">z</text><text class="dream b" x="152" y="32" fill="#f5d77a" font-size="20">Z</text></g>
<text x="212" y="146" fill="#9aafc7" font-size="11">CODE / DEBUG / RECHARGE / REPEAT</text></g>
<g fill="#f5d77a"><rect class="spark" x="778" y="27" width="7" height="7"/><rect class="spark late" x="792" y="27" width="7" height="7"/></g>
</svg>'''
(assets / 'desk-buddy.svg').write_text(buddy)

print('Built the choreographed desk buddy.')
