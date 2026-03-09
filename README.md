# Tesis: Estimación de edad cerebral con datos multimodales (FC + T1w)

Pipeline: β-VAE comprime matrices de conectividad funcional (6670 → 64 dim), se concatenan con features T1w (116), XGBoost predice edad. Evaluado en cohorte RedLaT (N = 1245).

## Estructura del repositorio

- **`Code/`** — Código de experimentos, entrenamiento (VAE, XGBoost) y generación de figuras. Notebooks en `notebooks/` (p. ej. `main.ipynb`, `experiments.ipynb`), scripts en `scripts/`, módulos en `src/`.
- **`Latex/`** — Tesis (libro) y presentación Beamer. Documento principal en `Latex/tesis/tesis.tex` → `tesis.pdf`; diapositivas en `Latex/presentacion/presentacion.tex` → `presentacion.pdf`. Detalles y compilación en **`Latex/README.md`**.
- **`Animations/`** — Animaciones Manim del pipeline (FC → β-VAE → fusión multimodal → XGBoost). Escenas en `scene_01_fc.py` … `scene_04_xgboost.py`; para renderizar todo y generar el video combinado: `bash Animations/render_all.sh`. Salidas en `Animations/media/` (no versionadas).

Data, outputs y artefactos generados están en `.gitignore`.

## Notas para uso del repositorio

- **Datos:** Los datos de la cohorte RedLaT pueden no estar disponibles públicamente. El código se incluye como evidencia y referencia metodológica; sin los datos, no será posible reproducir los resultados completos.
- **Outputs de notebooks:** Las salidas de las celdas se conservan a propósito para poder cotejar figuras y tablas con lo mostrado en la tesis.
- **Animaciones:** Las escenas en `Animations/` que usan imágenes de `Outputs/` (p. ej. reconstrucciones del VAE) requieren haber generado antes esas figuras ejecutando el pipeline; sin datos, solo parte de las escenas será reproducible.
