{% if cookiecutter.docker_container == 'Pytorch' %}
FROM nvcr.io/nvidia/pytorch:19.09-py3

RUN pip install --upgrade pip
RUN pip install python-dotenv
RUN pip install tb-nightly
RUN pip install future
RUN pip install seaborn
RUN spacy download en

{% elif cookiecutter.docker_container == 'Tensorflow' %}
FROM nvcr.io/nvidia/tensorflow:19.09-py3
RUN pip install --upgrade pip
RUN pip install python-dotenv
{% elif cookiecutter.docker_container == 'Kaggle' %}
FROM kaggle/python
RUN pip install --upgrade pip
RUN pip install python-dotenv
{% endif %}