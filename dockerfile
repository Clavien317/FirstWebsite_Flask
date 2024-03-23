FROM python:3



WORKDIR "/run/media/clavien/Personnel/TP/Flask"
WORKDIR /app
COPY requirements.txt .
COPY index.py ./
RUN pip install -r requirements.txt



EXPOSE 6000


CMD ["python", "-m", "flask", "run"]