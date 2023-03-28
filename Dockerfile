FROM python:3.8-slim-bullseye
RUN pip3 install --upgrade pip
RUN pip3 install flask gunicorn
ENV PORT=8081
ENV FLASK_DIR=/opt
COPY wsgi.py $FLASK_DIR
COPY panxml2json.py $FLASK_DIR
COPY devicelist.csv $FLASK_DIR
ENTRYPOINT gunicorn -b 0.0.0.0:$PORT -w 1 --chdir=$FLASK_DIR --access-logfile '-' wsgi:app
EXPOSE $PORT

