from subprocess import Popen, PIPE
import os
import tqdm
import csv
import subprocess


def main():
    scipy_versions = ['0d6506aee44ee6d223fb6dea13ed06de4a935afe', 'e28b999aed912641acebc4bf88637a12b83fa885', 'f4f3c0ed831cc34824bffb0bc3c1f65e3ee4ddab', 'bc124d0f9c0b37c29bb4df2ea71b463a41e469ec', '429ce001c85a9bdb8b1b65eb0c38ba84917055f4', '54e1727a603f7698957f43ea2cd6236fe2530615', '4dd1792909bd725ff057ceb00f8dfabe9eab1c02']
    for scipy_version in scipy_versions:
        os.chdir(os.path.join("..", "REPOS", "scipy"))
        p = Popen(["git", "checkout", "master"])
        p.communicate()
        p = Popen(["git", "checkout", scipy_version])
        p.communicate()
        p = Popen("sudo -S -H pip3 install . --no-cache-dir", shell=True, stdin=PIPE)
        p.communicate(bytes("Ly941122" + "\n", encoding="utf-8"))
        os.chdir(os.path.join("..", "..", "pycallgraph"))

        downstream_test_pyfiles = os.listdir("test_scipy")
        ok = set()
        with open(os.path.join("results", "scipy", scipy_version + ".csv"), encoding="gbk") as rf:
            reader = csv.reader(rf)
            next(reader)
            for row in reader:
                if int(row[4]):
                    ok.add(row[1])
        scipy_version = scipy_version[:7]
        try:
            os.makedirs(os.path.join("test_logs", "scipy", scipy_version))
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
            pyfile_path = os.path.join("test_scipy", downstream_test_pyfile)
            with open(os.path.join("test_logs", "scipy", scipy_version, \
                downstream_name + ".log"), mode="w") as wf:
                p = Popen(["python3", pyfile_path], stdout=wf, stderr=wf)
                try:
                    p.communicate(timeout=12600)
                except:
                    p.kill()


if __name__ == '__main__':
    main()
