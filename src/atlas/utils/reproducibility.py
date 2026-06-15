"""Gestion de la reproductibilité et du tracking des expériences."""

import json
import random
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np


def get_git_hash() -> str:
    """Retourne le hash court du commit courant."""
    try:
        return (
            subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
            .decode()
            .strip()
        )
    except Exception:
        return "unknown"


def save_run(
    config: dict, metrics: dict, artifacts: dict[str, Any] | None = None
) -> Path:
    """Enregistre un run d'expérience avec tous les paramètres."""
    git_hash = get_git_hash()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = Path("runs") / f"{git_hash}_{timestamp}"
    run_dir.mkdir(parents=True, exist_ok=True)

    run_record = {
        "git_hash": git_hash,
        "timestamp": timestamp,
        "config": config,
        "metrics": metrics,
        "artifacts": artifacts or {},
    }

    with open(run_dir / "run.json", "w") as f:
        json.dump(run_record, f, indent=2, default=str)

    return run_dir


def set_all_seeds(seed: int = 42) -> None:
    """Fixe toutes les seeds pour reproductibilité totale."""

    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch

        torch.manual_seed(seed)
    except ImportError:
        pass
