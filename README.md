# Scraping and Data Processing with Python

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)

## Table of Contents

- [Usage](#usage)
  - [Prerequisites](#prerequisites)
  - [Example Usage](#example-usage)
- [Authors](#authors)
- [License](#license)
- [Contributions](#contributions)
- [Features](#features)
- [Installation](#installation)
- [Example Usage](#example-usage)

## Usage

### Prerequisites

Before running the scripts, ensure you have the following libraries installed:

- requests
- json
- pandas
- hdfs
- BeautifulSoup

### Example Usage

Here's how you can use these scripts:

1. Run `scrapping.py` to scrape data from Mastodon and store it in HDFS.
2. Run `mapper.py` to process the data.
3. Run `hbase.py` to store the processed data in HBase.

## Authors

- [Taha SRHAYAR](https://github.com/tsrhayar)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome. Feel free to open a pull request.

## Features

- `scrapping.py`: This script uses the `requests` library to extract data from Mastodon, cleans and formats the data, and stores it in a distributed file system HDFS.

- `mapper.py`: This script takes the data extracted by `scrapping.py`, performs analysis and mapping of relevant information, and generates structured output for storage.

- `hbase.py`: This script connects the project to an HBase NoSQL database and stores the mapped data in specific tables.

## Installation

You can install the required libraries using `pip`:

```bash
pip install requests json pandas hdfs beautifulsoup4
