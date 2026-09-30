from pathlib import Path
from html import escape

root = Path(__file__).resolve().parents[1]
source = (root / "src/circuit-lab.html").read_text(encoding="utf-8")
frame = (root / "tools/frame-template.html").read_text(encoding="utf-8").replace("<!--CIRCUIT_LAB_SOURCE-->", source)
page = (root / "tools/page-template.html").read_text(encoding="utf-8").replace("__CIRCUIT_LAB_FRAME__", escape(frame, quote=True))
(root / "index.html").write_text(page, encoding="utf-8")
print("Built index.html")
