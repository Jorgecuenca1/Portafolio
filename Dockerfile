FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app/portafolio
RUN apt update -y && apt install -y wkhtmltopdf
COPY requirements.txt /app/portafolio/
RUN pip install -r requirements.txt
COPY . /app/portafolio/
CMD sh app-entrypoint.sh