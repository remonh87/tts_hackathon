FROM nvidia/cuda:12.2.0-base-ubuntu20.04
RUN apt-get update && apt-get -y install software-properties-common
RUN apt install -y git && apt install -y curl
RUN add-apt-repository 'ppa:deadsnakes/ppa' && apt-get update
RUN  apt-get install -y python3.10
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1 &&  update-alternatives --config python3
RUN apt -y remove --purge python3-apt && apt autoclean
RUN apt install -y python3-apt && apt install -y python3.10-distutils && apt install -y python3.10-venv && apt install -y python3.10-dev
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3.10 get-pip.py
RUN apt install -y python3-pip && pip install --upgrade pip 
RUN mkdir input
RUN git clone https://github.com/remonh87/tts_hackathon.git
RUN cd tts_hackathon && pip install -r ./requirements.txt
RUN pip install git+https://github.com/serp-ai/bark-with-voice-clone.git && pip install tensorboardX 
