# LaTeX — Tesis y presentación

Estructura:

- **`tesis/`** — Documento principal (libro). Fuente: `tesis.tex`. Salida: **`tesis.pdf`**.
- **`presentacion/`** — Diapositivas Beamer. Fuente: `presentacion.tex`. Salida: **`presentacion.pdf`**.
- Carpetas `00_tapa/`, `01_agradecimientos/`, …, `07_conclu/`, `conf.tex`, `acronimos.tex`, `tesis.bib` — compartidas por la tesis (y por la presentación para figuras).

## Compilación

**Tesis** (genera `tesis/tesis.pdf`):
```bash
cd Latex/tesis
pdflatex -shell-escape tesis.tex
bibtex tesis
pdflatex -shell-escape tesis.tex
pdflatex -shell-escape tesis.tex
```

**Presentación** (genera `presentacion/presentacion.pdf`):
```bash
cd Latex/presentacion
pdflatex presentacion.tex
pdflatex presentacion.tex
```

Los artefactos (`.aux`, `.log`, `.pdf`, etc.) se generan en la misma carpeta del `.tex` y están en `.gitignore`; solo se versionan las fuentes y recursos (figuras, etc.).
