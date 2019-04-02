import requests
import os
import time
from tqdm import tqdm
import json
import csv


topic_url = "https://api.github.com/search/repositories?&q=topic:numpy&order=desc&sort=stars&page=%d"
headers = {
    "Accept": "application/vnd.github.mercy-preview+json"
}
csv_header = ("项目", "版本", "获取代码时间", "测试用例个数", "节点个数", "边数", "运行时间")

def craw_numpy_topic():
    s = requests.Session()

    for i in tqdm(range(1, 35)):
        resp = s.get(topic_url % (i, ), headers=headers, auth=("yannluo", "Ly941122"))
        with open(os.path.join("numpy_topics", "%d.json" % (i, )), mode="w", encoding="utf-8") as wf:
            wf.write(resp.text)
        if i % 20 == 0:
            time.sleep(60)


def archive_repos():
    repos = []
    files = os.listdir("numpy_topics")
    for i in range(1, 35):
        file = "%d.json" % (i, )
        with open(os.path.join("numpy_topics", file), mode="r", encoding="utf-8") as rf:
            json_content = json.load(rf)
            repos.extend([item["full_name"] for item in json_content["items"]])
    repos = list(set(repos))
    repos.sort()
    return repos


def main():
    # craw_numpy_topic()
    repos = archive_repos()
    with open("1.csv", mode="w", encoding="utf-8") as wf:
        writer = csv.writer(wf)
        writer.writerow(csv_header)
        for repo in repos[0:403]:
            writer.writerow((repo,"","","","","",""))


if __name__ == "__main__":
    main()
