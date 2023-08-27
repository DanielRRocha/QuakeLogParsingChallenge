# Quake Log Parsing Challenge

This repository contains a Python script that parses Quake log files and extracts statistics about the games played.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contributing](#contributing)

## Introduction

This script processes Quake log files and extracts various statistics about the games played. It parses the log file to identify game starts, kills, and other events to generate game statistics.

The main purpose of this script is to demonstrate parsing and data extraction from Quake log files.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DanielRRocha/QuakeLogParsingChallenge.git

2. Change to the project directory:

  ```bash
  cd QuakeLogParsingChallenge
  ```
3. (Optional) Set up a virtual environment:
  ```bash
  python3 -m venv venv
source venv/bin/activate
  ```
## Usage
To use the script, follow these steps:

1. Run the script using the following command:
  ```bash
  python quakeLogParse.py
  ```
2. The script will process the provided Quake log file, extract game statistics, and print the results.

Please note that the script includes a predefined log data for testing purposes. You can modify the `process_log` function to read from an actual URL or file, if needed.

## Documentation
Code Explanation
The script quakeLogParse.py is responsible for processing Quake log files and generating game statistics. It follows these steps:

* Imports necessary libraries and modules.
* Defines regular expression patterns for parsing the log file.
* Sets up data storage using dictionaries and default dictionaries.
* Reads the log file using urllib.request.urlopen.
* Iterates through the lines of the log file, parsing and processing each line.
* Generates game statistics such as total kills, player lists, kill counts, and kills by means.
* Prints the extracted statistics for each game.
### Function process_log(log_url)
This function takes a log URL as input and processes the log file at that URL. It extracts game statistics and returns the game_stats dictionary containing the extracted data.

### Function main()
This function serves as the entry point for the script. It calls the process_log function and prints the extracted game statistics for each game.


## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please feel free to open an issue or create a pull request.

### Using Git Flow

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine:

    ```bash
    git clone https://github.com/DanielRRocha/QuakeLogParsingChallenge
  
3. Change to the project directory:

    ```bash
    cd QuakeLogParsingChallenge
    ```

4. Set up the Git Flow repository structure:
    ```bash
    git flow init
    ```
5. Create a new feature branch based on the develop branch:
    ```bash
    git flow feature start your-feature-name
    ```
6. Make your changes and commit them:
    ```bash
    git add .
    git commit -m "Add description of changes"
    ```
7. Push your feature branch to your forked repository:
    ```bash
    git push origin feature/your-feature-name

8. Open a pull request from your feature branch to the develop branch of the original repository.

9. Your pull request will be reviewed. We will test your code, and if it works as expected, we will merge it into the main branch.

Please make sure to keep your forked repository in sync with the original repository by regularly pulling the latest changes from the main branch.