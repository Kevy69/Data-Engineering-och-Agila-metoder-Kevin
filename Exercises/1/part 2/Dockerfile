FROM python:3.9

RUN apt update && apt install cron nano -y

# Using pip because thats the python package manager. apt can be used ofc.
RUN pip install matplotlib pandas numpy tabulate


WORKDIR /Exercise1-part2

COPY . .

