from subprocess import Popen, PIPE
import os
import tqdm
import csv
import subprocess


def main():

    downstream_test_pyfiles = os.listdir("test_all")
    try:
        os.makedirs(os.path.join("test_logs", "all"))
    except:
        pass
    for downstream_test_pyfile in tqdm.tqdm(downstream_test_pyfiles[9:]):
        downstream_name = "_".join(downstream_test_pyfile.split('.')[0].split("_")[1:])
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
        pyfile_path = os.path.join("test_all", downstream_test_pyfile)
        with open(os.path.join("test_logs", "all", downstream_name + ".log"), mode="w") as wf:
            p = Popen(["python3", pyfile_path], stdout=wf, stderr=wf)
            try:
                p.communicate(timeout=12600)
            except:
                p.kill()


if __name__ == '__main__':
    main()
