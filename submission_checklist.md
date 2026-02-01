# Submission Checklist

Status of required items for the assignment:

- **1) Dataset size:** PASS — dataset `Uber Request Data.csv` contains 6,745 rows and 6 columns.
- **2) Questions:** PASS — four research questions (Q1–Q4) are asked and answered in the notebook and script.
- **3) Visualisations:** PASS — four plots are produced and saved:
  - `q1_status_distribution.png`
  - `q2_hourly_demand_supply_gap.png`
  - `q3_unmet_rates_by_pickup.png`
  - `q4_gap_heatmap_weekday_hour.png`
- **4) Runnable .py:** PASS — `uber_request_eda.py` runs from the terminal and saves plots to an output folder.
- **5) Notebook:** PASS — `uber_request_project.ipynb` contains code, Markdown explanations, questions, and inline visualisations.

Reproduce steps

1. (Optional) Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements_frozen.txt
```

2. Run the EDA script (uses `Uber Request Data.csv` by default):

```bash
python3 uber_request_eda.py --out outputs_submission
```

3. Check outputs in `outputs_submission` (or the folder you supplied to `--out`).

Project files of interest

- `uber_request_eda.py` (runnable script)
- `uber_request_project.ipynb` (exploratory notebook with explanations)
- `Uber Request Data.csv` (dataset)
- `requirements_frozen.txt` (pinned dependencies)
- `README.md` (usage and install instructions)

To create a submission package, compress the `dscd_611_gr_A14` folder into a ZIP file.
