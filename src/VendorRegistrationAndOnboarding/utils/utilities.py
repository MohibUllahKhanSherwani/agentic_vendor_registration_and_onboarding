from pathlib import Path
import yaml
import os
from dotenv import load_dotenv
from passlib.context import CryptContext
from logging.handlers import RotatingFileHandler
import logging


pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def load_yaml(path: str | Path) -> dict:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"YAML file not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if data is None:
        raise ValueError(f"YAML file is empty: {path}")
    return data

def load_env():
    root_dir = Path(__file__).resolve().parents[3]  # go to project root
    print(root_dir)
    env_path = os.path.join(root_dir,".env")

    load_dotenv(dotenv_path=env_path)

def setup_logger(
    name: str = "agent_logger",
    log_file: str = os.path.join(os.getcwd(), "app.log"),
    level: int = logging.INFO,
):
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024, 
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    if not root_logger.handlers:
        root_logger.addHandler(file_handler)
        root_logger.addHandler(console_handler)

    return root_logger
logger = setup_logger()

async def ensure_session(user_id: str, session_id: str,session_service,app_name):
    session = await session_service.get_session(app_name=app_name, user_id=user_id, session_id=session_id)
    if session is None:
        logger.info(f"Creating New Session")
        session = await session_service.create_session(
        session_id=session_id,
        user_id=user_id,
        app_name=app_name
    )
    else:
        logger.info(f"Session Already Exists")
    return session