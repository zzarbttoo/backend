FROM python:3.9

WORKDIR /pulse_realtime

COPY ./requirements.txt /pulse_realtime/requirements.txt

ARG PORT
ARG PROFILE

ENV PORT_INT=${PORT}
ENV PYTHON_PROFILES_ACTIVE=${PROFILE}

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /template/requirements.txt

COPY . /template

EXPOSE 0
EXPOSE 5672

COPY entrypoint.sh /pulse_realtime/entrypoint.sh
RUN chmod +x /pulse_realtime/entrypoint.sh

ENTRYPOINT ["/pulse_realtime/entrypoint.sh"]
