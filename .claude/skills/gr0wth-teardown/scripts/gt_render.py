"""Render a run's playbook.md (or content.md) to one self-contained HTML file.

It handles the Markdown subset references/playbook-format.md defines, plus three
additions:
  - a fenced block whose info string is `prompt` gets a "Copy the prompt" button;
  - `<!-- gt:growth-chart -->` draws data/growth.csv with every move in
    data/moves.csv pinned on it (a hover tooltip, and a table view below);
  - `<!-- gt:contact-sheet channel=<name> -->` lays the top-quarter and bottom
    posts of data/<name>-posts.csv side by side, from their downloaded images.
The words SEEN and INFERRED become labels. Images are embedded, so the file
works on its own.
"""

from __future__ import annotations

import base64
import html
import mimetypes
import re
from pathlib import Path

import gt_analyze as ga
import gt_common as gc

CSS = """
:root{color-scheme:light;--bg:#f6f5f2;--surface:#fcfcfb;--text:#0b0b0b;--text-2:#52514e;--muted:#77756f;
--line:#e3e1db;--accent:#2a78d6;--seen-bg:#e3f1e8;--seen-fg:#145c2f;--inf-bg:#fbefd9;--inf-fg:#7a4a00;
--code-bg:#f0eee9;--pin:#77756f;--series:#2a78d6}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;--bg:#121211;--surface:#1a1a19;
--text:#ffffff;--text-2:#c3c2b7;--muted:#9a988f;--line:#33322f;--accent:#3987e5;--seen-bg:#16351f;--seen-fg:#9fdcb2;
--inf-bg:#3b2c0e;--inf-fg:#f2c97a;--code-bg:#242422;--pin:#9a988f;--series:#3987e5}}
:root[data-theme="dark"]{color-scheme:dark;--bg:#121211;--surface:#1a1a19;--text:#ffffff;--text-2:#c3c2b7;
--muted:#9a988f;--line:#33322f;--accent:#3987e5;--seen-bg:#16351f;--seen-fg:#9fdcb2;--inf-bg:#3b2c0e;--inf-fg:#f2c97a;
--code-bg:#242422;--pin:#9a988f;--series:#3987e5}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",
Inter,Roboto,"Helvetica Neue",Arial,sans-serif}
.wrap{max-width:960px;margin:0 auto;padding:32px 16px 80px}
header.top{display:flex;justify-content:space-between;align-items:flex-start;gap:16px;margin-bottom:8px}
.theme{border:1px solid var(--line);background:var(--surface);color:var(--text-2);border-radius:8px;padding:6px 10px;
font:inherit;font-size:13px;cursor:pointer;flex:none}
h1{font-size:30px;line-height:1.2;margin:0 0 8px;letter-spacing:-0.01em}
h2{font-size:22px;line-height:1.3;margin:48px 0 12px;padding-top:8px;border-top:1px solid var(--line)}
h3{font-size:18px;margin:28px 0 8px}
h4{font-size:16px;margin:20px 0 6px}
p,ul,ol,table,pre,blockquote,figure{margin:0 0 14px}
ul,ol{padding-left:22px}
li{margin:2px 0}
a{color:var(--accent);text-decoration-thickness:1px;text-underline-offset:2px;overflow-wrap:anywhere}
code{font:13px/1.5 ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--code-bg);padding:1px 5px;border-radius:4px}
pre{background:var(--code-bg);border-radius:10px;padding:14px 16px;overflow-x:auto;white-space:pre-wrap;word-break:break-word}
pre code{background:none;padding:0}
blockquote{border-left:3px solid var(--line);margin-left:0;padding:2px 0 2px 14px;color:var(--text-2)}
hr{border:0;border-top:1px solid var(--line);margin:32px 0}
nav.toc{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin:16px 0 8px;font-size:14px}
nav.toc ol{margin:0;padding-left:20px;columns:2;column-gap:32px}
@media (max-width:640px){nav.toc ol{columns:1}h1{font-size:25px}}
.table{overflow-x:auto;margin:0 0 14px;border:1px solid var(--line);border-radius:10px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:14px;margin:0}
th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-weight:600;color:var(--text-2);background:var(--surface)}
tr:last-child td{border-bottom:0}
.tag{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.04em;border-radius:4px;padding:0 5px;line-height:18px;vertical-align:1px}
.tag.seen{background:var(--seen-bg);color:var(--seen-fg)}
.tag.inferred{background:var(--inf-bg);color:var(--inf-fg)}
.prompt{position:relative;margin:0 0 16px}
.prompt pre{margin:0;padding-top:42px}
.copy{position:absolute;top:8px;right:8px;border:1px solid var(--line);background:var(--surface);color:var(--text);
border-radius:6px;padding:4px 10px;font:inherit;font-size:13px;cursor:pointer}
.copy:focus-visible,.theme:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.sheet{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:0 0 18px}
@media (max-width:640px){.sheet{grid-template-columns:1fr}}
.sheet section{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:12px}
.sheet h5{margin:0 0 10px;font-size:13px;color:var(--text-2);text-transform:uppercase;letter-spacing:.05em}
.cells{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:10px}
.gallery{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:12px;margin:0 0 18px}
.gallery .cells{grid-template-columns:repeat(auto-fill,minmax(104px,1fr))}
img{max-width:100%;height:auto}
.cell{margin:0;font-size:12px;color:var(--text-2)}
.cell img{width:100%;aspect-ratio:var(--ar,16/9);object-fit:cover;border-radius:6px;display:block;background:var(--code-bg)}
.sheet.contain .cell img{object-fit:contain;background:#ffffff;border:1px solid var(--line)}
.cell figcaption{margin-top:4px;line-height:1.35}
.cell b{color:var(--text)}
.empty{color:var(--muted);font-size:14px}
figure.chart{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px 14px 8px;position:relative}
figure.chart figcaption{font-size:14px;color:var(--text-2);margin:0 0 6px}
figure.chart svg{width:100%;height:auto;display:block;overflow:visible}
figure.chart .plot{overflow-x:auto;-webkit-overflow-scrolling:touch}
@media (max-width:640px){figure.chart svg{min-width:620px}}
.axis text{fill:var(--muted);font-size:11px}
.axis line,.grid line{stroke:var(--line);stroke-width:1}
.series{fill:none;stroke:var(--series);stroke-width:2;stroke-linejoin:round;stroke-linecap:round}
.dot{fill:var(--series);stroke:var(--surface);stroke-width:2}
.pin line{stroke:var(--pin);stroke-width:1;stroke-dasharray:3 3}
.pin circle{fill:var(--surface);stroke:var(--pin);stroke-width:2}
.pin:hover line,.pin:focus line{stroke:var(--text)}
.pin:hover circle,.pin:focus circle{stroke:var(--text)}
.hit{fill:transparent;cursor:default}
.tip{position:absolute;pointer-events:none;background:var(--text);color:var(--bg);font-size:12px;line-height:1.4;
padding:6px 8px;border-radius:6px;max-width:260px;opacity:0;transition:opacity .08s}
.tip.on{opacity:1}
details.data{margin-top:8px;font-size:13px}
details.data summary{cursor:pointer;color:var(--text-2)}
footer{margin-top:56px;color:var(--muted);font-size:13px}
"""

JS = """
(function(){
  var root=document.documentElement,btn=document.querySelector('.theme');
  function label(){var d=root.getAttribute('data-theme');btn.textContent=d==='dark'?'Light':d==='light'?'Dark':
    (matchMedia('(prefers-color-scheme: dark)').matches?'Light':'Dark');}
  try{var saved=localStorage.getItem('gt-theme');if(saved)root.setAttribute('data-theme',saved);}catch(e){}
  if(btn){label();btn.addEventListener('click',function(){
    var dark=root.getAttribute('data-theme')==='dark'||(!root.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme: dark)').matches);
    root.setAttribute('data-theme',dark?'light':'dark');try{localStorage.setItem('gt-theme',root.getAttribute('data-theme'));}catch(e){}label();});}
  document.querySelectorAll('.copy').forEach(function(b){b.addEventListener('click',function(){
    var text=b.parentNode.querySelector('code').innerText;
    function done(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy the prompt';},1600);}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(text).then(done,fallback);}else{fallback();}
    function fallback(){var t=document.createElement('textarea');t.value=text;document.body.appendChild(t);t.select();
      try{document.execCommand('copy');done();}catch(e){}document.body.removeChild(t);}
  });});
  document.querySelectorAll('figure.chart').forEach(function(fig){
    var tip=fig.querySelector('.tip');
    fig.querySelectorAll('[data-tip]').forEach(function(el){
      function show(ev){tip.textContent=el.getAttribute('data-tip');tip.classList.add('on');
        var r=fig.getBoundingClientRect(),b=el.getBoundingClientRect();
        var x=(ev&&ev.clientX?ev.clientX:b.left+b.width/2)-r.left,y=b.top-r.top;
        tip.style.left=Math.max(8,Math.min(x-tip.offsetWidth/2,r.width-tip.offsetWidth-8))+'px';
        tip.style.top=Math.max(4,y-tip.offsetHeight-8)+'px';}
      function hide(){tip.classList.remove('on');}
      el.addEventListener('mouseenter',show);el.addEventListener('mousemove',show);el.addEventListener('mouseleave',hide);
      el.addEventListener('focus',show);el.addEventListener('blur',hide);
    });
  });
})();
"""

# ---------------------------------------------------------------- inline Markdown


def _inline(text: str) -> str:
    tokens = []

    def keep(fragment):
        tokens.append(fragment)
        return "\x00%d\x00" % (len(tokens) - 1)

    text = re.sub(r"`([^`]+)`", lambda m: keep("<code>%s</code>" % html.escape(m.group(1))), text)
    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", lambda m: keep(
        '<img src="%s" alt="%s" loading="lazy">' % (html.escape(m.group(2)), html.escape(m.group(1)))), text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+|[^)\s:]+)\)", lambda m: keep(
        '<a href="%s">%s</a>' % (html.escape(m.group(2)), _inline_plain(m.group(1)))), text)
    text = re.sub(r"(?<![\"'=(])\b(https?://[^\s<>\"')\]]+[^\s<>\"')\].,;:!?])", lambda m: keep(
        '<a href="%s">%s</a>' % (html.escape(m.group(1)), html.escape(m.group(1)))), text)
    text = html.escape(text, quote=False)
    text = _inline_marks(text)
    return re.sub(r"\x00(\d+)\x00", lambda m: tokens[int(m.group(1))], text)


def _inline_plain(text: str) -> str:
    return _inline_marks(html.escape(text, quote=False))


def _inline_marks(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(r"\bSEEN\b", '<span class="tag seen">SEEN</span>', text)
    text = re.sub(r"\bINFERRED\b", '<span class="tag inferred">INFERRED</span>', text)
    return text


# ---------------------------------------------------------------- block Markdown


def _slug(text, used):
    base = re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", text).lower()).strip("-") or "section"
    slug, n = base, 2
    while slug in used:
        slug = "%s-%d" % (base, n)
        n += 1
    used.add(slug)
    return slug


def _table(lines):
    def cells(line):
        line = line.strip()
        if line.startswith("|"):
            line = line[1:]
        if line.endswith("|"):
            line = line[:-1]
        return [c.strip() for c in re.split(r"(?<!\\)\|", line)]
    head = cells(lines[0])
    body = [cells(line) for line in lines[2:]]
    out = ['<div class="table"><table><thead><tr>']
    out += ["<th>%s</th>" % _inline(c) for c in head]
    out.append("</tr></thead><tbody>")
    for row in body:
        out.append("<tr>" + "".join("<td>%s</td>" % _inline(c.replace("\\|", "|")) for c in row) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


_LIST_RE = re.compile(r"^(\s*)([-*]|\d+[.)])\s+(.*)$")


def _list(lines):
    """Nested lists from indentation (two or more spaces per level)."""
    html_parts, stack = [], []  # stack of (indent, tag)
    for line in lines:
        m = _LIST_RE.match(line)
        if not m:  # a continuation line joins the last item
            if html_parts:
                html_parts[-1] = html_parts[-1][:-5] + " " + _inline(line.strip()) + "</li>"
            continue
        indent, marker, content = len(m.group(1).expandtabs(4)), m.group(2), m.group(3)
        tag = "ol" if marker[0].isdigit() else "ul"
        while stack and indent < stack[-1][0]:
            _indent, closed_tag, nested = stack.pop()
            html_parts.append("</%s>" % closed_tag)
            if nested:
                html_parts.append("</li>")
        if not stack or indent > stack[-1][0]:
            if stack and html_parts and html_parts[-1].endswith("</li>"):
                html_parts[-1] = html_parts[-1][:-5]
                stack.append((indent, tag, True))
            else:
                stack.append((indent, tag, False))
            html_parts.append("<%s>" % tag)
        html_parts.append("<li>%s</li>" % _inline(content))
    closing = []
    while stack:
        indent, tag, nested = stack.pop()
        closing.append("</%s>" % tag)
        if nested:
            closing.append("</li>")
    return "".join(html_parts + closing)


def markdown(text: str, directive=None):
    """(body_html, title, toc) for the supported Markdown subset."""
    lines = text.replace("\r\n", "\n").split("\n")
    out, toc, used, title = [], [], set(), ""
    i = 0
    paragraph = []

    def flush():
        if paragraph:
            out.append("<p>%s</p>" % _inline(" ".join(s.strip() for s in paragraph)))
            del paragraph[:]

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("```"):
            flush()
            info = stripped[3:].strip()
            j = i + 1
            while j < len(lines) and not lines[j].strip().startswith("```"):
                j += 1
            code = html.escape("\n".join(lines[i + 1:j]))
            if info == "prompt":
                out.append('<div class="prompt"><button class="copy" type="button">Copy the prompt</button>'
                           "<pre><code>%s</code></pre></div>" % code)
            else:
                out.append("<pre><code>%s</code></pre>" % code)
            i = j + 1
            continue
        m = re.match(r"^<!--\s*gt:([a-z-]+)(.*?)-->\s*$", stripped)
        if m:
            flush()
            args = dict(re.findall(r"(\w+)=([^\s]+)", m.group(2)))
            out.append(directive(m.group(1), args) if directive else "")
            i += 1
            continue
        if stripped.startswith("<!--"):
            flush()
            while i < len(lines) and "-->" not in lines[i]:
                i += 1
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            flush()
            level, content = len(m.group(1)), _inline(m.group(2).strip())
            if level == 1 and not title:
                title = re.sub(r"<[^>]+>", "", content)
            anchor = _slug(content, used)
            if level == 2:
                toc.append((anchor, content))
            out.append('<h%d id="%s">%s</h%d>' % (level, anchor, content, level))
            i += 1
            continue
        if re.match(r"^(-{3,}|\*{3,})$", stripped):
            flush()
            out.append("<hr>")
            i += 1
            continue
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            flush()
            j = i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                j += 1
            out.append(_table(lines[i:j]))
            i = j
            continue
        if _LIST_RE.match(line):
            flush()
            j = i
            block = []
            while j < len(lines) and lines[j].strip() and (_LIST_RE.match(lines[j]) or lines[j].startswith("  ")):
                block.append(lines[j])
                j += 1
            out.append(_list(block))
            i = j
            continue
        if stripped.startswith(">"):
            flush()
            j = i
            quote = []
            while j < len(lines) and lines[j].strip().startswith(">"):
                quote.append(lines[j].strip()[1:].strip())
                j += 1
            out.append("<blockquote>%s</blockquote>" % _inline(" ".join(quote)))
            i = j
            continue
        if not stripped:
            flush()
        else:
            paragraph.append(line)
        i += 1
    flush()
    return "\n".join(out), title, toc


# ---------------------------------------------------------------- images


def _data_uri(path: Path) -> str:
    kind = mimetypes.guess_type(str(path))[0] or "image/jpeg"
    data = path.read_bytes()
    if data[:3] == b"\xff\xd8\xff":
        kind = "image/jpeg"
    elif data[:8] == b"\x89PNG\r\n\x1a\n":
        kind = "image/png"
    elif data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        kind = "image/webp"
    return "data:%s;base64,%s" % (kind, base64.b64encode(data).decode())


def _embed_images(body: str, run: Path, link_only: bool) -> str:
    def swap(m):
        src = html.unescape(m.group(1))
        if src.startswith(("http://", "https://", "data:")) or link_only:
            return m.group(0)
        path = (run / src).resolve()
        if not path.exists() or run.resolve() not in path.parents:
            return m.group(0)
        return 'src="%s"' % _data_uri(path)
    return re.sub(r'src="([^"]+)"', swap, body)


# ---------------------------------------------------------------- the growth chart


def _nice_scale(value, min_ticks=4, max_ticks=6):
    """(top, step): a round step (1, 2, 2.5, or 5 times a power of ten) giving 4 to 6
    intervals, and the first multiple of it at or above the value."""
    if value <= 0:
        return 1, 0.25
    exponent = 10 ** (len(str(int(value))) - 1)
    for scale in (exponent / 10.0, exponent):
        for unit in (1, 2, 2.5, 5):
            step = unit * scale
            intervals = int(-(-value // step))
            if min_ticks <= intervals <= max_ticks:
                return step * intervals, step
    return 10 * exponent, 2.5 * exponent


def _fmt(value):
    if value >= 1e6:
        return "%.1fM" % (value / 1e6)
    if value >= 1e3:
        return "%.0fK" % (value / 1e3) if value >= 1e4 else "%.1fK" % (value / 1e3)
    return ("%.1f" % value).rstrip("0").rstrip(".")


def growth_chart(run: Path, key="ratings"):
    series = gc.read_csv(run / "data" / "growth.csv")
    points = [(r["month"], ga.to_number(r.get(key))) for r in series]
    points = [(m, v) for m, v in points if v is not None]
    if len(points) < 2:
        return '<p class="empty">No growth series to draw (data/growth.csv has fewer than two %s values).</p>' % key
    moves = gc.read_csv(run / "data" / "moves.csv")
    w, h, left, right, top, bottom = 880, 320, 56, 16, 16, 34
    first, last = ga._month_index(points[0][0]), ga._month_index(points[-1][0])
    span = max(last - first, 1)
    ymax, ystep = _nice_scale(max(v for _m, v in points))
    ticks = [ystep * k for k in range(int(round(ymax / ystep)) + 1)]

    def x(month_index):
        return left + (w - left - right) * (month_index - first) / span

    def y(value):
        return top + (h - top - bottom) * (1 - value / ymax)

    parts = ['<g class="grid">']
    for value in ticks:
        parts.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f"/>' % (left, w - right, y(value), y(value)))
    parts.append('</g><g class="axis">')
    for value in ticks:
        parts.append('<text x="%d" y="%.1f" text-anchor="end" dy="4">%s</text>' % (left - 8, y(value), _fmt(value)))
    years = [str(year) for year in range(int(points[0][0][:4]), int(points[-1][0][:4]) + 1)]
    for year in years:
        index = ga._month_index(year + "-01")
        if first <= index <= last:
            parts.append('<text x="%.1f" y="%d" text-anchor="middle">%s</text>' % (x(index), h - 10, year))
    parts.append("</g>")
    path = " ".join(("M" if i == 0 else "L") + "%.1f,%.1f" % (x(ga._month_index(m)), y(v))
                    for i, (m, v) in enumerate(points))
    parts.append('<path class="series" d="%s"/>' % path)
    for m, v in points:
        cx, cy = x(ga._month_index(m)), y(v)
        parts.append('<circle class="dot" cx="%.1f" cy="%.1f" r="4"/>' % (cx, cy))
        parts.append('<circle class="hit" cx="%.1f" cy="%.1f" r="12" tabindex="0" data-tip="%s: %s %s"/>' % (
            cx, cy, m, "{:,}".format(int(v)), html.escape(key.replace("_", " "))))
    pinned = []
    for move in moves:
        when = gc.parse_date(move.get("date", ""))
        if not when:
            continue
        index = ga._month_index(gc.month_of(when)) + (when.day - 1) / 31.0
        if not first <= index <= last:
            continue
        px = x(index)
        tip = "%s - %s (%s)" % (move.get("date", "")[:10], move.get("label", ""), move.get("channel", ""))
        if move.get("lift_pct"):
            tip += ", lift %s%%" % move["lift_pct"]
        parts.append('<g class="pin" tabindex="0" data-tip="%s"><line x1="%.1f" x2="%.1f" y1="%d" y2="%d"/>'
                     '<circle cx="%.1f" cy="%d" r="4"/><rect class="hit" x="%.1f" y="%d" width="12" height="%d"/></g>' % (
                         html.escape(tip), px, px, top, h - bottom, px, h - bottom, px - 6, top, h - bottom - top))
        pinned.append(move)
    rows = "".join("<tr><td>%s</td><td>%s</td></tr>" % (m, "{:,}".format(int(v))) for m, v in points)
    move_rows = "".join("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (
        html.escape(mv.get("date", "")[:10]), html.escape(mv.get("channel", "")), html.escape(mv.get("label", "")))
        for mv in pinned)
    caption = "App Store ratings total by month%s." % (
        ", with %d dated moves pinned (hover a pin)" % len(pinned) if pinned else "")
    return ('<figure class="chart"><figcaption>%s</figcaption><div class="plot">'
            '<svg viewBox="0 0 %d %d" role="img" aria-label="%s">%s</svg></div>'
            '<div class="tip" role="status"></div><details class="data"><summary>Table view</summary>'
            '<div class="table"><table><thead><tr><th>Month</th><th>%s</th></tr></thead><tbody>%s</tbody></table></div>%s'
            "</details></figure>" % (
                caption, w, h, html.escape(caption), "".join(parts), html.escape(key.replace("_", " ").title()), rows,
                ('<div class="table"><table><thead><tr><th>Move date</th><th>Channel</th><th>Move</th></tr></thead>'
                 "<tbody>%s</tbody></table></div>" % move_rows) if move_rows else ""))


# ---------------------------------------------------------------- contact sheets


RATIOS = {"tiktok": "9/16", "instagram": "4/5", "appstore": "9/16", "x": "16/9", "ads-google": "6/5"}
# Images whose edges carry text (ad previews, screenshots of posts) are shown whole, not cropped.
CONTAIN = {"ads-google", "x", "linkedin", "reddit"}


def _tier_by(rows, metric):
    """Top quarter and bottom half by one metric, for a data file that has no tier column."""
    ranked = sorted((r for r in rows if ga.to_number(r.get(metric)) is not None),
                    key=lambda r: -ga.to_number(r.get(metric)))
    n = len(ranked)
    top_n, bottom_n = int(-(-n // 4)), n // 2
    for index, row in enumerate(ranked):
        row["tier"] = "top" if index < top_n else ("bottom" if index >= n - bottom_n else "middle")
        row["metric_value"] = row.get(metric)
    return rows


def contact_sheet(run: Path, channel: str, per_side=8, source=None, metric=None):
    """Top-quarter and bottom-half images side by side. `source` names another data file
    (data/<source>.csv) and `metric` the column to tier it by, when it has no tier column."""
    rows = gc.read_csv(run / "data" / ("%s.csv" % source if source else "%s-posts.csv" % channel))
    if rows and metric:
        rows = _tier_by(rows, metric)
    ratio = RATIOS.get(source or channel, "16/9")

    def label_of(r):
        if r.get("first_shown"):
            return "first shown %s, last %s" % (r["first_shown"], r.get("last_shown", ""))
        return (r.get("title") or r.get("text") or r.get("caption") or "")[:90]

    def cells(tier, reverse):
        chosen = [r for r in rows if r.get("tier") == tier and r.get("image")]
        chosen.sort(key=lambda r: ga.to_number(r.get("metric_value") or r.get("metric")) or 0, reverse=reverse)
        if not chosen:
            return '<p class="empty">No %s posts with a downloaded image.</p>' % tier
        out = []
        for r in chosen[:per_side]:
            label = label_of(r)
            metric_value = ga.to_number(r.get("metric_value") or r.get("metric"))
            shown = _fmt(metric_value) + (" days" if metric == "days_shown" else "") if metric_value is not None else ""
            out.append('<figure class="cell"><a href="%s"><img src="%s" alt="%s"></a><figcaption><b>%s</b> %s</figcaption></figure>' % (
                html.escape(r.get("url") or r.get("ad_url") or ""), html.escape(r["image"]), html.escape(label),
                shown, html.escape(label)))
        return '<div class="cells">%s</div>' % "".join(out)

    if not rows:
        return '<p class="empty">No %s posts were pulled or captured.</p>' % html.escape(channel)
    fit = " contain" if (source or channel) in CONTAIN else ""
    return ('<div class="sheet%s" style="--ar:%s"><section><h5>Top quarter</h5>%s</section>'
            "<section><h5>Bottom half</h5>%s</section></div>" % (fit, ratio, cells("top", True), cells("bottom", False)))


def gallery(run: Path, folder: str, limit=12, ratio="9/16"):
    """Every image in one run folder, in name order (App Store screenshots, a capture set)."""
    base = (run / folder).resolve()
    if run.resolve() not in base.parents or not base.is_dir():
        return '<p class="empty">No images in %s.</p>' % html.escape(folder)
    files = sorted(p for p in base.iterdir() if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp"))[:int(limit)]
    if not files:
        return '<p class="empty">No images in %s.</p>' % html.escape(folder)
    cells = "".join('<figure class="cell"><img src="%s" alt="%s"><figcaption>%s</figcaption></figure>' % (
        html.escape(str(p.relative_to(run.resolve()))), html.escape(p.name), html.escape(p.stem)) for p in files)
    return '<div class="gallery" style="--ar:%s"><div class="cells">%s</div></div>' % (html.escape(ratio), cells)


# ---------------------------------------------------------------- the page


def render(run, source_name=None, link_images=False):
    run = Path(run)
    names = [source_name] if source_name else ["playbook.md", "content.md"]
    source = next((run / n for n in names if (run / n).exists()), None)
    if not source:
        raise SystemExit("No %s in %s." % (" or ".join(names), run))

    def directive(name, args):
        if name == "growth-chart":
            return growth_chart(run, args.get("key", "ratings"))
        if name == "contact-sheet":
            return contact_sheet(run, args.get("channel", ""), source=args.get("source"), metric=args.get("metric"))
        if name == "gallery":
            return gallery(run, args.get("dir", "img"), args.get("limit", 12), args.get("ratio", "9/16"))
        return ""

    body, title, toc = markdown(source.read_text(encoding="utf-8"), directive)
    body = _embed_images(body, run, link_images)
    toc_html = ""
    if len(toc) > 2:
        toc_html = '<nav class="toc" aria-label="Contents"><ol>%s</ol></nav>' % "".join(
            '<li><a href="#%s">%s</a></li>' % (a, c) for a, c in toc)
    first_h1 = re.search(r"<h1[^>]*>.*?</h1>", body, re.S)
    heading = first_h1.group(0) if first_h1 else ""
    if first_h1:
        body = body.replace(heading, "", 1)
    meta = gc.read_json(run / "run.json")
    page = ("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            "<title>%s</title><style>%s</style></head><body><div class=\"wrap\">"
            "<header class=\"top\"><div>%s</div><button class=\"theme\" type=\"button\">Dark</button></header>%s%s"
            "<footer>gr0wth-teardown run %s for %s. Generated from %s; every count is dated in the run's data files.</footer>"
            "</div><script>%s</script></body></html>") % (
        html.escape(title or "Gr0wth teardown"), CSS, heading, toc_html, body, html.escape(run.name),
        html.escape(meta.get("product", "")), html.escape(source.name), JS)
    out = source.with_suffix(".html")
    out.write_text(page, encoding="utf-8")
    return out
