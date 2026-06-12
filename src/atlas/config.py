"""Configuration centrale — charge params.yaml et variables d'environnement."""

from pathlib import Path
import yaml

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

PROJECT_ROOT = Path(__file__).parent.parent.parent
PARAMS_FILE = PROJECT_ROOT / "params.yaml"
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
FIGURES_OUTPUT = PROJECT_ROOT / "figures" / "output"
RUNS_DIR = PROJECT_ROOT / "runs"


def load_params() -> dict:
    """Charge params.yaml."""
    with open(PARAMS_FILE) as f:
        return yaml.safe_load(f)


PARAMS = load_params()
RANDOM_SEED = PARAMS["reproducibility"]["random_seed"]
