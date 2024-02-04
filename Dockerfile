FROM runpod/base:0.4.0-cuda11.8.0

WORKDIR /

RUN pip install tensorflow
RUN pip install transformers
RUN pip install runpod

ADD src .

CMD python3.11 -u /handler.py
