FROM python:3

ADD exoApp.py /

ADD requirements.txt /

RUN pip install -r ./requirements.txt

CMD [ "python", "./exoApp.py" ]
