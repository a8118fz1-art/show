#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import os
import sys

os.chdir('f:\\OllamaModels\\SHOW揚網站')
os.makedirs('images', exist_ok=True)

# 缺失的車型 - 使用替代 URL 來源
missing_vehicles = {
    'YAMAHA_XJ6.jpg': 'https://upload.wikimedia.org/wikipedia/commons/3/3a/Yamaha_XJ6_in_Barcelona%2C_Spain.jpg',
    'YAMAHA_FZ6.jpg': 'https://upload.wikimedia.org/wikipedia/commons/7/78/Yamaha_FZ6N_-_2006.jpg',
    'HONDA_CB650.jpg': 'https://upload.wikimedia.org/wikipedia/commons/8/8a/Honda_CB650_-_2013.jpg',
    'SUZUKI_SFV650.jpg': 'https://upload.wikimedia.org/wikipedia/commons/6/63/Suzuki_SFV_650_-_2009_JD.jpg',
    'SUZUKI_SV650.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Suzuki_SV650_2015.jpg/1200px-Suzuki_SV650_2015.jpg'
}

print('開始下載缺失的摩托車圖片...\n')
success_count = 0
fail_count = 0

for filename, url in missing_vehicles.items():
    filepath = os.path.join('images', filename)
    
    # 檢查是否已存在
    if os.path.exists(filepath):
        print(f'✓ {filename} 已存在，跳過')
        continue
        
    try:
        print(f'正在下載: {filename}')
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        with urllib.request.urlopen(req, timeout=15) as response:
            with open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        
        file_size = os.path.getsize(filepath) / 1024
        print(f'✓ {filename} 下載完成 ({file_size:.1f} KB)\n')
        success_count += 1
        
    except Exception as e:
        print(f'✗ {filename} 下載失敗: {str(e)}\n')
        fail_count += 1
        # 如果檔案在下載過程中出錯，刪除它
        if os.path.exists(filepath):
            os.remove(filepath)

print(f'\n{'='*50}')
print(f'下載結果: 成功 {success_count} 個, 失敗 {fail_count} 個')
print(f'{'='*50}')

# 列出所有已下載的圖片
print(f'\n已下載的車型圖片:')
for filename in ['YAMAHA_MT07.jpg', 'YAMAHA_XJ6.jpg', 'YAMAHA_FZ6.jpg', 
                  'HONDA_CB650.jpg', 'HONDA_NC750.jpg', 
                  'SUZUKI_SFV650.jpg', 'SUZUKI_SV650.jpg']:
    filepath = os.path.join('images', filename)
    if os.path.exists(filepath):
        size = os.path.getsize(filepath) / 1024
        print(f'  ✓ {filename} ({size:.1f} KB)')
    else:
        print(f'  ✗ {filename} (缺失)')
