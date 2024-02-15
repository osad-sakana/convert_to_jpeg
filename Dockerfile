# Pythonイメージをベースにする
FROM python:3.8

# 作業ディレクトリを設定
WORKDIR /app

# 現在のディレクトリの内容をコンテナ内の/appにコピー
COPY . /app

# 依存関係のインストール
RUN pip install --no-cache-dir -r requirements.txt

# コンテナが実行された時にスクリプトを実行
CMD ["python", "./main.py"]
