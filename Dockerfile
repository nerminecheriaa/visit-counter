
# Alpine : base minimale (~50 Mo) -> image légère, surface d'attaque réduite
FROM python:3.12-alpine

WORKDIR /app

# Utilisateur non-root
RUN adduser -D appuser

# Dépendances copiées d'abord : le cache Docker est réutilisé
# tant que requirements.txt ne change pas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

USER appuser
EXPOSE 5000

# CMD : commande exécutée au démarrage du conteneur
CMD ["python", "app.py"]