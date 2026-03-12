from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def month_num_to_name(month_num: int) -> str:
    month_map = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec",
    }
    return month_map.get(month_num, str(month_num))


def load_data() -> pd.DataFrame:
    """
    Load cleaned sea ice data from the repository data folder.
    """
    # build dataset path relative to this script location
    repo_root = Path(__file__).resolve().parents[1]
    data_path = repo_root / "data" / "sea_ice_data_clean.csv"
    
	# load into dataframe
    df = pd.read_csv(data_path)

	# check for missing cols
    required_cols = {"year", "mo", "extent", "area"}
    missing_cols = required_cols - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

	# enforce numeric columns to be numeric
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["mo"] = pd.to_numeric(df["mo"], errors="coerce")
    df["extent"] = pd.to_numeric(df["extent"], errors="coerce")
    df["area"] = pd.to_numeric(df["area"], errors="coerce")

	# drop rows w/ missing data
    df = df.dropna(subset=["year", "mo", "extent", "area"]).copy()
    df["year"] = df["year"].astype(int)
    df["mo"] = df["mo"].astype(int)

	# create date column for plotting later
    df = df.sort_values(["year", "mo"]).reset_index(drop=True)
    df["date"] = pd.to_datetime(
        dict(year=df["year"], month=df["mo"], day=1),
        errors="coerce",
    )

    return df


# helper for consistent save formats
def save_figure(fig: plt.Figure, output_path: Path) -> None:
    fig.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)

"""
Separate functions below for creating each plots (easeir to read)
- each one takes df and output path as input, creates figure, and saves to output path
"""

def plot_extent_over_time(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Figure 1: Arctic sea ice extent over time.
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["date"], df["extent"], linewidth=1.8)

    ax.set_title("Figure 1. Sea Ice Extent Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Extent (million sq. km)")
    ax.grid(True, alpha=0.3)

    save_figure(fig, output_dir / "figure1_extent_over_time.png")


def plot_area_over_time(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Figure 2: Arctic sea ice area over time.
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["date"], df["area"], linewidth=1.8)

    ax.set_title("Figure 2. Sea Ice Area Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Area (million sq. km)")
    ax.grid(True, alpha=0.3)

    save_figure(fig, output_dir / "figure2_area_over_time.png")


def plot_average_extent_by_month(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Figure 3: Average sea ice extent by month.
    """
    monthly_avg = (
        df.groupby("mo", as_index=False)["extent"]
        .mean()
        .sort_values("mo")
    )
    monthly_avg["month_name"] = monthly_avg["mo"].apply(month_num_to_name)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(monthly_avg["month_name"], monthly_avg["extent"])

    ax.set_title("Figure 3. Average Sea Ice Extent by Month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Average Extent (million sq. km)")
    ax.grid(True, axis="y", alpha=0.3)

    save_figure(fig, output_dir / "figure3_average_extent_by_month.png")


def plot_march_vs_september(df: pd.DataFrame, output_dir: Path) -> None:
    """
    Figure 4: March vs September sea ice extent over time.
    """
    march_df = df[df["mo"] == 3][["year", "extent"]].copy()
    september_df = df[df["mo"] == 9][["year", "extent"]].copy()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(
        march_df["year"],
        march_df["extent"],
        label="March",
        linewidth=2.0,
    )
    ax.plot(
        september_df["year"],
        september_df["extent"],
        label="September",
        linewidth=2.0,
    )

    ax.set_title("Figure 4. March vs September Sea Ice Extent Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Extent (million sq. km)")
    ax.legend()
    ax.grid(True, alpha=0.3)

    save_figure(fig, output_dir / "figure4_march_vs_september_extent.png")


# main function to run all above steps
def main() -> None:
    # path building, output dir defining
    repo_root = Path(__file__).resolve().parents[1]
    output_dir = repo_root / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    df = load_data()

	# create and save all figures
    plot_extent_over_time(df, output_dir)
    plot_area_over_time(df, output_dir)
    plot_average_extent_by_month(df, output_dir)
    plot_march_vs_september(df, output_dir)

    print("EDA figures created successfully in the output/ folder.")

if __name__ == "__main__":
    main()