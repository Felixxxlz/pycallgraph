from subprocess import Popen, PIPE
import os
import tqdm
import csv
import subprocess


def main():
    astropy_versions = ['c73640ba0da2807dc467d76de21b51fbbc1ca3c0', '2394af9f65825d48961457636fe8b5d40d8ad9b9', '2ce0412596517cc6cee49541495208b3a5e66531', '5cec111b9595ff6ce097a9381b8f804d202ba8c2', 'e3b9fbecdc9ae34db5a88ccfcb9c067352886391', '89bb7a1e71eda4e4d6baece0460206a7f062a93c', 'b6be4e54ffb60df5088c28c0dcc9c283b7201c4d', 'e9a32561c9e828f93dfab71138e977a147e0e442', '4dfef4bc64be527ae63a099c2c3d7ce0e2b0a36f']
    for astropy_version in astropy_versions:
        os.chdir(os.path.join("..", "REPOS", "astropy"))
        p = Popen(["git", "checkout", "master"])
        p.communicate()
        p = Popen(["git", "checkout", astropy_version])
        p.communicate()
        p = Popen("sudo -S -H pip3 install . --no-cache-dir", shell=True, stdin=PIPE)
        p.communicate(bytes("Ly941122" + "\n", encoding="utf-8"))
        os.chdir(os.path.join("..", "..", "pycallgraph"))

        downstream_test_pyfiles = os.listdir("test_astropy")
        ok = set()
        with open(os.path.join("results", "astropy", astropy_version + ".csv"), encoding="gbk") as rf:
            reader = csv.reader(rf)
            next(reader)
            for row in reader:
                if int(row[4]):
                    ok.add(row[1])
        astropy_version = astropy_version[:7]
        try:
            os.makedirs(os.path.join("test_logs", "astropy", astropy_version))
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
            pyfile_path = os.path.join("test_astropy", downstream_test_pyfile)
            with open(os.path.join("test_logs", "astropy", astropy_version, \
                "test_log_" + downstream_name + ".txt"), mode="w") as wf:
                p = Popen(["python3", pyfile_path], stdout=wf, stderr=wf)
                try:
                    p.communicate(timeout=12600)
                except:
                    p.kill()


if __name__ == '__main__':
    main()
