FROM python:3

WORKDIR /app
# app est un dossier dans le conteneur

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./src/main.py", "[100]", "[20]"]