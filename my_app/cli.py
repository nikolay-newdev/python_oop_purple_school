from pathlib import Path
import sys

from my_app.config.config import AppSettings


def create_app(data_path: Path | None=None):
    settings: AppSettings
    if data_path:
        settings = AppSettings.from_custom(data_path)
    else:
        settings = AppSettings.from_defaults()
    # Старт приложения


def run():
    data_path = None
    if len(sys.argv[1]):
        data_path = Path(sys.argv[1])
    create_app(data_path)
        
    print("Запуск")