FROM python:3.9
WORKDIR /metro
COPY requirements.txt /metro
RUN pip3 install --upgrade pip -r requirements.txt
COPY . /metro
EXPOSE 5000