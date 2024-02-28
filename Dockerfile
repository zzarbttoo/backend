# FROM krmp-d2hub-idock.9rum.cc/goorm/python:3.9
FROM python:3.9

WORKDIR /

COPY ./requirements.txt /backend/requirements.txt

ARG PORT
ARG PROFILE

ENV PORT_INT=${PORT}
ENV PYTHON_PROFILES_ACTIVE=${PROFILE}

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

COPY . /backend


EXPOSE 5672

ENTRYPOINT ["python3", "-m", "uvicorn", "app.main:app"]
CMD ["--host", "0.0.0.0", "--port", "5672" , "--env-file", "app/config/local.env"]

