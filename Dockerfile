FROM python:3
MAINTAINER Pedro Christo
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python","./HL72JsonAPI.py"]
EXPOSE 5000