FROM python:3.9
WORKDIR /scr/app
COPY ./scr/ .
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./plot.py" ]