FROM python:3.7

ADD exoApp.py /

ADD requirements.txt /

RUN pip install -r ./requirements.txt

EXPOSE 5000

CMD [ "python", "./exoApp.py" ]
