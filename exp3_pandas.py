from subprocess import Popen, PIPE
import os
import tqdm
import csv
import subprocess


def main():
    pandas_versions = ['0f5a7e3a6edace63fcb342a1a0187856aee24b93', 'de3a85c8404505ace0c0febc26b1fbe824f48034', '025b5dcbcf27f8b3b74a415acc1a17bb50bcebae', '37d04a3d3df82c3abb80afc2ef6fcfa0b7d5df44', 'd8642e903cccb8fa0ea4d4477c89bbc1523b8c8e', '77713d5791a21faf88d49ce4c2505cc2eb7f6642', '27aa9d8733d20c5d96d9678dd7a0c0773ede58b7', '96a128eaa0a7425dd4285d219780ef29c2727e46', 'f2bcb9f0060d030085cdbaeeb638664c6f73e636', '8e54e556a6083c3ef26f246db36fb0ac556e846f', '2618b218eb4fad936310dcce011acc1b79e0ed96', '86879ac9af524adc684bec77c621d27b19a36ca0', 'dca809b0151adb744940a727f5d82ca43f4c3ea4', '27927056b368fa8c9501c4ec8729546dbe98068c', '4814a2875d078d6e9e9300bd1f77af15ef4f0f0a', '8311214023c4613758a5efbd9acb3894147aa704', '19626d2567487f8e698174de835c28c900784ed3', '6e0f9a971bcd07a4a6283dc03190b4363d42e292', '51c6a05477ffb5835ee52fc0bbb26e2f64f13bf7', '485cbbb9da072e19b5bd81b1e6b7f0643b5e5bc0', '05780f864f01653d4d7791cd4df66aca54716b4e', 'cb89bc0c012a3154fae394a7299e72ec75956c9b']
    for pandas_version in pandas_versions:
        os.chdir(os.path.join("..", "REPOS", "pandas"))
        p = Popen(["git", "checkout", "master"])
        p.communicate()
        p = Popen(["git", "checkout", pandas_version])
        p.communicate()
        p = Popen("sudo -S pip3 install . --no-cache-dir", shell=True, stdin=PIPE)
        p.communicate(bytes("Ly941122" + "\n", encoding="utf-8"))
        os.chdir(os.path.join("..", "..", "pycallgraph"))

        downstream_test_pyfiles = os.listdir("test_pandas")
        ok = set()
        with open(os.path.join("results", "pandas", pandas_version + ".csv"), encoding="gbk") as rf:
            reader = csv.reader(rf)
            next(reader)
            for row in reader:
                if int(row[4]):
                    ok.add(row[1])
        pandas_version = pandas_version[:7]
        try:
            os.makedirs(os.path.join("test_logs", "pandas", pandas_version))
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
            pyfile_path = os.path.join("test_pandas", downstream_test_pyfile)
            with open(os.path.join("test_logs", "pandas", pandas_version, \
                downstream_name + ".log"), mode="w") as wf:
                p = Popen(["python3", pyfile_path], stdout=wf, stderr=wf)
                try:
                    p.communicate(timeout=12600)
                except:
                    p.kill()


if __name__ == '__main__':
    main()
