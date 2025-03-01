## Google Trends Data Analysis Script

This Python script retrieves and visualizes hourly Google Trends data for a specified keyword across several Indonesian provinces. It utilizes the `pytrends` library to fetch trend data, `pandas` for data manipulation, and `matplotlib` for plotting.

### Functionality

* **Data Retrieval:** Fetches hourly Google Trends data for a given keyword across specified provinces using the `pytrends` library.
* **Data Processing:** Filters the retrieved data to include only non-zero trend values.
* **Data Storage:** Saves the processed trend data for each province to individual CSV files.
* **Data Visualization:** Generates a plot showing the hourly trend data for the keyword across all specified provinces.
* **Data Display:** Prints the latest 5 data points for each province.

### Libraries Used

* `pytrends`: For fetching Google Trends data.
* `pandas`: For data manipulation and storage.
* `matplotlib`: For data visualization.

### Usage

1.  **Installation:**
    * Ensure you have Python 3.x installed.
    * Install the required libraries: `pip install pytrends pandas matplotlib`

2.  **Running the Script:**
    * Save the script as a `.py` file.
    * Run the script from your terminal: `python your_script_name.py`

3.  **Output:**
    * The script will generate CSV files for each province containing the hourly trend data.
    * A plot will be displayed, visualizing the trend data across all provinces.
    * The latest 5 data points for each province will be printed to the console.

### Customization

* **Keywords:** Modify the `kw_list` variable to change the search keyword.
* **Provinces:** Adjust the `province_codes` dictionary to include or exclude provinces.
* **Timeframe:** Change the `timeframe` parameter in `pytrends.build_payload()` to adjust the time range of the data.
* **Plotting:** Customize the plot appearance using `matplotlib` functions.

### Notes

* Ensure you have a stable internet connection to fetch data from Google Trends.
* The script may take some time to execute, depending on the number of provinces and the timeframe selected.
* The output CSV files and plot can be used for further analysis or reporting.
