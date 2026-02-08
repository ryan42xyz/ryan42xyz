# 从 resume.tex 生成并验收 PDF

## 1. 一次性安装 TeX（未装过才需要）

在终端执行（会提示输入本机密码）：

```bash
brew install --cask basictex
```

安装完成后**无需重启终端**，本脚本会自动找 `/Library/TeX/texbin` 里的 xelatex。

## 1b. 安装 resume.tex 依赖的宏包（若报 `titlesec.sty not found`）

BasicTeX 不含全部宏包，需用 tlmgr 安装（会提示输入本机密码）。

若 tlmgr 提示 “tlmgr itself needs to be updated”，先更新再装包：

```bash
# 1) 更新 tlmgr（路径按你的 TeX Live 版本调整，如 2025basic）
sudo /usr/local/texlive/2025basic/bin/universal-darwin/tlmgr update --self

# 2) 安装宏包
sudo /usr/local/texlive/2025basic/bin/universal-darwin/tlmgr install titlesec enumitem hyperref setspace fontspec
```

若 TeX Live 版本不是 2025，可先运行 `ls /usr/local/texlive/*/bin/*/tlmgr` 确认 tlmgr 路径，再把上面命令里的路径换成你的。

## 2. 生成并验收 PDF

```bash
cd /path/to/github-init/github-profile
python3 tex2pdf.py
```

成功时会输出：`Done: .../resume.pdf (xx.x KB)` 和 `PDF header OK, ready to use.`  
脚本会检查生成的 `resume.pdf` 是否存在且为合法 PDF。
