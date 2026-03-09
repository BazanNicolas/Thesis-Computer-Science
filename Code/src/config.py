from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Paths:
    excel_path: Path
    fc_folder: Path
    t1w_csv_path: Path
    out_dir: Path


@dataclass(frozen=True)
class ExperimentConfig:
    seed: int = 42
    diagnoses_to_use: tuple[str, ...] = ("CN", "AD", "FTD")
    test_size: float = 0.10
    k_folds: int = 5
    fisher_z: bool = True
    use_optuna: bool = True
    optuna_xgb_trials: int = 100
    optuna_vae_trials: int = 60
    reuse_artifacts: bool = True
