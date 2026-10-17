"""
第二轮：为缺少专用 CSS 的文件追加工具专属样式
"""
import os, re

APPS_DIR = r"D:\GitHub\mini-tools\apps"

TOOL_EXTRA_CSS = {
    "text-diff.html": """
/* 文本差异对比专用样式 */
.toolbar {
  display: flex; align-items: center; gap: 8px; padding: 6px 16px;
  background: #fafafa; border-bottom: 1px solid var(--border);
  flex-shrink:0; flex-wrap:wrap;
}
.toolbar-sep { width:1px; height:20px; background:var(--border); margin:0 4px; }
.toolbar-hint { font-size:0.7rem; color:var(--text-light); margin-left:auto; }
.panel {
  flex:1; display:flex; flex-direction:column; overflow:hidden;
}
.panel:nth-child(1) { border-right: 1px solid var(--border); }
.panel-header {
  display:flex; align-items:center; justify-content:space-between;
  padding:6px 12px; font-size:0.75rem; font-weight:600;
  background: #fafafa; border-bottom: 1px solid var(--border);
  color: var(--text);
}
.panel-body { flex:1; overflow:hidden; }
.panel-body textarea {
  width:100%; height:100%; padding:12px 14px;
  border:none; background:#fff; color:var(--text);
  font-family:var(--font-mono); font-size:0.82rem; line-height:1.6;
  resize:none; outline:none;
}
.panel-body textarea::placeholder { color: #999; }
.result-area {
  border-top: 1px solid var(--border); overflow-y:auto;
  height:200px; background:#fafafa; flex-shrink:0;
}
.result-area .panel-header { position:sticky; top:0; z-index:2; }
.diff-line {
  display:flex; padding:2px 12px; font-family:var(--font-mono);
  font-size:0.78rem; line-height:1.6; border-bottom:1px solid #f0f0f0;
}
.diff-line .line-num {
  min-width:36px; text-align:right; color:#999;
  font-size:0.7rem; padding-right:8px; user-select:none;
}
.diff-line.added { background: #f0fff0; }
.diff-line.added .line-num { color: #000; }
.diff-line.removed { background: #fff0f0; }
.diff-line.removed .line-num { color: #000; }
.stats {
  display:flex; gap:16px; padding:8px 16px;
  border-top: 1px solid var(--border);
  background: #fafafa; font-size:0.78rem; flex-shrink:0;
}
.stat-item { color: var(--text-light); }
.stat-val { font-weight:600; font-family:var(--font-mono); }
.stat-val.added { color: var(--success); }
.stat-val.removed { color: var(--danger); }
.stat-val.same { color: var(--text); }""",

    "regex-tester.html": """
/* 正则表达式测试器专用样式 */
.main { flex:1; display:grid; grid-template-columns: 1fr 1fr; min-height:0; overflow:hidden; }
.regex-panel, .test-panel {
  display:flex; flex-direction:column; overflow:hidden;
}
.regex-panel { border-right: 1px solid var(--border); }
.panel-header {
  padding:8px 14px; font-size:0.72rem; font-weight:600; background:#fafafa;
  border-bottom:1px solid var(--border); display:flex; align-items:center;
  justify-content:space-between; flex-shrink:0;
}
.panel-header label { font-size:0.7rem; color:var(--text-light); }
.regex-input-row {
  display:flex; align-items:center; gap:6px; padding:8px 12px;
  border-bottom: 1px solid var(--border); flex-shrink:0;
}
.regex-input-row input {
  flex:1; padding:6px 10px; border:1px solid var(--border);
  font-family:var(--font-mono); font-size:0.85rem; background:#fff; color:var(--text);
}
.regex-input-row input:focus { border-width:2px; }
.regex-input-row input.invalid { border-color: var(--danger); background: #fff5f5; }
.flag-row {
  display:flex; gap:6px; padding:4px 12px; align-items:center;
  border-bottom: 1px solid var(--border); flex-shrink:0;
}
.flag-btn {
  padding:2px 8px; border:1px solid var(--border); background:#fff;
  color:var(--text-light); font-size:0.72rem; cursor:pointer;
  font-family:var(--font-mono); transition: all 0.15s;
}
.flag-btn:hover { background: var(--accent); color: #fff; }
.flag-btn.active { background: var(--accent); color: #fff; }
.test-panel textarea {
  flex:1; padding:14px; border:none; background:#fff;
  font-family:var(--font-mono); font-size:0.85rem; line-height:1.6;
  resize:none; outline:none; color:var(--text);
}
.test-panel textarea::placeholder { color: #999; }
.result-area {
  height:200px; overflow-y:auto; border-top:1px solid var(--border);
  background:#fafafa; flex-shrink:0;
}
.result-area .panel-header { position:sticky; top:0; z-index:2; }
.match-highlight {
  background: #ff0; color: var(--text); padding:0 1px;
}
.match-item {
  padding:4px 14px; font-family:var(--font-mono); font-size:0.8rem;
  border-bottom:1px solid #f0f0f0; line-height:1.5;
}
.match-index { color:#999; font-size:0.68rem; margin-right:8px; }
.match-group { color: var(--text); font-size:0.72rem; margin-top:2px; padding-left:20px; }
.preset-section {
  padding:8px 12px; border-bottom:1px solid var(--border); flex-shrink:0;
  background:#fafafa;
}
.preset-label { font-size:0.65rem; font-weight:600; color:var(--text-light); text-transform:uppercase;
  letter-spacing:0.5px; margin-bottom:4px; }
.preset-row { display:flex; flex-wrap:wrap; gap:4px; }
.preset-tag {
  padding:2px 8px; border:1px solid var(--border); font-size:0.68rem;
  cursor:pointer; background:#fff; color:var(--text);
  font-family:var(--font-mono); white-space:nowrap;
}
.preset-tag:hover { background:var(--accent); color:#fff; }""",

    "base64-tool.html": """
/* Base64 编解码工具专用样式 */
.tab-content { display:none; flex:1; flex-direction:column; overflow:hidden; }
.tab-content.active { display:flex; }
.text-area { flex:1; display:flex; flex-direction:column; gap:10px; padding:16px; }
#base64Input {
  flex:1; padding:12px; border:1px solid var(--border);
  background:#fff; color:var(--text);
  font-family:var(--font-mono); font-size:0.85rem; line-height:1.6;
  resize:none; outline:none;
}
#base64Input:focus { border-width:2px; }
#base64Input::placeholder { color:#999; }
.base64-output {
  padding:12px; border:1px solid var(--border);
  background:#fafafa; font-family:var(--font-mono);
  font-size:0.82rem; min-height:60px; max-height:160px;
  overflow-y:auto; word-break:break-all; line-height:1.5;
  color:var(--text);
}
.result-hint {
  color:var(--text-light); font-size:0.75rem;
  display:flex; align-items:center; gap:4px;
}
.image-area { flex:1; display:flex; flex-direction:column; overflow:hidden; }
.dropzone {
  margin:16px; min-height:200px; border:2px dashed var(--border);
  display:flex; flex-direction:column; align-items:center;
  justify-content:center; cursor:pointer; background:#fafafa;
  transition:all 0.2s;
}
.dropzone:hover { border-color:var(--accent); background:#f5f5f5; }
.dropzone .dz-icon { font-size:2rem; margin-bottom:8px; }
.dropzone .dz-text { color:var(--text-light); font-size:0.85rem; }
.image-preview-area {
  flex:1; display:flex; align-items:center; justify-content:center;
  padding:12px; overflow:auto;
}
.image-preview-area img { max-width:100%; max-height:300px; border:1px solid var(--border); }
.image-base64-output {
  padding:10px 14px; margin:8px 16px 16px;
  border:1px solid var(--border); font-family:var(--font-mono);
  font-size:0.72rem; background:#fafafa; max-height:120px;
  overflow-y:auto; word-break:break-all; line-height:1.4; color:var(--text);
}""",

    "qrcode-tool.html": """
/* 二维码生成器专用样式 */
.main { flex:1; display:flex; flex-direction:column; overflow:hidden; gap:0; padding:0; }
.input-row {
  display:flex; gap:8px; padding:12px 16px; align-items:center;
  border-bottom:1px solid var(--border); flex-shrink:0;
}
#qrInput {
  flex:1; padding:8px 12px; border:1px solid var(--border);
  font-size:0.9rem; background:#fff; color:var(--text);
  font-family:inherit;
}
#qrInput:focus { border-width:2px; }
.control-row {
  display:flex; gap:12px; padding:8px 16px; align-items:center;
  border-bottom:1px solid var(--border); flex-shrink:0;
}
.control-row label { font-size:0.75rem; color:var(--text-light); white-space:nowrap; }
.control-row input[type=range] { width:120px; accent-color:var(--accent); }
.control-row span { font-size:0.72rem; color:var(--text-light); min-width:36px; text-align:right; font-family:var(--font-mono); }
.qr-display {
  flex:1; display:flex; align-items:center; justify-content:center;
  padding:20px; overflow:auto;
}
.qr-display canvas { border:2px solid var(--border); }
.qr-info {
  padding:8px 16px; font-size:0.72rem; color:var(--text-light);
  border-top:1px solid var(--border); display:flex; gap:16px; flex-shrink:0;
}""",

    "screenshot-tool.html": """
/* 截图笔记工具专用样式 */
.main { flex:1; display:flex; overflow:hidden; min-height:0; }
.toolbar {
  display:flex; flex-direction:column; gap:6px; padding:10px;
  background:#fafafa; border-right:1px solid var(--border);
  flex-shrink:0; min-width:52px; align-items:center;
}
.tool-btn {
  width:36px; height:36px; border:1px solid var(--border);
  background:#fff; cursor:pointer; display:flex;
  align-items:center; justify-content:center;
  font-size:1rem; transition:all 0.1s; color:var(--text);
}
.tool-btn:hover { background:var(--accent); color:#fff; }
.tool-btn.active { background:var(--accent); color:#fff; border-width:2px; }
.color-bar { display:flex; gap:2px; }
.color-dot {
  width:16px; height:16px; border:1px solid var(--border);
  cursor:pointer; transition:all 0.1s;
}
.color-dot:hover { transform:scale(1.2); }
.color-dot.active { border-width:2px; }
.canvas-area {
  flex:1; display:flex; align-items:center; justify-content:center;
  background:#fafafa; overflow:auto; position:relative;
}
.canvas-area canvas { border:1px solid var(--border); background:#fff; cursor:crosshair; }
.drop-hint {
  position:absolute; color:var(--text-light); font-size:0.85rem;
  pointer-events:none; user-select:none;
}""",

    "markdown-editor.html": """
/* Markdown 编辑器专用样式 */
.main { flex:1; display:grid; grid-template-columns: 1fr 1fr; min-height:0; overflow:hidden; }
.md-panel { display:flex; flex-direction:column; overflow:hidden; }
.md-panel:first-child { border-right:1px solid var(--border); }
.panel-header {
  padding:8px 14px; font-size:0.72rem; font-weight:600; background:#fafafa;
  border-bottom:1px solid var(--border); display:flex; align-items:center;
  justify-content:space-between; flex-shrink:0;
}
.md-panel textarea {
  flex:1; padding:14px; border:none; background:#fff;
  font-family:var(--font-mono); font-size:0.85rem; line-height:1.7;
  resize:none; outline:none; color:var(--text);
}
.md-panel textarea::placeholder { color:#999; }
.md-preview {
  flex:1; padding:16px; overflow-y:auto; background:#fff; word-wrap:break-word;
}
.md-preview p { margin:6px 0; }
.md-preview h1 { font-size:1.5rem; border-bottom:2px solid var(--border); padding-bottom:6px; margin:16px 0 10px; }
.md-preview h2 { font-size:1.25rem; border-bottom:1px solid var(--border); padding-bottom:4px; margin:14px 0 8px; }
.md-preview h3 { font-size:1.1rem; margin:12px 0 6px; }
.md-preview h4, .md-preview h5, .md-preview h6 { font-size:1rem; margin:10px 0 6px; color:#555; }
.md-preview ul, .md-preview ol { padding-left:22px; margin:6px 0; }
.md-preview li { margin:2px 0; }
.md-preview blockquote {
  border-left:4px solid var(--border); padding:6px 14px; margin:8px 0;
  background:#fafafa; color:#555;
}
.md-preview code {
  background:#f0f0f0; padding:2px 6px; font-family:var(--font-mono);
  font-size:0.88em; color:var(--text);
}
.md-preview pre {
  background:#fafafa; border:1px solid var(--border);
  padding:14px 16px; overflow-x:auto; margin:8px 0; line-height:1.5;
}
.md-preview pre code { background:none; padding:0; font-size:0.82rem; color:var(--text); }
.md-preview a { color:var(--text); text-decoration:underline; }
.md-preview img { max-width:100%; margin:6px 0; }
.md-preview hr { border:none; border-top:1px solid var(--border); margin:16px 0; }
.md-preview table { border-collapse:collapse; width:100%; margin:8px 0; }
.md-preview th, .md-preview td { border:1px solid var(--border); padding:6px 10px; text-align:left; }
.md-preview th { background:#f5f5f5; font-weight:600; }
.md-preview strong { color:var(--text); }""",

    "json-formatter.html": """
/* JSON 格式化工具专用样式 */
.main { flex:1; display:flex; flex-direction:column; overflow:hidden; padding:0; }
.input-section, .output-section { display:flex; flex-direction:column; overflow:hidden; }
.input-section { flex:3; }
.output-section { flex:2; border-top:1px solid var(--border); }
.panel-header {
  padding:8px 14px; font-size:0.72rem; font-weight:600; background:#fafafa;
  border-bottom:1px solid var(--border); display:flex; align-items:center;
  justify-content:space-between; flex-shrink:0;
}
#jsonInput {
  flex:1; padding:14px; border:none; background:#fff;
  font-family:var(--font-mono); font-size:0.85rem; line-height:1.6;
  resize:none; outline:none; color:var(--text);
}
#jsonInput::placeholder { color:#999; }
#jsonOutput {
  flex:1; padding:14px; border:none; background:#fafafa;
  font-family:var(--font-mono); font-size:0.82rem; line-height:1.5;
  resize:none; outline:none; overflow-y:auto; color:var(--text);
  white-space:pre-wrap; word-break:break-all;
}
.json-stats {
  display:flex; gap:12px; padding:4px 14px; font-size:0.72rem;
  color:var(--text-light); flex-shrink:0;
}
.json-stats .error { color:var(--danger); }
.indent-row {
  display:flex; align-items:center; gap:4px;
}
.indent-row label { font-size:0.7rem; color:var(--text-light); }
.indent-row select {
  padding:2px 4px; border:1px solid var(--border);
  font-size:0.72rem; background:#fff; color:var(--text);
}""",

    "color-picker.html": """
/* 颜色拾取器专用样式 */
.main { flex:1; display:flex; overflow:hidden; min-height:0; }
.picker-side {
  width:280px; display:flex; flex-direction:column; padding:16px;
  gap:14px; background:#fafafa; border-right:1px solid var(--border);
  overflow-y:auto; flex-shrink:0;
}
.preview-block {
  width:120px; height:120px; border:2px solid var(--border);
  margin:0 auto; align-self:center;
  transition:background 0.15s;
}
.color-input-native {
  width:100%; height:36px; border:1px solid var(--border); cursor:pointer; background:none;
}
.value-row {
  display:flex; align-items:center; gap:6px; font-size:0.78rem;
}
.value-row label { width:32px; font-weight:600; color:var(--text-light); flex-shrink:0; }
.value-row input {
  flex:1; padding:4px 8px; border:1px solid var(--border);
  font-family:var(--font-mono); font-size:0.78rem; background:#fff; color:var(--text);
}
.value-row input:focus { border-width:2px; }
.palette-side { flex:1; overflow-y:auto; padding:12px 16px; }
.palette-section { margin-bottom:16px; }
.palette-label {
  font-size:0.7rem; font-weight:600; color:var(--text-light);
  text-transform:uppercase; letter-spacing:0.5px; margin-bottom:6px;
}
.palette-grid {
  display:grid; grid-template-columns: repeat(auto-fill, minmax(36px,1fr));
  gap:4px;
}
.palette-swatch {
  width:100%; aspect-ratio:1; border:1px solid var(--border);
  cursor:pointer; transition:all 0.1s;
}
.palette-swatch:hover { border-width:2px; transform:scale(1.1); }""",

    "timer.html": """
/* 计时器专用样式 */
.main { flex:1; display:flex; flex-direction:column; overflow-y:auto; padding:0; }
.mode-row {
  display:flex; gap:4px; padding:12px 16px 0; flex-shrink:0;
}
.timer-display-area {
  display:flex; flex-direction:column; align-items:center;
  padding:30px 16px; flex-shrink:0;
}
.timer-display {
  font-family:var(--font-mono); font-size:4rem; font-weight:700;
  color:var(--text); letter-spacing:3px; line-height:1;
}
.timer-display.warning { color: var(--danger); }
.timer-display.danger { color: var(--danger); animation: blink 0.6s infinite; }
@keyframes blink { 0%,100%{opacity:1;} 50%{opacity:0.3;} }
.timer-label { font-size:0.78rem; color:var(--text-light); margin-top:6px; }
.timer-progress {
  width:200px; height:4px; background:#eee; margin-top:10px;
}
.timer-progress-bar { height:100%; background:var(--accent); transition:width 0.3s; }
.input-row {
  display:flex; gap:4px; justify-content:center; align-items:center;
  padding:0 16px 12px; flex-shrink:0;
}
.input-row input {
  width:56px; padding:8px 4px; border:1px solid var(--border);
  font-size:1.1rem; text-align:center; font-family:var(--font-mono);
  background:#fff; color:var(--text);
}
.input-row input:focus { border-width:2px; }
.input-row span { font-size:0.75rem; color:var(--text-light); }
.control-row {
  display:flex; gap:10px; justify-content:center; padding:0 16px 12px;
  flex-shrink:0; flex-wrap:wrap;
}
.preset-row {
  display:flex; gap:4px; justify-content:center; padding:0 16px 12px;
  flex-shrink:0; flex-wrap:wrap;
}
.sequence-area {
  padding:0 16px; flex-shrink:0; display:flex; flex-direction:column; gap:6px;
}
.seq-item {
  display:flex; align-items:center; gap:6px; padding:6px 10px;
  background:#fafafa; border:1px solid var(--border);
  font-size:0.8rem;
}
.seq-item span { font-family:var(--font-mono); min-width:40px; }
.seq-item input {
  width:50px; padding:2px 4px; border:1px solid var(--border);
  font-family:var(--font-mono); font-size:0.78rem; background:#fff; color:var(--text);
}
.seq-item button { background:none; border:none; color:var(--text-light); cursor:pointer; font-size:0.9rem; }
.seq-item button:hover { color:var(--danger); }""",
}

def append_css_to_file(filepath, extra_css):
    """在 </style> 之前追加专用 CSS"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 在 </style> 之前插入
    if extra_css not in content:
        # 找到最后一个 .toast 或 .error 样式后的位置，在 </style> 前插入
        marker = '}\n</style>'
        if marker in content:
            content = content.replace(marker, '}\n' + extra_css + '\n</style>')
        else:
            # fallback
            content = content.replace('</style>', extra_css + '\n</style>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filename, css in TOOL_EXTRA_CSS.items():
    filepath = os.path.join(APPS_DIR, filename)
    if os.path.exists(filepath):
        print(f"追加CSS: {filename}")
        append_css_to_file(filepath, css)
    else:
        print(f"文件不存在: {filename}")

print("\n全部专属CSS追加完毕!")
