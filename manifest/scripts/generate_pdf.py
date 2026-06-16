#!/usr/bin/env python3
"""
manifest / generate_pdf.py

Accepts a content spec (JSON) and produces a light, designed PDF via weasyprint.
Visual principles: breathe, never dense, editorial not generated.

Usage:
  python generate_pdf.py --spec-file /tmp/spec.json --output /tmp/out.pdf
  python generate_pdf.py --spec '{"title": "..."}' --output /tmp/out.pdf
  python generate_pdf.py --spec-file /tmp/spec.json --output /tmp/out.html --html-only
"""

import argparse
import base64
import io
import json
import subprocess
import sys
from pathlib import Path


# ── Dependency check ──────────────────────────────────────────────────────────

def ensure_deps():
    missing = []
    try:
        import weasyprint  # noqa: F401
    except ImportError:
        missing.append("weasyprint")
    try:
        import matplotlib  # noqa: F401
    except ImportError:
        missing.append("matplotlib")
    if missing:
        print(f"Installing: {', '.join(missing)}", file=sys.stderr)
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", *missing,
            "--break-system-packages", "-q"
        ])


# ── Themes ────────────────────────────────────────────────────────────────────

THEME = {
    "minimal": {
        "accent":       "#111827",
        "accent_light": "#f9fafb",
        "accent_mid":   "#e5e7eb",
        "callout_bg":   "#f0f9ff",
        "callout_bar":  "#2563eb",
        "callout_text": "#1e3a5f",
        "cover_rule":   "#111827",
        "muted":        "#6b7280",
        "body":         "#374151",
        "heading":      "#111827",
        "chart_bar":    "#2563eb",
    },
    "rich": {
        "accent":       "#5b21b6",
        "accent_light": "#faf5ff",
        "accent_mid":   "#ede9fe",
        "callout_bg":   "#faf5ff",
        "callout_bar":  "#7c3aed",
        "callout_text": "#3b0764",
        "cover_rule":   "#5b21b6",
        "muted":        "#7c3aed",
        "body":         "#374151",
        "heading":      "#1e1b4b",
        "chart_bar":    "#7c3aed",
    },
}


def build_css(t: dict) -> str:
    return f"""
@page {{
    size: A4;
    margin: 24mm 22mm 30mm 22mm;
    @bottom-center {{
        content: counter(page);
        font-size: 7.5pt;
        color: #d1d5db;
        font-family: system-ui, sans-serif;
    }}
}}
@page :first {{ @bottom-center {{ content: ""; }} }}

* {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
    font-family: system-ui, -apple-system, 'Segoe UI', sans-serif;
    font-size: 10.5pt;
    line-height: 1.75;
    color: {t['body']};
    background: white;
}}

/* ── Cover ── */
.cover {{
    page-break-after: always;
    padding: 80pt 0 60pt;
}}
.cover-eyebrow {{
    font-size: 7.5pt;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: {t['muted']};
    margin-bottom: 24pt;
}}
.cover h1 {{
    font-size: 34pt;
    font-weight: 800;
    color: {t['heading']};
    line-height: 1.12;
    margin-bottom: 20pt;
    letter-spacing: -0.025em;
    border-bottom: 2pt solid {t['cover_rule']};
    padding-bottom: 24pt;
}}
.cover-sub {{
    font-size: 12pt;
    color: {t['muted']};
    line-height: 1.55;
    margin-top: 20pt;
}}

/* ── Sections (report / mixed / data) ── */
.section {{
    margin-top: 40pt;
}}
.section + .section {{
    border-top: 1pt solid {t['accent_mid']};
    padding-top: 32pt;
}}

.section-label {{
    font-size: 7pt;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: {t['muted']};
    margin-bottom: 10pt;
}}
.section h2 {{
    font-size: 16pt;
    font-weight: 700;
    color: {t['heading']};
    line-height: 1.22;
    margin-bottom: 16pt;
    letter-spacing: -0.015em;
}}

/* ── Slide pages ── */
.slide {{
    page-break-after: always;
    padding-top: 56pt;
    min-height: 72vh;
}}
.slide .section-label {{ margin-bottom: 12pt; }}
.slide h2 {{
    font-size: 24pt;
    font-weight: 800;
    color: {t['heading']};
    line-height: 1.18;
    letter-spacing: -0.025em;
    margin-bottom: 24pt;
}}

/* ── Text ── */
p.body-text {{
    color: {t['body']};
    margin-bottom: 11pt;
    max-width: 64ch;
}}

/* ── Bullets ── */
ul.manifest-bullets {{
    list-style: none;
    padding: 0;
    margin: 0;
}}
ul.manifest-bullets li {{
    padding: 6pt 0 6pt 22pt;
    color: {t['body']};
    position: relative;
    border-bottom: 1pt solid {t['accent_mid']};
    line-height: 1.6;
}}
ul.manifest-bullets li:last-child {{ border-bottom: none; }}
ul.manifest-bullets li::before {{
    content: "";
    position: absolute;
    left: 2pt;
    top: 14.5pt;
    width: 5pt;
    height: 5pt;
    border-radius: 50%;
    background: {t['accent']};
}}

/* ── Callout ── */
.callout {{
    margin: 0;
    padding: 18pt 22pt;
    background: {t['callout_bg']};
    border-left: 3pt solid {t['callout_bar']};
    color: {t['callout_text']};
    font-size: 11.5pt;
    line-height: 1.6;
    font-style: italic;
    max-width: 58ch;
}}

/* ── Code ── */
pre.code-block {{
    background: #0f172a;
    color: #e2e8f0;
    padding: 16pt 18pt;
    border-radius: 5pt;
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    font-size: 8pt;
    line-height: 1.65;
    white-space: pre-wrap;
    overflow-wrap: break-word;
}}

/* ── Diagram ── */
.diagram-wrap {{
    background: #f8fafc;
    border: 1pt solid {t['accent_mid']};
    border-radius: 5pt;
    padding: 14pt 16pt;
}}
.diagram-label {{
    font-size: 7pt;
    color: {t['muted']};
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 8pt;
}}
.diagram-wrap pre {{
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    font-size: 8pt;
    color: #334155;
    white-space: pre-wrap;
}}

/* ── Table ── */
table.manifest-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 9.5pt;
    margin-top: 4pt;
}}
table.manifest-table th {{
    text-align: left;
    font-size: 7pt;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: {t['muted']};
    padding: 0 14pt 9pt 0;
    border-bottom: 2pt solid {t['heading']};
}}
table.manifest-table td {{
    padding: 9pt 14pt 9pt 0;
    border-bottom: 1pt solid {t['accent_mid']};
    color: {t['body']};
    vertical-align: top;
}}
table.manifest-table tr:last-child td {{ border-bottom: none; }}

/* ── Chart ── */
.chart-wrap {{ margin-top: 4pt; }}
.chart-wrap img {{ width: 100%; max-width: 480pt; }}
"""


# ── Chart generator ──────────────────────────────────────────────────────────

def make_chart(content: dict, t: dict) -> str:
    """Render a bar chart and return a base64-encoded PNG."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    labels  = content.get("labels", [])
    values  = content.get("values", [])
    ylabel  = content.get("ylabel", "")
    colors  = content.get("colors") or [t["chart_bar"]] * len(labels)

    fig, ax = plt.subplots(figsize=(8, 3.0))
    bars = ax.bar(labels, values, color=colors, width=0.52, zorder=3,
                  edgecolor="white", linewidth=0.5)

    ax.set_ylabel(ylabel, fontsize=8, color=t["muted"])
    ax.tick_params(axis="x", labelsize=8, colors=t["body"])
    ax.tick_params(axis="y", labelsize=7.5, colors=t["muted"])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(t["accent_mid"])
    ax.spines["bottom"].set_color(t["accent_mid"])
    ax.yaxis.grid(True, color=t["accent_light"], zorder=0, linewidth=0.8)
    ax.set_facecolor("white")
    fig.patch.set_facecolor("white")
    ax.set_axisbelow(True)

    peak = max(values) if values else 1
    for bar, val in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + peak * 0.025,
            f"{val:g}", ha="center", va="bottom",
            fontsize=8, fontweight="600", color=t["heading"]
        )

    fig.tight_layout(pad=0.4)
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=160, bbox_inches="tight", facecolor="white")
    buf.seek(0)
    b64 = base64.b64encode(buf.read()).decode()
    plt.close(fig)
    return b64


# ── HTML helpers ──────────────────────────────────────────────────────────────

def esc(text) -> str:
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def render_body(sec: dict, style: str, t: dict) -> str:
    stype   = sec.get("type", "text")
    content = sec.get("content", "")
    parts   = []

    if stype == "text":
        for para in str(content).split("\n\n"):
            para = para.strip()
            if para:
                parts.append(f'<p class="body-text">{esc(para)}</p>')

    elif stype == "bullets":
        items = content if isinstance(content, list) else [content]
        parts.append('<ul class="manifest-bullets">')
        for item in items:
            parts.append(f"  <li>{esc(str(item))}</li>")
        parts.append("</ul>")

    elif stype == "callout":
        parts.append(f'<div class="callout">{esc(content)}</div>')

    elif stype == "code":
        parts.append(f'<pre class="code-block">{esc(content)}</pre>')

    elif stype == "diagram":
        parts.append('<div class="diagram-wrap">')
        parts.append('  <p class="diagram-label">Mermaid source</p>')
        parts.append(f"  <pre>{esc(content)}</pre>")
        parts.append("</div>")

    elif stype == "table":
        rows = content if isinstance(content, list) else []
        if rows:
            headers = list(rows[0].keys())
            parts.append('<table class="manifest-table"><thead><tr>')
            for h in headers:
                parts.append(f"<th>{esc(h)}</th>")
            parts.append("</tr></thead><tbody>")
            for row in rows:
                parts.append("<tr>")
                for h in headers:
                    parts.append(f"<td>{esc(str(row.get(h, '')))}</td>")
                parts.append("</tr>")
            parts.append("</tbody></table>")

    elif stype == "chart":
        b64 = make_chart(content, t)
        parts.append(
            f'<div class="chart-wrap">'
            f'<img src="data:image/png;base64,{b64}">'
            f'</div>'
        )

    return "\n".join(parts)


def render_section(sec: dict, style: str, t: dict, slide_mode: bool = False) -> str:
    heading     = sec.get("heading", "")
    wrapper_cls = "slide" if slide_mode else "section"
    parts       = [f'<div class="{wrapper_cls}">']
    if heading:
        parts.append(f'  <p class="section-label">{esc(heading)}</p>')
        parts.append(f'  <h2>{esc(heading)}</h2>')
    parts.append(render_body(sec, style, t))
    parts.append("</div>")
    return "\n".join(parts)


def build_html(spec: dict) -> str:
    title    = spec.get("title", "Document")
    subtitle = spec.get("subtitle", "")
    style    = spec.get("style", "minimal")
    doc_type = spec.get("type", "mixed")
    sections = spec.get("sections", [])
    t        = THEME.get(style, THEME["minimal"])

    slide_mode = doc_type == "slides"

    cover = (
        '<div class="cover">\n'
        '  <p class="cover-eyebrow">Manifest</p>\n'
        f'  <h1>{esc(title)}</h1>\n'
        + (f'  <p class="cover-sub">{esc(subtitle)}</p>\n' if subtitle else "")
        + "</div>"
    )

    body = "\n\n".join(
        render_section(s, style, t, slide_mode) for s in sections
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{esc(title)}</title>
<style>{build_css(t)}</style>
</head>
<body>
{cover}
{body}
</body>
</html>"""


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(description="manifest — generate a PDF from a spec")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--spec",      help="JSON spec as a string")
    g.add_argument("--spec-file", help="Path to a JSON spec file")
    p.add_argument("--output",    required=True, help="Output path (.pdf or .html)")
    p.add_argument("--html-only", action="store_true",
                   help="Write HTML instead of PDF (debug)")
    args = p.parse_args()

    spec = (
        json.loads(args.spec) if args.spec
        else json.loads(Path(args.spec_file).read_text())
    )

    html = build_html(spec)
    out  = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    if args.html_only or out.suffix == ".html":
        out.with_suffix(".html").write_text(html, encoding="utf-8")
        print(f"HTML → {out.with_suffix('.html')}", file=sys.stderr)
        return

    ensure_deps()
    from weasyprint import HTML
    HTML(string=html).write_pdf(str(out))
    print(f"PDF → {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
