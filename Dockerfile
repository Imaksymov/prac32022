FROM python

COPY . /lab2.py

WORKDIR /lab2.py

CMD ["python3", "lab2"]