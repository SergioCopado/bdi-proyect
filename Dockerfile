FROM python:3.8

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY data_extractor.py .

RUN mkdir /json

CMD ["python", "-u", "data_extractor.py"]