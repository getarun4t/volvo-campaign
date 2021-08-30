FROM python:latest

RUN apt-get update -yqq && apt-get install apt-transport-https zip -yqq &&  apt-get upgrade -yqq
WORKDIR /Test_Automation_Framework
COPY requirements.txt /Test_Automation_Framework/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . /Test_Automation_Framework
CMD pytest