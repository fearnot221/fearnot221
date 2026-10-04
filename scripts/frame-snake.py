"""Give generated contribution snakes a pixel-game frame without changing animation."""
from pathlib import Path
import re

for path in Path('dist').glob('github-contribution-grid-snake*.svg'):
    source = path.read_text()
    root = re.search(r'<svg\b([^>]*)>', source)
    if root is None:
        raise ValueError(f'Missing SVG root: {path}')
    attrs = root.group(1)
    width = float(re.search(r'\bwidth="([\d.]+)"', attrs).group(1))
    height = float(re.search(r'\bheight="([\d.]+)"', attrs).group(1))
    dark = 'dark' in path.name
    bg, line, ink = ('#111c2c', '#34445a', '#f5d77a') if dark else ('#fff8e7', '#ddc995', '#75540b')
    w, h = width + 40, height + 96
    nested = source[root.start():].replace('<svg ', '<svg x="20" y="64" ', 1)
    frame = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w:g}" height="{h:g}" viewBox="0 0 {w:g} {h:g}" role="img" aria-label="Contribution arcade: animated GitHub contribution snake">
<rect x="2" y="2" width="{w-4:g}" height="{h-4:g}" fill="{bg}" stroke="{line}" stroke-width="4"/>
<path d="M2 48H{w-2:g}" stroke="{line}" stroke-width="2"/>
<rect x="20" y="19" width="10" height="10" fill="{ink}"/>
<text x="42" y="30" font-family="monospace" font-size="16" font-weight="bold" letter-spacing="2" fill="{ink}">CONTRIBUTION ARCADE</text>
<text x="{w-20:g}" y="30" text-anchor="end" font-family="monospace" font-size="12" fill="{ink}">FEARNOT / SNAKE</text>
{nested}
</svg>'''
    path.write_text(frame)
    print(f'Framed {path}')
