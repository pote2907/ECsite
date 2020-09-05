# ベースをpython3.7
FROM python:3.7-alpine

# __pycache__フォルダが作られないようにする
ENV PYTHONDONTWRITEBYTECODE 1
# バッファされないようにする
ENV PYTHONUNBUFFERED 1

# requirementsファイルをDockerコンテナにコピー
COPY ./requirements.txt /requirements.txt

# postgresqlの依存モジュール群をインストール
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# アプリケーションコード保存先を作成
RUN mkdir /ECsite
# ワークディレクトリをappに指定
WORKDIR /ECsite
# ローカルのソースコードをappにコピー
COPY . /ECsite

# staticファイルの保存先を作成
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

CMD gunicorn ECsite.wsgi:application --bind 0.0.0.0:$PORT
