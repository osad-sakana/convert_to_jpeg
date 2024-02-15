import os
from PIL import Image, UnidentifiedImageError
from shutil import move

input_dir = './input'
output_dir = './output'
processed_dir = './processed'

# ディレクトリが存在しない場合は作成
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
if not os.path.exists(processed_dir):
    os.makedirs(processed_dir)

# inputディレクトリ内のファイルをリストアップ
for filename in os.listdir(input_dir):
    input_path = os.path.join(input_dir, filename)

    try:
        # 画像を開いてJPEGに変換
        with Image.open(input_path) as img:
            img = img.convert('RGB')  # JPEGへの変換にはRGB形式が必要
            
            # JPEGに変換して保存するファイルのパスを設定
            output_filename = filename.rsplit('.', 1)[0] + '.jpg'
            output_path = os.path.join(output_dir, output_filename)
            
            img.save(output_path)
            
            # 変換後のファイルをprocessedディレクトリに移動
            processed_path = os.path.join(processed_dir, filename)
            move(input_path, processed_path)
    
    except UnidentifiedImageError:
        # 画像ファイルでない場合はスキップし、入力ディレクトリにそのまま残す
        print(f"Skipping non-image file: {filename}")
        continue
