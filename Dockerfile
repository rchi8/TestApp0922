# 基本イメージとしてPython 3.8を使用
FROM python:3.10-slim-buster

# 作業ディレクトリを設定
WORKDIR /app

# requirements.txtを/appディレクトリにコピー
COPY requirements.txt /app/

# 必要なPythonライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# appディレクトリとmodelディレクトリをコピー
COPY app/ /app/app/
COPY model/ /app/model/

# 環境変数の設定（オプション）
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# app.pyを実行するコマンド
CMD ["flask", "run"]
