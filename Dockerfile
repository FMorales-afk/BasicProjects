FROM python:3.10

WORKDIR /calculator

COPY . . 

CMD ["python","./calc_menu.py"]