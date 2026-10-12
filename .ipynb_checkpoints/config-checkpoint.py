"""
Konfigurasi Global Lingkungan dan Agen.
Mendukung switching dinamis antara Simulator Deterministik dan Provider LLM Eksternal.
"""
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class AppConfig:
    MAX_AGENT_ITERATIONS: int = 5
    SIMULATE_ENVIRONMENT: bool = True
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    DEFAULT_MODEL: str = "gpt-4o-mini"
    LOG_LEVEL: str = "INFO"

CONFIG = AppConfig()