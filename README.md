
# new README 
$content = @"
---
title: Igala-English NMT Translator
emoji: 🌍
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.32.0
app_file: streamlit_app.py
pinned: false
---

# Igala-English Neural Machine Translation

Demo app for low-resource language translation.
"@

[System.IO.File]::WriteAllText("README.md", $content, [System.Text.UTF8Encoding]::new($false))


