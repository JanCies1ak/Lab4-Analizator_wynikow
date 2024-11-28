 # Wybór obrazu bazowego
FROM python:3.10-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Kopiowanie plików do kontenera
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY model.pkl model.pkl

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# Otwarcie portu
EXPOSE 5000

# Uruchomienie aplikacji
CMD ["python", "app.py"]
