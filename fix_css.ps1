# Fix missing CSS in mini-tools apps
$ErrorActionPreference = "Stop"

$sharedCSS = @'
/* === Auto-fix: shared utility styles === */
.toolbar {
  display: flex; align-items: center; gap: 6px; padding: 6px 16px;
  flex-shrink: 0; border-bottom: 1px solid var(--border); background: #fafafa;
  flex-wrap: wrap;
}
.toolbar-btn {
  padding: 4px 10px; border: 1px solid var(--border); background: #fff;
  color: var(--text); font-size: 0.78rem; cursor: pointer;
  font-family: inherit; transition: all 0.1s;
}
.toolbar-btn:hover { background: var(--accent); color: #fff; }
.toolbar-sep { width: 1px; height: 20px; background: var(--border); margin: 0 2px; }
.toolbar-hint { font-size: 0.7rem; color: var(--text-light); margin-left: auto; }
.titlebar-btn {
  padding: 4px 10px; border: 1px solid var(--border); background: #fff;
  color: var(--text); font-size: 0.78rem; cursor: pointer;
  font-family: inherit; transition: all 0.1s;
}
.titlebar-btn:hover { background: var(--accent); color: #fff; }
.accent { background: var(--accent); color: #fff; }
.btn.danger { color: var(--danger); border-color: var(--danger); }
.btn.danger:hover { background: var(--danger); color: #fff; }
.stats {
  display: flex; gap: 16px; padding: 6px 16px; font-size: 0.72rem;
  color: var(--text-light); flex-shrink: 0; border-top: 1px solid var(--border);
  background: #fafafa;
}
.stat-item { display: flex; align-items: center; gap: 4px; }
.stat-val { color: var(--text); font-weight: 600; font-family: var(--font-mono); }
.statusbar {
  display: flex; align-items: center; gap: 12px; padding: 6px 16px;
  font-size: 0.72rem; color: var(--text-light);
  border-top: 1px solid var(--border); background: #fafafa; flex-shrink: 0;
}
.status-item { display: flex; align-items: center; gap: 4px; }
.status-count { color: var(--text); font-weight: 600; }
.context-menu {
  position: fixed; background: #fff; border: 1px solid var(--border);
  padding: 6px 0; z-index: 1000; display: none; min-width: 160px;
  box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
}
.context-menu.show { display: block; }
.context-item {
  padding: 8px 16px; font-size: 0.82rem; cursor: pointer;
  display: flex; align-items: center; justify-content: space-between;
  transition: background 0.1s;
}
.context-item:hover { background: #f0f0f0; }
.context-shortcut { font-size: 0.7rem; color: var(--text-light); }
.editor-area { display: flex; flex-direction: column; overflow: hidden; flex: 1; }
.result-area { display: flex; flex-direction: column; overflow: hidden; }
.panel-body { flex: 1; display: flex; overflow: hidden; }
.divider {
  width: 4px; cursor: col-resize; background: #f0f0f0;
  transition: background 0.15s; flex-shrink: 0;
}
.divider:hover, .divider.active { background: var(--border); }
.drop-highlight { border: 2px dashed var(--accent) !important; background: #fafafa !important; }
.info { padding: 14px; color: var(--text-light); font-size: 0.82rem; }
.indent-select {
  padding: 2px 6px; border: 1px solid var(--border); background: #fff;
  color: var(--text); font-size: 0.75rem; font-family: inherit;
}
.valid { border-color: #000 !important; }
.invalid { border-color: var(--danger) !important; }
.error-msg { color: var(--danger); font-size: var(--font-mono); padding: 4px 0; }
.no-match { color: var(--text-light); font-size: 0.85rem; }
/* regex-tester */
.regex-row {
  display: flex; align-items: center; gap: 8px; padding: 8px 16px;
  flex-shrink: 0; border-bottom: 1px solid var(--border); background: #fafafa;
}
.regex-row input { flex: 1; padding: 6px 10px; border: 1px solid var(--border); font-family: var(--font-mono); font-size: 0.85rem; }
.flag-options { display: flex; gap: 4px; }
.flag-options .btn { padding: 3px 10px; font-size: 0.75rem; }
.flag-options .btn.active { background: var(--accent); color: #fff; }
.editor-wrap { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
.editor-wrap textarea { flex: 1; padding: 12px; border: none; border-top: 1px solid var(--border); font-family: var(--font-mono); font-size: 0.85rem; resize: none; outline: none; }
.presets { display: flex; gap: 4px; padding: 6px 16px; flex-shrink: 0; flex-wrap: wrap; border-bottom: 1px solid var(--border); }
.preset-btn { padding: 3px 10px; border: 1px solid var(--border); background: #fff; color: var(--text); font-size: 0.72rem; cursor: pointer; font-family: inherit; }
.preset-btn:hover { background: var(--accent); color: #fff; }
.match-text { color: var(--text); font-weight: 600; }
.match-groups { font-family: var(--font-mono); font-size: 0.78rem; color: var(--text-light); }
/* screenshot-tool */
.tool-group { display: flex; gap: 2px; }
.tool-label { font-size: 0.7rem; color: var(--text-light); margin-bottom: 2px; }
.stroke-select { padding: 2px 4px; border: 1px solid var(--border); font-size: 0.72rem; }
.selected { background: var(--accent) !important; color: #fff !important; }
.canvas-container {
  flex: 1; display: flex; align-items: center; justify-content: center;
  background: #f0f0f0; overflow: hidden; position: relative;
}
.canvas-placeholder { color: var(--text-light); font-size: 1.2rem; }
/* color-picker */
.color-preview {
  width: 100%; height: 120px; border: 1px solid var(--border);
  cursor: pointer; transition: background 0.2s;
}
.picker-section { display: flex; flex-direction: column; gap: 10px; }
.mid-section { display: flex; gap: 10px; }
.right-section { display: flex; flex-direction: column; gap: 10px; flex: 1; }
.color-row { display: flex; align-items: center; gap: 8px; }
.color-values { display: flex; flex-direction: column; gap: 4px; }
.section-title { font-size: 0.72rem; font-weight: 600; color: var(--text-light); text-transform: uppercase; letter-spacing: 0.5px; }
.info-block { font-size: 0.78rem; line-height: 1.6; color: var(--text); }
.info-block .key { font-weight: 600; }
.favorites-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(40px, 1fr)); gap: 4px; }
.card { background: #fff; border: 1px solid var(--border); padding: 8px; font-size: 0.75rem; }
.export-preview { display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 16px; background: #fafafa; border: 1px solid var(--border); }
.eyedropper-overlay { position: fixed; inset: 0; z-index: 999; cursor: crosshair; }
.eyedropper-magnifier { width: 30px; height: 30px; border: 2px solid var(--border); border-radius: 50%; box-shadow: 0 0 8px rgba(0,0,0,0.3); }
.eyedropper-label { font-size: 0.75rem; color: var(--text-light); }
/* base64-tool */
.text-panel { display: flex; flex-direction: column; overflow: hidden; }
.text-row { display: flex; gap: 8px; padding: 8px 16px; flex-shrink: 0; }
.text-actions { display: flex; gap: 4px; }
.img-panel { display: flex; flex-direction: column; overflow: hidden; }
.img-actions { display: flex; gap: 4px; padding: 8px 16px; flex-shrink: 0; }
.col-header { font-size: 0.78rem; font-weight: 600; padding: 8px 16px; background: #fafafa; border-bottom: 1px solid var(--border); flex-shrink: 0; }
.col-body { flex: 1; overflow: hidden; display: flex; }
.text-col { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
.img-result { max-width: 100%; max-height: 300px; object-fit: contain; }
.img-dropzone {
  flex: 1; min-height: 160px; border: 2px dashed var(--border);
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  cursor: pointer; transition: all 0.2s; background: #fafafa; margin: 8px;
}
.img-dropzone:hover { border-color: var(--accent); background: #f5f5f5; }
.placeholder { color: var(--text-light); font-size: 0.85rem; }
/* qrcode-tool */
.input-section { display: flex; gap: 8px; padding: 12px 16px; flex-shrink: 0; }
.input-section textarea { flex: 1; padding: 10px; border: 1px solid var(--border); font-family: var(--font-mono); font-size: 0.85rem; resize: none; min-height: 60px; }
.qr-section {
  flex: 1; display: flex; align-items: center; justify-content: center;
  background: #fafafa; overflow: hidden;
}
.qr-placeholder { color: var(--text-light); font-size: 1.1rem; }
.size-row { display: flex; align-items: center; gap: 8px; padding: 8px 16px; flex-shrink: 0; }
/* timer */
.mode-tabs { display: flex; border-bottom: 1px solid var(--border); flex-shrink: 0; }
.mode-tab {
  padding: 8px 18px; border: none; border-right: 1px solid var(--border);
  background: #fafafa; color: var(--text-light); font-size: 0.85rem;
  cursor: pointer; font-family: inherit;
}
.mode-tab:hover { color: var(--text); }
.mode-tab.active { background: #fff; color: var(--text); font-weight: 600; }
.controls { display: flex; justify-content: center; gap: 8px; padding: 12px; flex-shrink: 0; }
.control-btn {
  padding: 8px 18px; border: 1px solid var(--border); background: #fff;
  color: var(--text); font-size: 0.85rem; cursor: pointer; font-family: inherit;
}
.control-btn:hover { background: var(--accent); color: #fff; }
.control-btn.start { background: var(--accent); color: #fff; }
.control-btn.pause { background: #f5f5f5; }
.control-btn.reset { color: var(--danger); }
.settings-row { display: flex; align-items: center; gap: 12px; padding: 8px 16px; flex-shrink: 0; }
.time-input-row { display: flex; align-items: center; gap: 8px; }
.time-input-row input { width: 60px; padding: 4px 8px; border: 1px solid var(--border); font-family: var(--font-mono); font-size: 0.85rem; text-align: center; }
.progress-bar { height: 4px; background: #f0f0f0; flex-shrink: 0; }
.progress-fill { height: 100%; background: var(--accent); transition: width 0.3s; }
.pomodoro-section { display: flex; flex-direction: column; gap: 8px; padding: 8px 16px; }
.phase-list { display: flex; flex-direction: column; gap: 4px; }
.phase-name { font-size: 0.8rem; color: var(--text); font-weight: 500; }
.phase-time { font-size: 0.72rem; color: var(--text-light); font-family: var(--font-mono); }
.phase-status { font-size: 0.7rem; }
.phase-icon { margin-right: 4px; }
.add-phase-form { display: flex; gap: 6px; align-items: center; padding: 8px 0; }
.add-phase-form input { padding: 4px 8px; border: 1px solid var(--border); font-size: 0.78rem; width: 100px; }
.shortcut-hint { font-size: 0.65rem; color: var(--text-light); text-align: center; padding: 4px; }
/* json formatter result types */
.success { color: var(--text); }
.error { color: var(--danger); }
/* base64 image dropzone text cols */
.img-dropzone .dz-icon { font-size: 2.5rem; }
.img-dropzone .dz-text { color: var(--text-light); font-size: 0.85rem; }
'@

function InjectCSS($filePath) {
    $content = Get-Content $filePath -Raw -Encoding UTF8
    $name = Split-Path $filePath -Leaf
    
    # Insert before first closing </style> tag
    if ($content -match '</style>') {
        $idx = $content.LastIndexOf('</style>')
        if ($idx -gt 0) {
            # Check which missing classes are actually used in the body
            $newContent = $content.Substring(0, $idx) + "`n" + $sharedCSS + "`n" + $content.Substring($idx)
            [System.IO.File]::WriteAllText($filePath, $newContent, (New-Object System.Text.UTF8Encoding $false))
            Write-Host "  Fixed: $name"
            return $true
        }
    }
    Write-Host "  SKIP: $name (no </style> found)"
    return $false
}

$appsDir = "D:\GitHub\mini-tools\apps"
$files = Get-ChildItem "$appsDir\*.html"
$count = 0

foreach ($f in $files) {
    if (InjectCSS $f.FullName) { $count++ }
}

Write-Host "`n=== Done: injected CSS into $count files ==="
