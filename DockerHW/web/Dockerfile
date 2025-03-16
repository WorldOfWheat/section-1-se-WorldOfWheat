FROM python:3.11-slim

RUN mkdir /work
WORKDIR /work
ADD requirements.txt ./
ADD main.py ./
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
