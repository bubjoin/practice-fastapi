FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# pip flags: no save packages, keep it latest version, install from requirements file
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

ENTRYPOINT ["uvicorn"]

# --proxy-headers
# with Nginx etc TLS Termination Proxy(load balancer), app is running behind HTTPS, etc
CMD ["app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]

