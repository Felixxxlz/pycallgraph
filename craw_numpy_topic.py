import requests
import os
import time
from tqdm import tqdm
import json


topic_url = "https://api.github.com/search/repositories?&q=topic:numpy&order=desc&sort=stars&page=%d"
headers = {
    "Accept": "application/vnd.github.mercy-preview+json"
}


def craw_numpy_topic():
    s = requests.Session()

    for i in tqdm(range(1, 35)):
        resp = s.get(topic_url % (i, ), headers=headers, auth=("yannluo", "Ly941122"))
        with open(os.path.join("numpy_topics", "%d.json" % (i, )), mode="w", encoding="utf-8") as wf:
            wf.write(resp.text)
        if i % 20 == 0:
            time.sleep(60)


def archive_repo():
    repos = []
    files = os.listdir("numpy_topics")
    for i in range(1, 35):
        file = "%d.json" % (i, )
        with open(os.path.join("numpy_topics", file), mode="r", encoding="utf-8") as rf:
            json_content = json.load(rf)
            repos.extend([item["full_name"] for item in json_content["items"]])
    return list(set(repos))


def main():
    # craw_numpy_topic()
    archive_repo()


if __name__ == "__main__":
    main()
