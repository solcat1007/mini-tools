# Create GitHub repos for all mini-tools (ASCII-safe version)
$ErrorActionPreference = "Continue"
$baseDir = "D:\GitHub\mini-tools"
$appsDir = "$baseDir\apps"
$buildDir = "$baseDir\_repos"

if (Test-Path $buildDir) { Remove-Item $buildDir -Recurse -Force }
New-Item -ItemType Directory -Path $buildDir -Force | Out-Null

$tools = @(
    @{file="base64-tool.html";     name="base64-tool";      desc="Base64 encode/decode tool - text & image conversion"},
    @{file="color-picker.html";    name="color-picker";     desc="Color picker - HEX/RGB/HSL conversion, palette, favorites"},
    @{file="css-gradient.html";    name="css-gradient-tool"; desc="CSS gradient generator - linear/radial/conic visualization"},
    @{file="css-shadow.html";      name="css-shadow-tool";   desc="CSS box-shadow generator - multi-layer visual editor"},
    @{file="hash-tool.html";       name="hash-tool";         desc="Hash calculator - MD5/SHA-1/SHA-256/SHA-512 for text & files"},
    @{file="json-formatter.html";  name="json-formatter";    desc="JSON formatter - format/compact/validate/escape/sort keys"},
    @{file="markdown-editor.html"; name="markdown-editor";   desc="Markdown editor - live preview, toolbar, export MD/HTML"},
    @{file="qrcode-tool.html";     name="qrcode-tool";       desc="QR code generator - text/URL to QR, custom size/color, PNG export"},
    @{file="regex-tester.html";    name="regex-tester";      desc="Regex tester - real-time match highlighting, capture groups, presets"},
    @{file="screenshot-tool.html"; name="screenshot-tool";   desc="Screenshot annotator - canvas drawing with arrows/shapes/blur"},
    @{file="text-counter.html";    name="text-counter";      desc="Text counter - word/char/line/paragraph stats, reading time estimate"},
    @{file="text-diff.html";       name="text-diff";         desc="Text diff tool - LCS-based line comparison, side-by-side view"},
    @{file="timer.html";           name="timer-tool";        desc="Timer - countdown/stopwatch/pomodoro modes, notification + sound"},
    @{file="uuid-generator.html";  name="uuid-generator";    desc="UUID generator - v1/v4/NIL, batch generation, one-click copy"}
)

$total = $tools.Count
$i = 0

foreach ($t in $tools) {
    $i++
    $toolFile = $t.file
    $toolName = $t.name
    $toolDesc = $t.desc
    $srcPath = Join-Path $appsDir $toolFile
    $repoDir = Join-Path $buildDir $toolName
    
    Write-Host "[$i/$total] Creating $toolName ..."
    
    New-Item -ItemType Directory -Path $repoDir -Force | Out-Null
    Copy-Item $srcPath "$repoDir\index.html"
    
    $readme = @"
# $toolName

$toolDesc

## Features

Pure frontend tool - no server required, open in browser and use.

## Usage

1. Download `index.html`
2. Open in browser
3. Start using!

Or visit GitHub Pages (if configured).

## Tech Stack

- Pure HTML/CSS/JavaScript
- Zero dependencies, no build tools
- White minimalist theme design

## License

MIT
"@
    $utf8 = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText("$repoDir\README.md", $readme, $utf8)
    [System.IO.File]::WriteAllText("$repoDir\.gitignore", ".DS_Store`nThumbs.db`n*.log`n", $utf8)
    
    Push-Location $repoDir
    git init 2>&1 | Out-Null
    git add -A 2>&1 | Out-Null
    git commit -m "Initial commit: $toolName" 2>&1 | Out-Null
    
    $result = gh repo create "solcat1007/$toolName" --public --source=. --remote=origin --push 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  OK: https://github.com/solcat1007/$toolName"
    } else {
        Write-Host "  FAIL: $result"
    }
    
    Pop-Location
}

Write-Host "`nDone: processed $i repos"
