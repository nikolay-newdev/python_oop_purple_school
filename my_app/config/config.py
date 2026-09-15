from dataclasses import dataclass
from pathlib import Path


@dataclass
class AppSettings:
    data_directory: Path # отвечает за путь к папке с базой знаний
    app_name: str = "Note Manager"
    app_version: str = "0.1.0"

    @classmethod
    def from_defaults(cls) -> "AppSettings":
        base_path = Path(__file__).parent.parent.parent
        data_path = base_path/'data'
        return cls(data_directory=data_path)

    @classmethod
    def from_custom(cls, data_path: str | Path) -> "AppSettings":
        return cls(data_directory=Path(data_path))

