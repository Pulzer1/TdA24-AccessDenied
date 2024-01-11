# syntax=docker/dockerfile:1

FROM python:3.10-buster

# TAILWIND CLI standalone + making it executable
COPY ./app/tailwindcss-linux-x64 /usr/local/bin/tailwindcss
RUN chmod +x /usr/local/bin/tailwindcss


WORKDIR /app

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

COPY . .

RUN tailwindcss -i ./app/static/styles.css -o ./app/static/output.css

RUN pipenv install --system --deploy

EXPOSE 80

CMD ["./start.sh"]

