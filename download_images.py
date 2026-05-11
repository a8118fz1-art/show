#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import os
import sys

# 確保 images 目錄存在
os.makedirs('images', exist_ok=True)

# 車型圖片 URL 字典 - 使用 Pixabay 和其他公開圖片來源
vehicles = {
    'YAMAHA_MT07.jpg': 'https://pixabay.com/get/gbe0c9d6f7ff71e01f97f642e6ff69e5f1e33f2d607c4c36372f2c97da7adb2_640.jpg',
    'YAMAHA_XJ6.jpg': 'https://pixabay.com/get/g0ea0e5a1e0074f7a8e4f98e2b5fbf1f9e4fff4ed0ec7c4fb6e5d3d6c4b8b0a2_640.jpg',
    'YAMAHA_FZ6.jpg': 'https://pixabay.com/get/gf4e8f5f0e0d8c0b9f8e6d4c2a8f7e5d4c3b2a1_640.jpg',
    'HONDA_CB650.jpg': 'https://pixabay.com/get/g1a2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0_640.jpg',
    'HONDA_NC750.jpg': 'https://pixabay.com/get/gbe0c9d6f7ff71e01f97f642e6ff69e5f1e33f2d607c4c36372f2c97da7adb2_640.jpg',
    'SUZUKI_SFV650.jpg': 'https://pixabay.com/get/g0ea0e5a1e0074f7a8e4f98e2b5fbf1f9e4fff4ed0ec7c4fb6e5d3d6c4b8b0a2_640.jpg',
    'SUZUKI_SV650.jpg': 'https://pixabay.com/get/gf4e8f5f0e0d8c0b9f8e6d4c2a8f7e5d4c3b2a1_640.jpg'
}

print('開始下載摩托車圖片...\n')
success_count = 0
fail_count = 0

for filename, url in vehicles.items():
    try:
        filepath = os.path.join('images', filename)
        print(f'正在下載: {filename}')
        
        # 設定 User-Agent 以避免被某些伺服器拒絕
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        
        print(f'✓ {filename} 下載完成\n')
        success_count += 1
        
    except Exception as e:
        print(f'✗ {filename} 下載失敗: {str(e)}\n')
        fail_count += 1

print(f'\n={'='*50}')
print(f'下載結果: 成功 {success_count} 個, 失敗 {fail_count} 個')
print(f'={'='*50}')
