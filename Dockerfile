FROM python:slim as dependency
WORKDIR /reqs
COPY requirements.txt /reqs
RUN pip install --no-cache-dir -r requirements.txt

FROM python:slim
WORKDIR /home/app
COPY . .
COPY --from=dependency /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
CMD ["python","./HL72JsonAPI.py"]
EXPOSE 5000