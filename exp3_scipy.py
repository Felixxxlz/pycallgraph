from subprocess import Popen, PIPE
import os
import tqdm
import csv
import subprocess


def main():
    scipy_versions = ["429ce001c85a9bdb8b1b65eb0c38ba84917055f4", "3a3361c964e0c7c0543d4c4752a1b8fa0bab27d4", "bc124d0f9c0b37c29bb4df2ea71b463a41e469ec",
    "9262aee2ceb789e8440ecb9ee3691a6c7dfd962c", "0f5d8aab5d9990c433168ad3424b3f5c9440978e",
    "4dd1792909bd725ff057ceb00f8dfabe9eab1c02", "33049dcbed33580cb32ce8410faff6a90deb2228",
    "54e1727a603f7698957f43ea2cd6236fe2530615", "c12ec062c0623aab8162665de103d8c9ab9cd103",
    "0d6506aee44ee6d223fb6dea13ed06de4a935afe", "f6548033bb57350da1165ab0089e1a7fcc910736",
    "5d5188e01d197b9bc5d16cb703d69862deaacd46", "1bdab7c5f6391e710a6ebbd1a22501ef295b16ca"]
    for scipy_version in scipy_versions:
        os.chdir(os.path.join("..", "REPOS", "scipy"))
        p = Popen(["git", "checkout", "master"])
        p.communicate()
        p = Popen(["git", "checkout", scipy_version])
        p.communicate()
        p = Popen("sudo -S pip3 install . --no-cache-dir", shell=True, stdin=PIPE)
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
                "test_log_" + downstream_name + ".txt"), mode="w") as wf:
                p = Popen(["python3", pyfile_path], stdout=wf, stderr=wf)
                try:
                    p.communicate(timeout=12600)
                except:
                    p.kill()


if __name__ == '__main__':
    main()
