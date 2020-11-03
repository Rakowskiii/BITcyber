FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip 


WORKDIR /project
ADD . /project
RUN pip3 install -r requirements.txt
CMD ["python3","blog.py"]