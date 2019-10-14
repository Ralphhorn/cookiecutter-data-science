{% if cookiecutter.docker_container == 'Pytorch' %}
FROM nvcr.io/nvidia/pytorch:19.09-py3

RUN pip install --upgrade pip
RUN pip install python-dotenv
RUN pip install tb-nightly
RUN pip install future
RUN pip install seaborn
RUN spacy download en
RUN jupyter contrib nbextension install --user
RUN jupyter nbextension enable codefolding/main
RUN jupyter nbextension enable execute_time/ExecuteTime
RUN jupyter nbextension enable hinterland/hinterland
RUN jupyter nbextension enable livemdpreview/livemdpreview
RUN pip install yapf
RUN jupyter nbextension enable code_prettify/code_prettify
RUN jupyter nbextension enable toggle_all_line_numbers/main

{% elif cookiecutter.docker_container == 'Tensorflow' %}
FROM nvcr.io/nvidia/tensorflow:19.09-py3
RUN pip install --upgrade pip
RUN pip install python-dotenv
RUN jupyter contrib nbextension install --user
RUN jupyter nbextension enable codefolding/main
RUN jupyter nbextension enable execute_time/ExecuteTime
RUN jupyter nbextension enable hinterland/hinterland
RUN jupyter nbextension enable livemdpreview/livemdpreview
RUN pip install yapf
RUN jupyter nbextension enable code_prettify/code_prettify
RUN jupyter nbextension enable toggle_all_line_numbers/main
{% elif cookiecutter.docker_container == 'Kaggle' %}
FROM kaggle/python
RUN pip install --upgrade pip
RUN pip install python-dotenv
RUN pip install jupyter_contrib_nbextensions
RUN jupyter contrib nbextension install --user
RUN jupyter nbextension enable codefolding/main
RUN jupyter nbextension enable execute_time/ExecuteTime
RUN jupyter nbextension enable hinterland/hinterland
RUN jupyter nbextension enable livemdpreview/livemdpreview
RUN pip install yapf
RUN jupyter nbextension enable code_prettify/code_prettify
RUN jupyter nbextension enable toggle_all_line_numbers/main
{% endif %}