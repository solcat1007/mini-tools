"""
批量转换所有 mini-tools HTML 文件：
1. CSS 全部改为白色极简主题（白底黑字黑边框）
2. 每个文件添加可折叠的"使用说明"区域
3. 确保所有界面文字为中文
"""
import os, re, json

APPS_DIR = r"D:\GitHub\mini-tools\apps"

# 各工具的使用说明
HELP_TEXT = {
    "markdown-editor.html": """### Markdown 编辑器
实时预览的 Markdown 编辑器，左右分栏设计。

**主要功能**
- 左侧编写 Markdown，右侧实时渲染预览
- 支持标题、加粗、斜体、代码块、表格、引用等常用语法
- 工具栏快捷插入：加粗/斜体/删除线/代码/标题/引用/列表/链接
- 右键菜单快速操作
- 实时统计字数、行数、字符数
- 导出 .md 和 .html 文件

**快捷键**
| 快捷键 | 功能 |
|--------|------|
| Ctrl+S | 导出 .md 文件 |
| Ctrl+Shift+E | 导出 .html 文件 |
| Ctrl+O | 打开文件 |
| Ctrl+B | 加粗 |
| Ctrl+I | 斜体 |

**注意事项**
- 代码块使用三个反引号包裹，支持语言标注
- 拖拽 .md/.txt 文件到编辑区可直接导入""",

    "json-formatter.html": """### JSON 格式化工具
JSON 格式化、压缩、校验、排序工具。

**主要功能**
- 格式化：美化 JSON 输出，可选缩进级别
- 压缩：去除空格和换行，生成紧凑 JSON
- 校验：检查 JSON 格式是否合法，显示顶层类型和键数量
- 转义/反转义：将文本转为 JSON 字符串字面量或还原
- 排序键：按字母顺序递归排列对象键

**快捷键**
| 快捷键 | 功能 |
|--------|------|
| Ctrl+Enter | 格式化 |
| Ctrl+K | 压缩 |
| Ctrl+L | 清空 |
| Ctrl+Shift+S | 按字母排序键 |

**注意事项**
- 如果 JSON 解析失败，错误信息会显示在结果区域
- 拖拽 .json 文件到编辑区可直接导入""",

    "color-picker.html": """### 颜色拾取器
颜色选择与调色板管理工具，支持屏幕取色。

**主要功能**
- 系统颜色选择器 + 屏幕取色（EyeDropper API）
- 自动转换并显示 HEX / RGB / HSL 值
- 点击任意值字段可复制对应格式
- 内置常用色、暖色系、冷色系、自然色四组预设
- 点击预设色块即可切换当前颜色

**快捷键**
| 快捷键 | 功能 |
|--------|------|
| Ctrl+C | 复制当前 HEX 值 |
| Ctrl+D | 收藏当前颜色 |

**注意事项**
- 屏幕取色功能需要 Chrome 95+ 浏览器支持
- 点击预览色块或数值字段即可复制""",

    "timer.html": """### 计时器
多功能计时器，支持倒计时、秒表、番茄钟三种模式。

**主要功能**
- 倒计时：设置时/分/秒，支持 1~60 分钟预设
- 秒表：从 0 开始正向计时
- 番茄钟：多阶段序列计时，可自定义添加/移除阶段
- 进度条显示剩余时间比例
- 最后10秒警告色提示
- 浏览器桌面通知 + Web Audio 提示音
- 全屏模式

**快捷键**
| 快捷键 | 功能 |
|--------|------|
| Space | 开始 / 暂停 |
| R | 重置 |
| ← / → | 切换模式 |
| F | 全屏 |

**注意事项**
- 定时器在后台标签页中可能降速，建议保持页面可见""",

    "text-diff.html": """### 文本差异对比
逐行对比两段文本的差异，基于 LCS 算法高亮差异行。

**主要功能**
- 左侧原始文本、右侧修改文本，实时逐行对比
- 新增行绿色标记、删除行红色标记
- 支持忽略大小写、忽略空白字符
- 一键交换左右两侧文本
- 底部实时统计新增/删除/相同行数

**快捷键**
| 快捷键 | 功能 |
|--------|------|
| Ctrl+Enter | 执行对比 |
| Ctrl+Shift+X | 交换两侧 |

**注意事项**
- 对比基于逐行匹配，适合代码和纯文本
- 忽略空白选项会去除行内所有空格后再比较""",

    "regex-tester.html": """### 正则表达式测试器
在线正则表达式测试工具，实时高亮匹配并展示捕获组。

**主要功能**
- 输入正则表达式和测试文本，实时高亮所有匹配项
- 支持 g/i/m/s/u 五种正则标志
- 展示每个匹配项的捕获组详情（$1/$2...）
- 内置邮箱/手机号/URL/日期/IP 等常用正则预设
- 正则语法错误时红框提示

**注意事项**
- 复杂正则在长文本上可能卡顿，建议先用小段文本测试
- 点击预设可直接填入正则表达式""",

    "base64-tool.html": """### Base64 编解码工具
Base64 编解码工具，支持文本和图片双模式。

**主要功能**
- 文本编码：普通文本 → Base64 编码
- 文本解码：Base64 → 普通文本（自动处理 UTF-8）
- 图片编码：拖拽/点击上传图片，自动生成 Base64 字符串
- 图片解码：粘贴 Base64 后还原图片预览
- 下载图片：将 Base64 编码的图片下载为 PNG

**注意事项**
- Base64 编码会使数据膨胀约 33%
- 大图片编码可能耗时，建议小于 5MB""",

    "qrcode-tool.html": """### 二维码生成器
纯前端二维码生成器，基于 Canvas 实时绘制 QR 码。

**主要功能**
- 输入文本/URL 后实时生成二维码
- 纯 Canvas 绘制，完整 QR 码生成引擎
- 滑块调节输出尺寸（150~500px）
- 一键下载 PNG 图片
- 支持中文/英文/数字/URL
- 显示当前 QR 版本和模块信息

**注意事项**
- 内容越长，QR 码版本越高、模块越密
- 建议内容不超过 500 个字符以保证可读性""",

    "screenshot-tool.html": """### 截图笔记工具
简易截图标注工具，粘贴截图后添加标注并导出。

**主要功能**
- Ctrl+V 从剪贴板粘贴截图到画布
- 6 种标注工具：箭头、矩形、椭圆、画笔、文字、马赛克
- 7 种颜色 + 5 级线条粗细
- 支持撤销上一个标注（Ctrl+Z）
- 导出 PNG 图片

**快捷键**
| 快捷键 | 功能 |
|--------|------|
| Ctrl+V | 粘贴剪贴板图片 |
| Ctrl+Z | 撤销上一个标注 |
| Ctrl+S | 导出 PNG |

**注意事项**
- 必须先截图到剪贴板（如 Win+Shift+S），再粘贴到工具中""",

    "css-gradient.html": """### CSS 渐变生成器
可视化 CSS 渐变生成器，拖拽色标调整渐变，一键复制 CSS。

**主要功能**
- 线性渐变和径向渐变一键切换
- 线性：角度 0~360° 滑块调节
- 径向：椭圆/圆形 + 9 种起始位置
- 最多 8 个色标节点，滑块调位置、取色器调色
- 12 组精美预设模板（日落/海洋/极光等）
- 一键复制含浏览器前缀的完整 CSS

**注意事项**
- 渐变代码包含 -webkit- 和 -moz- 前缀，兼容主流浏览器
- 点击预设色块可快速套用模板""",

    "text-counter.html": """### 文本统计工具
实时统计文本的各类指标，支持中英文混合计数。

**主要功能**
- 基础统计：总字符数、含/不含空格、行数、段落数、句子数
- 中英文混合计数：英文按单词计，中文按单字计
- 字符分类：字母/数字/标点/空格分别统计
- 阅读时间估算和朗读时间估算
- 关键词频率 Top 20，带柱状图可视化

**注意事项**
- 阅读时间按中文 300 字/分钟、英文 200 词/分钟估算
- 拖拽 .txt 文件到编辑区可直接导入文本""",

    "hash-tool.html": """### 哈希计算工具
文本与文件哈希计算工具，支持五种主流算法。

**主要功能**
- 文本哈希：输入文本即时计算，支持单选或全部五种算法
- 文件哈希：拖拽或上传任意文件，计算文件哈希值
- 算法支持：MD5 / SHA-1 / SHA-256 / SHA-384 / SHA-512
- 大小写切换、一键复制结果
- MD5 纯 JS 实现，SHA 系列基于 Web Crypto API

**注意事项**
- 文件哈希计算大文件时可能耗时
- SHA-512 安全性最高但哈希值最长""",

    "css-shadow.html": """### CSS 阴影生成器
box-shadow 可视化编辑器，支持多层阴影叠加。

**主要功能**
- 参数调节：X/Y偏移、模糊半径、扩散半径、颜色+不透明度
- 内阴影一键切换
- 最多 8 层阴影叠加，独立调节每层参数
- 9 组预设模板（柔和阴影/深阴影/悬浮卡片/彩色光晕等）
- 一键复制 box-shadow CSS 代码

**注意事项**
- 多层阴影按数组顺序叠加，先写的在最上层
- 不透明度通过颜色的 alpha 通道控制""",

    "uuid-generator.html": """### UUID / 随机字符串生成器
UUID v4 生成器与自定义随机字符串生成器。

**主要功能**
- UUID v4：基于 crypto.getRandomValues 生成标准 UUID
- 批量生成：1~100 个 UUID，列表展示
- 格式选项：去除连字符、大写/小写切换
- 一键复制单个/全部，支持导出 TXT
- 随机字符串：自定义长度（4~256），可选字符集

**注意事项**
- UUID v4 基于随机数，碰撞概率极低
- 随机字符串的字符集至少选择一种""",
}

# 新 CSS 模板（白色极简主题）
NEW_CSS = """/* ============================================================
   白色极简主题 — 纯白底 + 黑字 + 黑边框
   ============================================================ */
:root {
  --bg: #ffffff;
  --panel-bg: #fafafa;
  --text: #111111;
  --text-light: #555555;
  --border: #000000;
  --accent: #000000;
  --accent-hover: #333333;
  --success: #111111;
  --danger: #cc0000;
  --radius: 0px;
  --font-mono: "Cascadia Code","SF Mono","Fira Code","Consolas","Monaco",monospace;
  --font-sans: "Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;
}
* { margin:0; padding:0; box-sizing:border-box; }
body {
  font-family: var(--font-sans); background: var(--bg); color: var(--text);
  height: 100vh; display: flex; flex-direction: column; overflow: hidden;
}

/* 使用说明面板 */
.help-panel {
  border-bottom: 1px solid var(--border); background: #fafafa;
  flex-shrink: 0;
}
.help-toggle {
  padding: 10px 16px; font-size:0.82rem; font-weight:600; cursor:pointer;
  user-select:none; list-style:none; color: var(--text);
  border-bottom: 1px solid var(--border);
}
.help-toggle::-webkit-details-marker { display:none; }
.help-toggle::before { content: '▶ '; font-size:0.7rem; display:inline-block; transition:transform 0.15s; }
details[open] .help-toggle::before { transform: rotate(90deg); }
.help-content {
  padding: 12px 16px; font-size:0.78rem; line-height:1.7; color: var(--text);
  background: #fff; border-bottom: 1px solid var(--border);
}
.help-content h3 { font-size:0.9rem; margin-bottom:6px; font-weight:700; }
.help-content h4 { font-size:0.8rem; margin:8px 0 4px; font-weight:600; }
.help-content ul { padding-left:18px; margin:4px 0; }
.help-content li { margin:2px 0; }
.help-content table { border-collapse:collapse; width:100%; margin:6px 0; font-size:0.75rem; }
.help-content th, .help-content td { border:1px solid var(--border); padding:4px 8px; text-align:left; }
.help-content th { background: #f5f5f5; font-weight:600; }
.help-content code { background:#f0f0f0; padding:1px 4px; font-family:var(--font-mono); font-size:0.72rem; }

/* 标题栏 */
.titlebar {
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 16px; height: 44px; background: #fafafa;
  border-bottom: 1px solid var(--border); flex-shrink: 0;
  user-select: none;
}
.titlebar-title { font-size:0.9rem; font-weight:600; }
.titlebar-actions { display:flex; gap:6px; }

/* 按钮 */
.btn {
  padding: 5px 12px; border: 1px solid var(--border); background: #fff;
  color: var(--text); font-size: 0.82rem; cursor: pointer;
  font-family: inherit; white-space: nowrap; transition: all 0.1s;
}
.btn:hover { background: var(--accent); color:#fff; }
.btn.primary { background:var(--accent); color:#fff; }
.btn.primary:hover { background:var(--accent-hover); }

/* 标签页 */
.tab-row {
  display: flex; gap: 0; padding: 8px 16px 0; flex-shrink: 0;
}
.tab-btn {
  padding: 8px 18px; border: 1px solid var(--border); border-bottom: none;
  background: #fafafa; color: var(--text-light);
  font-size: 0.85rem; cursor: pointer; font-family: inherit;
  margin-right: -1px;
}
.tab-btn:hover { color: var(--text); }
.tab-btn.active { background: #fff; color: var(--text); font-weight:600; border-bottom: 2px solid var(--border); }

.main {
  flex:1; display:flex; overflow:hidden; min-height:0;
}
.tab-content { display:none; flex:1; flex-direction:column; overflow:hidden; gap:14px; }
.tab-content.active { display:flex; }

/* 文本输入框 */
textarea, input[type="text"], input[type="number"], select {
  border: 1px solid var(--border); background: #fff; color: var(--text);
  font-family: inherit; outline: none;
}
textarea:focus, input:focus, select:focus { border-width: 2px; padding: calc(original - 1px); }

/* Toast */
.toast {
  position:fixed; bottom:50px; left:50%; transform:translateX(-50%);
  background:var(--accent); color:#fff; padding:10px 24px;
  font-size:0.85rem; z-index:999;
  opacity:0; transition:opacity 0.2s; pointer-events:none;
  border: 1px solid var(--border);
}
.toast.show { opacity:1; }
.toast.success { background:var(--success); }
.toast.error { background:var(--danger); }"""


def get_help_html(filename):
    """获取指定工具的使用说明 HTML"""
    text = HELP_TEXT.get(filename, "")
    if not text:
        return ""
    return f"""<details class="help-panel" open>
  <summary class="help-toggle">使用说明</summary>
  <div class="help-content">
{text}
  </div>
</details>
"""


def fix_css_in_html(content, filename):
    """
    为 apps 下的工具文件替换 CSS 和添加说明。
    index.html 另行处理。
    """
    # 先添加使用说明（在 body 开始后、titlebar 之前）
    help_html = get_help_html(filename)
    
    if help_html and '<div class="titlebar">' in content:
        content = content.replace(
            '<div class="titlebar">',
            help_html + '\n<div class="titlebar">'
        )
    
    # 替换整个 <style>...</style> 块
    # 匹配 <style> 到第一个 </style>
    style_match = re.search(r'<style>.*?</style>', content, re.DOTALL)
    if style_match:
        # 构建新的 CSS：基础模板 + 保留原文件中特定工具的额外样式
        new_style = '<style>\n' + NEW_CSS
        
        # 处理原 CSS 中工具特有的样式（在 :root 和通用样式之后的部分）
        old_css = style_match.group(0)
        
        # 提取特定工具样式块（保留原文件中有用的特殊样式，但改为白色主题）
        # text-counter 的编辑器面板、统计面板等
        if 'text-counter' in filename:
            new_style += """

/* 文本统计工具专用样式 */
.editor-panel {
  flex:1; display:flex; flex-direction:column; overflow:hidden;
  border-right: 1px solid var(--border);
}
.editor-panel textarea {
  flex:1; padding:14px; border:none; background: #fff; color: var(--text);
  font-family: var(--font-mono); font-size: 0.85rem; line-height: 1.7;
  resize: none; outline: none; tab-size: 2;
}
.editor-panel textarea::placeholder { color: #999; }
.stats-panel {
  width: 320px; display:flex; flex-direction:column; overflow-y:auto;
  background: #fafafa; flex-shrink:0;
}
.stats-section {
  padding: 12px 16px; border-bottom: 1px solid var(--border);
}
.stats-section-title {
  font-size:0.7rem; color:var(--text); text-transform:uppercase;
  letter-spacing:1px; margin-bottom:8px; font-weight:600;
}
.stat-row {
  display:flex; align-items:center; justify-content:space-between;
  padding: 4px 0; font-size:0.82rem;
}
.stat-label { color: var(--text-light); }
.stat-value { font-weight:600; font-family:var(--font-mono); font-size:0.85rem; }
.keyword-row {
  display:flex; align-items:center; gap:8px; padding:3px 0; font-size:0.78rem;
}
.keyword-rank { color:var(--text-light); min-width:20px; text-align:right; }
.keyword-word { flex:1; color:var(--text); }
.keyword-bar-bg { width:80px; height:8px; background:#eee; overflow:hidden; flex-shrink:0; }
.keyword-bar { height:100%; background:var(--accent); transition:width 0.3s; }
.keyword-count { font-family:var(--font-mono); color:var(--text-light); min-width:30px; text-align:right; font-size:0.7rem; }
.empty-hint {
  display:flex; flex-direction:column; align-items:center; justify-content:center;
  height:100%; color:var(--text-light); opacity:0.5; gap:8px;
}"""

        elif 'uuid-generator' in filename:
            new_style += """

/* UUID 工具专用样式 */
.uuid-display {
  background: #fafafa; border: 1px solid var(--border);
  padding: 20px; text-align: center;
}
.uuid-value {
  font-family: var(--font-mono); font-size: 1.4rem; color: var(--text);
  word-break: break-all; margin-bottom: 4px;
}
.uuid-meta { font-size:0.65rem; color:var(--text-light); }
.batch-controls { display:flex; align-items:center; gap:10px; flex-wrap: wrap; padding: 0; }
.batch-controls label { font-size:0.78rem; color:var(--text-light); }
.batch-controls select, .batch-controls input {
  padding:4px 8px; border:1px solid var(--border); background:#fff; color:var(--text); font-family:inherit;
}
.batch-controls select { width:80px; }
.batch-list {
  flex:1; overflow-y:auto; background:#fff; border:1px solid var(--border);
  padding:8px; font-family:var(--font-mono);
  font-size:0.78rem; color:var(--text); line-height:1.8; display:none;
}
.batch-list.show { display:block; }
.string-form { display:flex; flex-wrap:wrap; gap:12px; align-items:flex-end; padding: 0; }
.form-field { display:flex; flex-direction:column; gap:3px; }
.form-field label { font-size:0.7rem; color:var(--text-light); text-transform:uppercase; letter-spacing:0.5px; }
.form-field input { width:80px; padding:5px 8px; border:1px solid var(--border); background:#fff; color:var(--text); font-family:var(--font-mono); font-size:0.82rem; }
.check-group { display:flex; gap:14px; flex-wrap:wrap; margin-top:4px; }
.check-item { font-size:0.78rem; display:flex; align-items:center; gap:4px; cursor:pointer; }
.string-result { background: #fafafa; border: 1px solid var(--border); padding: 16px; margin: 0; }
.string-value { font-family: var(--font-mono); font-size: 1.2rem; color: var(--text); word-break: break-all; margin-bottom: 8px; line-height: 1.6; }
.string-meta { font-size:0.68rem; color:var(--text-light); }"""

        elif 'css-gradient' in filename:
            new_style += """

/* CSS 渐变生成器专用样式 */
.toolbar {
  display: flex; align-items: center; gap: 8px; padding: 8px 16px;
  background: #fafafa; border-bottom: 1px solid var(--border);
  flex-shrink:0; flex-wrap:wrap;
}
.toolbar-hint { font-size:0.72rem; color:var(--text-light); margin-left:auto; }
.main { flex:1; display:grid; grid-template-columns: 320px 1fr; min-height:0; overflow:hidden; }
.sidebar {
  background: #fafafa; border-right: 1px solid var(--border);
  overflow-y: auto; padding: 14px; display:flex; flex-direction:column; gap:14px;
}
.preview-area { display:flex; align-items:center; justify-content:center; background:#fff; min-height:200px; position:relative; overflow:hidden; }
#gradientPreview { width:85%; height:70%; transition: background 0.2s; }
.control-group { display:flex; flex-direction:column; gap:6px; }
.control-label { font-size:0.75rem; color:var(--text-light); text-transform:uppercase; letter-spacing:0.5px; }
.control-row { display:flex; align-items:center; gap:6px; }
.control-row input[type=range] { flex:1; accent-color:var(--accent); }
.control-row input[type=color] { width:32px; height:24px; border:1px solid var(--border); cursor:pointer; padding:0; }
.control-row span { font-size:0.72rem; color:var(--text-light); min-width:32px; text-align:right; font-family:var(--font-mono); }
.gradient-type-row { display:flex; gap:4px; }
.gradient-type-row button { flex:1; }
.stop-item { display:flex; align-items:center; gap:6px; padding:6px 8px; background: #fafafa; border:1px solid var(--border); margin-bottom:4px; }
.stop-item input[type=color] { width:26px; height:22px; border:1px solid var(--border); cursor:pointer; padding:0; }
.stop-item input[type=range] { flex:1; accent-color:var(--accent); }
.stop-item button { background:none; border:none; color:var(--danger); cursor:pointer; font-size:1rem; padding:0 4px; }
.stop-item .stop-pct { font-family:var(--font-mono); font-size:0.7rem; color:var(--text-light); min-width:32px; text-align:right; }
.presets-section { margin-top: 8px; }
.preset-grid { display:grid; grid-template-columns: repeat(4, 1fr); gap:6px; margin-top:6px; }
.preset-item { height:40px; border:2px solid transparent; cursor:pointer; transition: all 0.15s; }
.preset-item:hover { border-color:var(--accent); }
.css-output { padding:12px; background:#fafafa; border-top:1px solid var(--border); display:flex; gap:8px; align-items:flex-start; }
.css-output textarea { flex:1; padding:10px 14px; border:1px solid var(--border); font-family:var(--font-mono); font-size:0.8rem; background:#fff; color:var(--text); resize:none; outline:none; height:72px; line-height:1.5; }"""

        elif 'css-shadow' in filename:
            new_style += """

/* CSS 阴影生成器专用样式 */
.main { flex:1; display:grid; grid-template-columns: 320px 1fr; min-height:0; overflow:hidden; }
.sidebar {
  background: #fafafa; border-right: 1px solid var(--border);
  overflow-y: auto; padding: 14px; display:flex; flex-direction:column; gap:14px;
}
.preview-area { display:flex; align-items:center; justify-content:center; background: #fafafa; }
.preview-box {
  width: 200px; height: 200px; background: #fff;
  border: 2px solid var(--border); transition: box-shadow 0.2s; font-size:0.75rem;
  display:flex; align-items:center; justify-content:center;
  color: var(--text-light); user-select:none;
}
.control-group { display:flex; flex-direction:column; gap:6px; }
.control-label { font-size:0.75rem; color:var(--text-light); text-transform:uppercase; letter-spacing:0.5px; }
.control-row { display:flex; align-items:center; gap:8px; }
.control-row input[type='range'] { flex:1; accent-color:var(--accent); height:4px; }
.control-row input[type='color'] { width:32px; height:24px; border:1px solid var(--border); cursor:pointer; padding:0; }
.control-row span { font-size:0.72rem; color:var(--text-light); min-width:36px; text-align:right; font-family:var(--font-mono); }
.control-row input[type='number'] { width:60px; padding:3px 6px; border:1px solid var(--border); background:#fff; color:var(--text); font-family:var(--font-mono); font-size:0.78rem; text-align:right; }
.layer-header { display:flex; align-items:center; justify-content:space-between; }
.layer-list { display:flex; flex-direction:column; gap:4px; }
.layer-item { display:flex; align-items:center; justify-content:space-between; padding:6px 10px; background: #fff; border:1px solid var(--border); font-size:0.78rem; cursor:pointer; transition: all 0.15s; }
.layer-item:hover { border-width:2px; }
.layer-item.active { border-width:2px; background: #f5f5f5; }
.layer-summary { font-family:var(--font-mono); font-size:0.65rem; color:var(--text-light); flex:1; margin-left:8px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
.layer-del { background:none; border:none; color:var(--text-light); cursor:pointer; font-size:1rem; padding:0 2px; opacity:0.5; }
.layer-del:hover { color: var(--danger); opacity:1; }
.preset-grid { display:grid; grid-template-columns: repeat(3, 1fr); gap:6px; }
.preset-item { height:44px; border:1px solid var(--border); cursor:pointer; transition: all 0.15s; display:flex; align-items:center; justify-content:center; font-size:0.65rem; color:var(--text-light); background:#fff; }
.preset-item:hover { border-width:2px; }
.css-output { padding:12px; background:#fafafa; border-top:1px solid var(--border); display:flex; gap:8px; align-items:flex-start; flex-shrink:0; }
.css-output textarea { flex:1; padding:10px 14px; border:1px solid var(--border); font-family:var(--font-mono); font-size:0.8rem; background:#fff; color:var(--text); resize:none; outline:none; height:68px; line-height:1.5; }"""

        elif 'hash-tool' in filename:
            new_style += """

/* 哈希工具专用样式 */
.tab-content { display:none; flex:1; flex-direction:column; overflow:hidden; }
.tab-content.active { display:flex; }
.text-area { flex:1; display:flex; flex-direction:column; gap:10px; padding:16px; }
#textHashInput { flex:1; padding:12px; border:1px solid var(--border); background: #fff; color: var(--text); font-family: var(--font-mono); font-size: 0.85rem; line-height: 1.6; resize: none; outline: none; }
#textHashInput:focus { border-width:2px; }
#textHashInput::placeholder { color: #999; }
.algo-select-row { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.algo-btn { padding: 6px 14px; border: 1px solid var(--border); background: #fff; color: var(--text-light); font-size: 0.8rem; cursor: pointer; font-family: var(--font-mono); transition: all 0.15s; }
.algo-btn:hover { background:var(--accent); color:#fff; }
.algo-btn.active { background: var(--accent); color: #fff; }
.result-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; flex-shrink: 0; padding: 0 16px 16px; }
.result-card { background: #fafafa; border: 1px solid var(--border); padding: 10px 12px; cursor:pointer; }
.result-card .algo-name { font-size:0.7rem; color:var(--text); text-transform:uppercase; letter-spacing:0.5px; margin-bottom:4px; font-weight:600; }
.result-card .hash-value { font-family: var(--font-mono); font-size:0.75rem; color: var(--text); word-break: break-all; }
.file-area { flex:1; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:16px; padding:16px; }
.dropzone { width: 100%; max-width: 500px; min-height: 180px; border: 2px dashed var(--border); display:flex; flex-direction:column; align-items:center; justify-content:center; cursor:pointer; transition: all 0.2s; background: #fafafa; }
.dropzone:hover { border-color: var(--accent); background: #f5f5f5; }
.dropzone .dz-icon { font-size:2.5rem; margin-bottom:8px; }
.dropzone .dz-text { color:var(--text-light); font-size:0.85rem; }
.file-name { font-family:var(--font-mono); color:var(--text); font-size:0.85rem; margin-top:4px; }
.file-size { color:var(--text-light); font-size:0.7rem; }"""

        new_style += '\n</style>'
        
        content = content[:style_match.start()] + new_style + content[style_match.end():]
    
    return content


# 处理所有 apps 下的 HTML 文件
for filename in os.listdir(APPS_DIR):
    if filename == 'README.md':
        continue
    if not filename.endswith('.html'):
        continue
    
    filepath = os.path.join(APPS_DIR, filename)
    print(f"处理: {filename}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 先移除 EMOJI 标题前缀（但保留titlebar-title内的文本，只去掉emoji本身）
    # 这个由 fix_css_in_html 处理
    
    new_content = fix_css_in_html(content, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  -> 完成")

print("\n所有文件处理完毕!")
