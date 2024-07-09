# Telegram vacancies parser (DVC pipeline and S3 storage)

Parse posts from list of telegram channels using dvc pipeline. For parsing using [snscrape](https://github.com/tobe93gf/snscrape) library.



**Stage of pipeline:**

1) Parsing telegram channels 

2) Posts preprocessing (using for training model)

3) Push to S3 storage (in this project use cloud from cloud.ru)

## Project set up

`pip install poetry`

`poetry install `

Run dvc pipeline: 

`dvc repro`