FROM python:3.12
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "healthcaret.wsgi:application"]
