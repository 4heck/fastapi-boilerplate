from pathlib import Path

from starlette.config import Config

env_file: Path = Path(__file__).parent.parent.parent.parent / ".env"
config: Config = Config(env_file if env_file.exists() else None)
