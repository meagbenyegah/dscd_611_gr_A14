# Uber Request EDA (DSCD_611 — Group A14)

Lightweight reproducible project for the Uber Request EDA assignment. This repository contains the dataset, an exploratory notebook, a runnable script that produces the required answers and visualisations, and pinned dependencies for reproducibility.

Repository layout

- `data/` — source data: `Uber Request Data.csv`
- `notebooks/` — `uber_request_project.ipynb` (exploratory analysis with Markdown explanations)
- `src/` — `uber_request_eda.py` (runnable script that saves plots)
- `outputs/` — example generated PNG plots (not required to submit)
- `requirements_frozen.txt` — pinned, exact package versions for reproducible installs
- `submission_checklist.md` — quick verification checklist

Quickstart (from project root)

```bash
cd dscd_611_gr_A14
python3 -m venv venv                # optional but recommended
source venv/bin/activate
python3 -m pip install -r requirements_frozen.txt

# Run the EDA script (uses data/Uber Request Data.csv by default)
python3 src/uber_request_eda.py --out outputs
```

Open `notebooks/uber_request_project.ipynb` in Jupyter to view the exploratory workflow with Markdown explanations and inline plots.

Notes

- The script writes four PNG visualisations to the `--out` folder and prints concise answers to the four research questions.
- Use `requirements_frozen.txt` for exact reproducibility; `requirements.txt` (if present) contains minimal, unpinned requirements.
