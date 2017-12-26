FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN python db_create.py

EXPOSE 5000

CMD [ "python", "run.py" ]