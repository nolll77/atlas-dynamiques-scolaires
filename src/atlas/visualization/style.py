"""Thème graphique global — Atlas des Dynamiques Scolaires."""

import matplotlib.pyplot as plt
from pathlib import Path

COLORS = {
    "public": "#1565C0",
    "prive": "#C62828",
    "international": "#2E7D32",
    "cluster_1": "#F44336",
    "cluster_2": "#FF9800",
    "cluster_3": "#2196F3",
    "cluster_4": "#4CAF50",
    "cluster_5": "#9C27B0",
    "background": "#FAFAFA",
    "grid": "#E0E0E0",
}

ETHICAL_NOTE = (
    "Note : Ces données mesurent des associations statistiques. "
    "Elles n'impliquent aucun jugement sur les établissements."
)


def set_atlas_style() -> None:
    """Applique le thème graphique global."""
    plt.rcParams.update({
        "figure.facecolor": COLORS["background"],
        "axes.facecolor": COLORS["background"],
        "axes.grid": True,
        "grid.color": COLORS["grid"],
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "axes.titlesize": 14,
        "figure.dpi": 150,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
    })


def add_ethical_note(ax, text: str = None) -> None:
    """Ajoute la note éthique standardisée à une figure."""
    ax.text(0.01, -0.10, text or ETHICAL_NOTE,
            transform=ax.transAxes, fontsize=8,
            color="gray", fontstyle="italic")


def save_figure(fig, name: str, formats: tuple = ("png", "pdf")) -> None:
    """Sauvegarde en multiple formats dans figures/output/."""
    output_dir = Path("figures/output")
    output_dir.mkdir(exist_ok=True)
    for fmt in formats:
        path = output_dir / f"{name}.{fmt}"
        fig.savefig(path, format=fmt)
        print(f"  💾 {path}")
