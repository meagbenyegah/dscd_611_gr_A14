# Uber Request EDA (DSCD_611 — Group A14)

Lightweight, reproducible exploratory data analysis of Uber trip requests (DSCD_611 — Group A14). The repository includes the dataset (sourced from Kaggle — https://www.kaggle.com/datasets/anupammajhi/uber-request-data), a Jupyter notebook documenting the analysis, a runnable script that generates the required figures and answers, and pinned dependencies to reproduce the results.

Repository layout

- `data/` — source data: `Uber Request Data.csv`
- `docs/` — project deliverables: project report (`Report_611_A14.pdf`) and presentation slides (`Presentation_611_A14.pptx`)
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

This repository uses the `Uber Request Data.csv` file (stored in the `data/` folder) as the chosen dataset for the assignment. The data for this project was obtained from Kaggle: "Uber Request Data" by `anupammajhi` — https://www.kaggle.com/datasets/anupammajhi/uber-request-data. Please refer to the Kaggle dataset page for full provenance and licensing details.
