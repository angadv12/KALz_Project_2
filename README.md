# KALz Project 2

## 1. Software and Platform
- All packages installed located in `requirements.txt`
> Run `pip install -r requirements.txt` to install all at once
- Used Mac & Windows during development

## 2. Repository Map
```
[Project Folder]/
├── data/
│   ├── sea_ice_data_clean.csv
├── output/
│   ├── [VARIOUS IMAGES]
│   ├──  ...
│   ├── [VARIOUS IMAGES]
│   ├── [VARIOUS .CSV FILES]
│   ├──  ...
│   └── [VARIOUS .CSV FILES]
├── scripts/
│   ├── MI2_EDA.py
├── venv/
├── .gitignore
├── LICENSE.md
├── README.md
└── requirements.txt
```
> [!NOTE]
> The models and venv/ were git ignored due to size; create them using directions below.
> You can delete everything in OUTPUT/ and recreate using the scripts if you would like.

## 3. How to reproduce our results
> [!NOTE]
> Ensure python is set up on your system.
> Run ALL terminal commands from the root directory.
> Use `python3` instead of `python` if commands aren't running.

### Create a virtual environment and install packages
Virtual environments isolate your packages to your current environment \
In your terminal:
- Create environment: `python -m venv venv`
- Activate it:
	- On macOS: `source venv/bin/activate`
	- On Windows: `source venv/Scripts/activate`
### Run python scripts
In your terminal:
- add here

## 4. References
[1]“Arctic sea ice maximum: Crisis as ice melts and risks rise - WWF Arctic,” WWF Arctic, Mar. 28, 2025. https://www.arcticwwf.org/newsroom/features/arctic-sea-ice-maximum-crisis-as-ice-melts-and-risks-rise/

‌[2] C. Grewcoe, “Time-Series Analysis: What Is It and How to Use It,” Timescale Blog, Mar. 12, 2024. https://www.tigerdata.com/blog/time-series-analysis-what-is-it-how-to-use-it 

[3] R. Lindsey and M. Scott, “Climate Change: Arctic Sea Ice Summer Minimum | NOAA Climate.gov,” www.climate.gov, Oct. 18, 2022. https://www.climate.gov/news-features/understanding-climate/climate-change-arctic-sea-ice-summer-minimum

[4]“Sea Ice Index, Version 4 | National Snow and Ice Data Center,” Nsidc.org, Mar. 2021, doi: https://doi.org/10.7265/a98x-0f50.
