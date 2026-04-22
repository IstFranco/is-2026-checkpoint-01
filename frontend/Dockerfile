FROM python:3.12-slim

WORKDIR /app

COPY html/ /app/

RUN useradd -m appuser
USER appuser

EXPOSE 8080

HEALTHCHECK CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:8080')"

CMD ["python3", "-m", "http.server", "8080"]
