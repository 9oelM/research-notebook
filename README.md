# Scraper
- Scrapes data on flats in Seoul from [Zigbang](https://www.zigbang.com/)
- Modified from the master branch to enable local scraping instead of on AWS lambda. 
- Research note taken on Jupyter notebook

## Usage
```
python3 handler.py
```

## Setup
0. Make sure you are using `python3.6+` and a decent `pip`
    ```bash
    python3 --version
    pip install --upgrade pip
    ```

1. Install `pipenv` and install packages
    ```bash
    pip install pipenv
    pipenv install 
    ```

2. Install node lts
    ```bash
    nvm install stable
    ```

3. Install `serverless` globally and install python requirements plugin
    ```bash
    npm install -g serverless
    serverless sls plugin install -n serverless-python-requirements
    ```

4. Install npm packages
    ```bash
    npm install 
    ```