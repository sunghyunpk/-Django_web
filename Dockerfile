FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/sunghyunpk/-Django_web.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY= seoks)_)d2qx-hleev)@l7l$u#p8x-(a^yq3ite6+=0lt@49=l" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# CMD ["gunicorn", "pragmatic.wsgi", "--bind", "0.0.0.0:8000"]