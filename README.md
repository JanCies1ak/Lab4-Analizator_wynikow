# Lab4-Analizator_wynikow

---
# Instrukcja uruchamiania 

## Pobierz repozytorium

```bash
git clone https://github.com/PJATK-ASI-2024/Lab4-Analizator_wynikow.git
cd Lab4-Analizator_wynikow
```

## Jak uruchomić lokalnie

Aktywuj wirtualne środowisko i pobierz zależności
```bash
python -m venv ./venv
source venv/bin/activate # Na Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Uruchom aplikację
```bash
python s24110.py
```

Aplikacja powinna działać lokalnie pod adresem http://localhost:5000

## Jak uruchomić z Dockera
Zbuduj obraz z użyciem pliku Dockerfile
```bash
docker build -t jancies1ak/lab4-analizator:v1 .
```

Uruchom kontener z utworzonego obrazu:
```bash
docker run -p 5000:5000 jancies1ak/lab4-analizator:v1
````

Aplikacja powinna być dostępna pod adresem http://localhost:5000

## Jak uruchomić z obrazu z Docker Huba

Aby pobrać obraz z Docker Huba, użyj poniższego polecenia:
```bash
docker pull jancies1ak/lab4-analizator:v1
```

Uruchom pobrany obraz:
```bash
docker run -p 5000:5000 jancies1ak/lab4-analizator:v1
```
Aplikacja będzie dostępna pod http://localhost:5000
