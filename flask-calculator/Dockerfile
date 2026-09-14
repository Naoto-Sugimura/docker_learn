# 軽量なPython環境を指定
FROM python:3.11-slim

# コンテナ内の作業フォルダを設定
WORKDIR /app

# 依存ライブラリのインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリのファイルをすべてコピー
COPY . .

# 5000番ポートを開放
EXPOSE 5000

# Flaskアプリの起動
CMD ["python", "app.py"]