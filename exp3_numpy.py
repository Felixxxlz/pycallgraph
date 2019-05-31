from subprocess import Popen, PIPE
import os
import tqdm
import csv
import subprocess
import json
import time
import sqlite3


def main():
    upstream = "numpy"
    with open("exp3_config_related_downstreams.json", mode="r") as rf:
        config = json.load(rf)
    versions = [sha for sha in config[upstream]]
    conn = sqlite3.connect("benchmark_test_logs/databases/test_info.db")
    for version in versions:
        os.chdir(os.path.join("repos", upstream))
        p = Popen(["git", "checkout", "master"])
        p.communicate()
        p = Popen(["git", "checkout", version])
        p.communicate()
        p = Popen("sudo -S pip3 install .", shell=True, stdin=PIPE)
        p.communicate(bytes("Ly941122" + "\n", encoding="utf-8"))
        os.chdir(os.path.join("..", ".."))

        try:
            p = Popen("find repos -name \"pycache\" | xargs rm -r")
            p.communicate()
        except:
            pass

        try:
            os.makedirs(os.path.join("benchmark_test_logs", upstream, version))
        except:
            pass
        related_downstreams = [item["downstream"] for item in config[upstream][version]]
        for downstream in tqdm.tqdm(related_downstreams):
            print(downstream)
            pyfile_path = os.path.join("test_all", "test_" + downstream + ".py")
            with open(os.path.join("benchmark_test_logs", upstream, version, \
                downstream + ".log"), mode="w") as wf:
                p = Popen(["python3", pyfile_path], stdout=wf, stderr=wf)
                start_time = time.time()
                try:
                    p.communicate(timeout=12600)
                except:
                    p.kill()
                cost = time.time() - start_time
                conn.execute("insert or replace into %s values (?,?,?,?);" % (upstream, ), (upstream, version, downstream, cost))
                conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
