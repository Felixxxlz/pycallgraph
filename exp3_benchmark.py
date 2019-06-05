from subprocess import Popen, PIPE
import os
import tqdm
import csv
import subprocess
import json
import time
import sqlite3


def init_environment():
    p = Popen("sudo -S pip3 uninstall numpy", shell=True, stdin=PIPE)
    p.communicate(bytes("Ly941122\ny\n", encoding="utf-8"))
    p = Popen("sudo -S pip3 install numpy", shell=True, stdin=PIPE)
    p.communicate(bytes("Ly941122" + "\n", encoding="utf-8"))

    p = Popen("sudo -S pip3 uninstall scipy", shell=True, stdin=PIPE)
    p.communicate(bytes("Ly941122\ny\n", encoding="utf-8"))
    p = Popen("sudo -S pip3 install scipy", shell=True, stdin=PIPE)
    p.communicate(bytes("Ly941122" + "\n", encoding="utf-8"))

    p = Popen("sudo -S pip3 uninstall pandas", shell=True, stdin=PIPE)
    p.communicate(bytes("Ly941122\ny\n", encoding="utf-8"))
    p = Popen("sudo -S pip3 install pandas", shell=True, stdin=PIPE)
    p.communicate(bytes("Ly941122" + "\n", encoding="utf-8"))

    p = Popen("sudo -S pip3 uninstall astropy", shell=True, stdin=PIPE)
    p.communicate(bytes("Ly941122\ny\n", encoding="utf-8"))
    p = Popen("sudo -S pip3 install astropy", shell=True, stdin=PIPE)
    p.communicate(bytes("Ly941122" + "\n", encoding="utf-8"))

    p = Popen("sudo -S pip3 uninstall scikit-learn", shell=True, stdin=PIPE)
    p.communicate(bytes("Ly941122\ny\n", encoding="utf-8"))
    p = Popen("sudo -S pip3 install scikit-learn", shell=True, stdin=PIPE)
    p.communicate(bytes("Ly941122" + "\n", encoding="utf-8"))


def main():
    upstreams = ("numpy", "scipy", "astropy", "pandas", "sklearn")
    with open("exp3_config_related_downstreams.json", mode="r") as rf:
        config = json.load(rf)
    for upstream in upstreams[3:]:
        init_environment()
        versions = [sha for sha in config[upstream]]
        conn = sqlite3.connect("benchmark_test_logs/databases/test_info.db")
        for version in versions:
            if upstream == "sklearn":
                tmp_upstream = "scikit-learn"
            else:
                tmp_upstream = upstream
            os.chdir(os.path.join("repos", tmp_upstream))
            p = Popen(["git", "checkout", "master"])
            p.communicate()
            p = Popen(["git", "checkout", version])
            p.communicate()
            p = Popen("sudo -S pip3 install .", shell=True, stdin=PIPE)
            p.communicate(bytes("Ly941122" + "\n", encoding="utf-8"))
            os.chdir(os.path.join("..", ".."))

            try:
                p = Popen("find repos -name \"__pycache__\" | xargs rm -r", shell=True)
                p.communicate()
            except:
                pass

            try:
                os.makedirs(os.path.join("benchmark_test_logs", upstream, version))
            except:
                pass
            related_downstreams = [item["downstream"] for item in config[upstream][version]]
            for downstream in tqdm.tqdm(related_downstreams):
                # if downstream not in ("sklearn_lvq", "geometer", "randomgen"):
                #     continue
                print(downstream)
                pyfile_path = os.path.join("test_all", "test_" + downstream + ".py")
                log_path = os.path.join("benchmark_test_logs", upstream, version, \
                    downstream + ".log")
                # if os.path.exists(log_path):
                #     continue
                with open(log_path, mode="w") as wf:
                    p = Popen(["python3", pyfile_path], stdout=wf, stderr=wf)
                    start_time = time.time()
                    try:
                        p.communicate(timeout=3600)
                    except:
                        p.kill()
                    cost = time.time() - start_time
                    conn.execute("insert or replace into %s values (?,?,?,?);" % (upstream, ), (upstream, version, downstream, cost))
                    conn.commit()
        conn.close()


if __name__ == '__main__':
    main()
