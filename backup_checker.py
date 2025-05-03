import os
import datetime
import argparse
from pathlib import Path

def check_backups(backup_dir, days_threshold=7):
    backup_path = Path(backup_dir)
    if not backup_path.exists():
        print(f"Erreur : Le dossier {backup_dir} n'existe pas.")
        return

    today = datetime.datetime.now()
    threshold = today - datetime.timedelta(days=days_threshold)
    recent_backups = [f for f in backup_path.iterdir() if f.is_file() and f.stat().st_mtime > threshold.timestamp()]
    
    if recent_backups:
        print(f"{len(recent_backups)} sauvegarde(s) récente(s) trouvée(s) dans {backup_dir}.")
    else:
        print(f"Aucune sauvegarde récente (moins de {days_threshold} jours) dans {backup_dir}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vérifie les sauvegardes récentes.")
    parser.add_argument("backup_dir", help="Dossier des sauvegardes")
    parser.add_argument("--days", type=int, default=7, help="Seuil en jours")
    args = parser.parse_args()
    check_backups(args.backup_dir, args.days)