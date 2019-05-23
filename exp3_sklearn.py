from subprocess import Popen, PIPE
import os
import tqdm
import csv
import subprocess


def main():
    sklearn_versions = ['358c6922f606a8e52e5b9a1ce4600a8eb643c12e', 'e574990d1ae5ce0d89b19020c1df1744fac9ddf8', '2718d6212f92220d5f228bfaf7bff0e75ea14965', 'a304db98c53cc9371185dd9e8f586fbb0aca95ec', 'f4e5224500d45a7ca01214041955aaaf4b7cae83']
    for sklearn_version in sklearn_versions:
        os.chdir(os.path.join("..", "REPOS", "scikit-learn"))
        p = Popen(["git", "checkout", "master"])
        p.communicate()
        p = Popen(["git", "checkout", sklearn_version])
        p.communicate()
        p = Popen("sudo -S -H pip3 install . --no-cache-dir", shell=True, stdin=PIPE)
        p.communicate(bytes("Ly941122" + "\n", encoding="utf-8"))
        os.chdir(os.path.join("..", "..", "pycallgraph"))

        downstream_test_pyfiles = os.listdir("test_sklearn")
        ok = set()
        with open(os.path.join("results", "sklearn", sklearn_version + ".csv"), encoding="gbk") as rf:
            reader = csv.reader(rf)
            next(reader)
            for row in reader:
                if int(row[4]):
                    ok.add(row[1])
        sklearn_version = sklearn_version[:7]
        try:
            os.makedirs(os.path.join("test_logs", "sklearn", sklearn_version))
        except:
            pass
        for downstream_test_pyfile in tqdm.tqdm(downstream_test_pyfiles):
            downstream_name = "_".join(downstream_test_pyfile.split('.')[0].split("_")[1:])
            if downstream_name not in ok:
                continue
            if downstream_name == "alphalens":
                continue
            if downstream_name == "joblib":
                continue
            if downstream_name == "dask":
                continue
            if downstream_name == "numpy_buffer":
                continue
            if downstream_name == "indi":
                continue
            print(downstream_name)
            pyfile_path = os.path.join("test_sklearn", downstream_test_pyfile)
            with open(os.path.join("test_logs", "sklearn", sklearn_version, \
                "test_log_" + downstream_name + ".txt"), mode="w") as wf:
                p = Popen(["python3", pyfile_path], stdout=wf, stderr=wf)
                try:
                    p.communicate(timeout=12600)
                except:
                    p.kill()


if __name__ == '__main__':
    main()
