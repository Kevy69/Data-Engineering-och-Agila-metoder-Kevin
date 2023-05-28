FROM python:3.9

# Using pip because thats the python package manager. apt can be used ofc.
RUN pip install matplotlib plotly pandas numpy dash scikit-learn

WORKDIR /Exercise1

COPY . .

CMD [ "python", "./src/ex1_0_setup.py"]