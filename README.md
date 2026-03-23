# KALz Project 2

## 1. Software and Platform
- **Python 3**: packages listed in `requirements.txt` (run `pip install -r requirements.txt`)
- **R (4.0+)**: packages: dplyr, ggplot2, zoo, forecast, tseries, lubridate, knitr, rmarkdown, tinytex
- Used Mac & Windows during development

## 2. Repository Map
```
[Project Folder]/
├── data/
│   ├── sea_ice_data_clean.csv          # Cleaned Arctic sea ice dataset (NSIDC)
├── output/
│   ├── DS4002Project2Code.pdf          # Rendered R Markdown report with all analysis outputs
│   ├── figure1_extent_over_time.png    # EDA: Sea ice extent over time
│   ├── figure2_area_over_time.png      # EDA: Sea ice area over time
│   ├── figure3_average_extent_by_month.png  # EDA: Average extent by month
│   ├── figure3_average_extent_by_month.png  # EDA: Average extent by month
│   ├── figure4_march_vs_september_extent.png # EDA: March vs September extent
│   ├── figure5_average_extent_over_time.png # EDA: Average extent over time
│   ├── figure6_linear_annual_extent.png # Model Output: Linear model extent
│   ├── figure7_quadratic_annual_extent.png # Model Output: Quadratic model extent
│   ├── figure8_decade_SD_extent.png # SD Analysis: Volatility analysis
│   ├── figure9_linear_forecast_extent.png # Model Output: Linear future forecast extent
│   ├── figure10_model_output.png # Model Output: Model output for linear, quadratic, and ARIMA models
│   └── figure11_linear_arima_forecast.png # Model Output: Linear and ARIMA near-zero values
├── scripts/
│   ├── MI2_EDA.py                      # Python EDA script (generates figures 1-4)
│   └── DS4002Project2Code.Rmd          # R Markdown script (full analysis, modeling, and forecasting)
├── Data Appendix.pdf                   # Data appendix describing variables and sources
├── venv/                               # Python virtual environment (git ignored)
├── .gitignore
├── LICENSE.md
├── README.md
└── requirements.txt                    # Python package dependencies
```
> [!NOTE]
> The venv/ directory was git ignored due to size; create it using directions below.
> You can delete everything in output/ and recreate using the scripts if you would like.

## 3. How to reproduce our results
> [!NOTE]
> Ensure Python and R are set up on your system.
> Run ALL terminal commands from the project root directory.
> Use `python3` instead of `python` if commands aren't running.

### Create a virtual environment and install Python packages
Virtual environments isolate your packages to your current environment.
In your terminal:
- Create environment: `python -m venv venv`
- Activate it:
	- On macOS: `source venv/bin/activate`
	- On Windows: `source venv/Scripts/activate`
- Install packages: `pip install -r requirements.txt`

### Run the Python EDA script
In your terminal:
- `python scripts/MI2_EDA.py`
- This generates figures 1-4 in the `output/` folder.

### Install R and required R packages
> [!NOTE]
> R (version 4.0+) must be installed on your system. Download from [CRAN](https://cran.r-project.org/). \
> RStudio is recommended (unless you know what you're doing) Download from [RStudio Desktop](https://posit.co/download/rstudio-desktop/). \
> Download [XQuartz](https://www.xquartz.org/) if on macOS

In an R console, install the required packages:
```r
install.packages(c("dplyr", "ggplot2", "zoo", "forecast", "tseries", "lubridate", "knitr", "rmarkdown", "tinytex"))
tinytex::install_tinytex()
```

### Run the R Markdown analysis script
The R Markdown file contains the full analysis: data cleaning, descriptive statistics, trend analysis, ARIMA modeling, and near-zero forecasting.

**Open in RStudio:**
1. Open `scripts/DS4002Project2Code.Rmd` in RStudio.
2. Click **Knit** to render the full report.

## 4. References
[1]“Arctic sea ice maximum: Crisis as ice melts and risks rise - WWF Arctic,” WWF Arctic, Mar. 28, 2025. https://www.arcticwwf.org/newsroom/features/arctic-sea-ice-maximum-crisis-as-ice-melts-and-risks-rise/

‌[2] C. Grewcoe, “Time-Series Analysis: What Is It and How to Use It,” Timescale Blog, Mar. 12, 2024. https://www.tigerdata.com/blog/time-series-analysis-what-is-it-how-to-use-it 

[3] R. Lindsey and M. Scott, “Climate Change: Arctic Sea Ice Summer Minimum | NOAA Climate.gov,” www.climate.gov, Oct. 18, 2022. https://www.climate.gov/news-features/understanding-climate/climate-change-arctic-sea-ice-summer-minimum

[4]“Sea Ice Index, Version 4 | National Snow and Ice Data Center,” Nsidc.org, Mar. 2021, doi: https://doi.org/10.7265/a98x-0f50.
