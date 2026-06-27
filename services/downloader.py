import pandas as pd
import requests

def download_csv(url, filename):

    r = requests.get(url)

    with open(filename, "wb") as f:
        f.write(r.content)

    return filename