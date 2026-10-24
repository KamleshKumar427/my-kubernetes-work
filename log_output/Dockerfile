FROM python:3.12-slim

WORKDIR /app
COPY app.py .

# -u: unbuffered output, so logs show up in `kubectl logs` right away
CMD ["python", "-u", "app.py"]
