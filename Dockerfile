FROM python:3.7.9

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt update && apt install -y libsm6 libxext6
RUN apt-get install -y libxrender-dev

RUN mkdir ./commands
RUN mkdir ./models

COPY commands/ ./commands
COPY models/ ./models

COPY bot.py .
COPY os_helper.py .

CMD ["python3", "bot.py"]