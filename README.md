# Research notebook
- Based on the data from [SeoulHouse/Scraper](https://github.com/seoulhouse/scraper)
- Research on the data on flats in Seoul

## Launch notebook
on cloud
```
jupyter notebook --ip=0.0.0.0 --port=8080 --no-browser
```

locally
```
jupyter notebook
```

## Get the working URL of the notebook (when running on Cloud9...)
- See [this issue](https://community.c9.io/t/cant-preview-in-aws-c9/23340)
- Go to your EC2 console
- Find the 32 letters long string comprised of random numbers and alphabets under 'Security Group' in 'Details'
- Go browse https://[32 letters].vfs.cloud9.[your region].amazonaws.com/
- `your region` is something like `us-east-1`
