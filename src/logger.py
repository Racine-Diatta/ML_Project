import os
import logging
from datetime import datetime

# Nom du fichier journal basé sur la date et l'heure actuelles
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Chemin du répertoire "logs"
logs_path = os.path.join(os.getcwd(), "logs")

# Création du répertoire "logs" s'il n'existe pas déjà
os.makedirs(logs_path, exist_ok=True)

# Chemin complet du fichier journal
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configuration du module de journalisation
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

