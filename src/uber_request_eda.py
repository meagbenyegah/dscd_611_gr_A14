#!/usr/bin/env python3
"""Uber Request Data — Exploratory Data Analysis (EDA)

This script runs from the terminal and reproduces the project outputs:
- Answers to the research questions
- All required visualizations (saved to an output folder)

Problem context:
When riders request a trip but the trip is not fulfilled (cancelled or no cars available),
the platform loses revenue and customers lose trust. This EDA identifies *when* and *where*
unmet requests occur most often, to guide operational improvements.

Run example:
    python uber_request_eda.py --data "Uber Request Data.csv" --out outputs
"""
import argparse
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def robust_parse_datetime(s: pd.Series) -> pd.Series:
    # Two-pass parse to handle mixed datetime formats.
    dt1 = pd.to_datetime(s, errors="coerce", dayfirst=True)
    mask = dt1.isna()
    if mask.any():
        dt2 = pd.to_datetime(s[mask], errors="coerce", dayfirst=False)
        dt1.loc[mask] = dt2
    return dt1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="Uber Request Data.csv",
                        help="Path to Uber Request Data CSV (default: Uber Request Data.csv)")
    parser.add_argument("--out", default="outputs", help="Output folder for plots")
    parser.add_argument("--version", action="version", version="uber_request_eda 1.0")
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(args.data)

    # ---------------- Data preparation ----------------
    df["request_dt"] = robust_parse_datetime(df["Request timestamp"])
    df["drop_dt"] = robust_parse_datetime(df["Drop timestamp"])

    df["request_date"] = df["request_dt"].dt.date
    df["request_hour"] = df["request_dt"].dt.hour
    df["weekday"] = df["request_dt"].dt.day_name()

    df["is_completed"] = (df["Status"] == "Trip Completed").astype(int)
    df["is_cancelled"] = (df["Status"] == "Cancelled").astype(int)
    df["is_no_cars"] = (df["Status"] == "No Cars Available").astype(int)
    df["is_unmet"] = (df["Status"] != "Trip Completed").astype(int)

    print("\n==============================")
    print("Uber Request Data — EDA Results")
    print("==============================")
    print(f"Rows: {len(df):,} | Columns: {df.shape[1]:,}")
    print("Note: Missing Driver id / Drop timestamp is expected for unfulfilled requests.\n")

    # ---------------- Q1 ----------------
    print("Q1) What proportion of requests were completed vs unmet (cancelled/no cars)?")
    status_counts = df["Status"].value_counts()
    status_pct = (status_counts / len(df) * 100).round(2)
    for label in ["Trip Completed", "Cancelled", "No Cars Available"]:
        print(f"  - {label}: {int(status_counts.get(label, 0))} ({float(status_pct.get(label, 0)):.2f}%)")

    plt.figure()
    status_counts.loc[["Trip Completed","Cancelled","No Cars Available"]].plot(kind="bar")
    plt.title("Uber Requests by Status")
    plt.xlabel("Status")
    plt.ylabel("Number of Requests")
    plt.tight_layout()
    plt.savefig(out_dir / "q1_status_distribution.png", dpi=200)
    plt.close()

    # ---------------- Q2 ----------------
    print("\nQ2) What is the hourly demand pattern, and when is the supply–demand gap highest?")
    hourly = df.groupby("request_hour").agg(
        requests=("Request id","count"),
        completed=("is_completed","sum")
    ).reset_index()
    hourly["gap"] = hourly["requests"] - hourly["completed"]
    peak_gap_hour = int(hourly.loc[hourly["gap"].idxmax(), "request_hour"])
    peak_gap_value = int(hourly["gap"].max())
    print(f"  - Highest unmet-demand gap occurs at hour {peak_gap_hour}: gap = {peak_gap_value} requests")

    plt.figure()
    plt.plot(hourly["request_hour"], hourly["requests"], marker="o", label="Requests")
    plt.plot(hourly["request_hour"], hourly["completed"], marker="o", label="Trips Completed")
    plt.plot(hourly["request_hour"], hourly["gap"], marker="o", label="Unmet Demand (Gap)")
    plt.title("Hourly Demand, Supply, and Gap")
    plt.xlabel("Hour of Day")
    plt.ylabel("Count")
    plt.xticks(range(0,24))
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_dir / "q2_hourly_demand_supply_gap.png", dpi=200)
    plt.close()

    # ---------------- Q3 ----------------
    print("\nQ3) Does pickup point (City vs Airport) affect completion/cancellation/no-car rates?")
    by_pickup = df.groupby("Pickup point").agg(
        requests=("Request id","count"),
        completed=("is_completed","sum"),
        cancelled=("is_cancelled","sum"),
        no_cars=("is_no_cars","sum"),
    )
    by_pickup["completion_rate_pct"] = (by_pickup["completed"] / by_pickup["requests"] * 100).round(2)
    by_pickup["cancel_rate_pct"] = (by_pickup["cancelled"] / by_pickup["requests"] * 100).round(2)
    by_pickup["no_cars_rate_pct"] = (by_pickup["no_cars"] / by_pickup["requests"] * 100).round(2)

    for pickup in by_pickup.index:
        print(f"  - {pickup}: Completion={by_pickup.loc[pickup,'completion_rate_pct']}%, "
              f"Cancelled={by_pickup.loc[pickup,'cancel_rate_pct']}%, "
              f"No Cars={by_pickup.loc[pickup,'no_cars_rate_pct']}%")

    plt.figure()
    x = np.arange(len(by_pickup.index))
    plt.bar(x - 0.2, by_pickup["cancel_rate_pct"], width=0.4, label="Cancelled (%)")
    plt.bar(x + 0.2, by_pickup["no_cars_rate_pct"], width=0.4, label="No Cars (%)")
    plt.title("Unmet Requests by Pickup Point (Rates)")
    plt.xlabel("Pickup Point")
    plt.ylabel("Rate (%)")
    plt.xticks(x, by_pickup.index)
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_dir / "q3_unmet_rates_by_pickup.png", dpi=200)
    plt.close()

    # ---------------- Q4 ----------------
    print("\nQ4) What are the recurring weekday×hour hotspots for unmet demand?")
    daily = df.groupby("request_date").agg(
        requests=("Request id","count"),
        completed=("is_completed","sum")
    ).reset_index()
    daily["gap"] = daily["requests"] - daily["completed"]
    peak_gap_day = str(daily.loc[daily["gap"].idxmax(), "request_date"])
    peak_gap_day_value = int(daily["gap"].max())
    print(f"  - Highest gap day: {peak_gap_day} (gap = {peak_gap_day_value})")

    pivot = df.pivot_table(index="weekday", columns="request_hour", values="is_unmet", aggfunc="sum", fill_value=0)
    weekday_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    pivot = pivot.reindex([w for w in weekday_order if w in pivot.index])

    plt.figure(figsize=(10,4))
    plt.imshow(pivot.values, aspect="auto")
    plt.title("Unmet Requests (Gap) Heatmap: Weekday vs Hour")
    plt.xlabel("Hour of Day")
    plt.ylabel("Weekday")
    plt.xticks(ticks=np.arange(0,24), labels=np.arange(0,24))
    plt.yticks(ticks=np.arange(len(pivot.index)), labels=pivot.index)
    plt.colorbar(label="Unmet Requests")
    plt.tight_layout()
    plt.savefig(out_dir / "q4_gap_heatmap_weekday_hour.png", dpi=200)
    plt.close()

    print("\nAll plots saved to:", out_dir.resolve())

if __name__ == "__main__":
    main()
