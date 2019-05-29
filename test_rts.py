import subprocess
import os
import tqdm
import sqlite3
import time


def install_upstream(upstream, sha):
    if upstream == "sklearn":
        upstream = "scikit-learn"
    os.chdir(os.path.join("repos", upstream))
    p = subprocess.Popen(["git", "checkout", "master"])
    p.communicate()
    p = subprocess.Popen(["git", "checkout", sha])
    p.communicate()
    p = subprocess.Popen("sudo -S -H pip3 install . --no-cache-dir", shell=True, stdin=subprocess.PIPE)
    p.communicate(bytes("Ly941122" + "\n", encoding="utf-8"))
    os.chdir(os.path.join("..", ".."))


def run_regression(upstream, sha):
    # install environment
    install_upstream(upstream, sha)

    # clean cache
    try:
        p = subprocess.Popen(' '.join(["find", "repos", "-name", "\"__pycache__\"", "|", "xargs", "rm", "-r"]), shell=True)
        p.communicate()
    except:
        pass

    # run testsuits
    try:
        os.makedirs(os.path.join("test_logs", upstream, sha))
    except:
        pass
    test_drivers_dir = os.path.join("test_drivers", upstream, sha)
    downstream_test_drivers = os.listdir(test_drivers_dir)
    for downstream_test_driver in tqdm.tqdm(downstream_test_drivers):
        downstream = "_".join(downstream_test_driver.split(".")[0].split("_")[1:])
        pyfile_path = os.path.join(test_drivers_dir, downstream_test_driver)
        with open(os.path.join("test_logs", upstream, sha, downstream + ".log"), mode="w") as wf:
            p = subprocess.Popen(["python3", pyfile_path], stdout=wf, stderr=wf)
            try:
                p.communicate(timeout=12600)
            except:
                p.kill()


def read_data():
    with open("data.txt") as rf:
        lines = rf.readlines()
    lines = [line.strip().split() for line in lines]
    ret = []
    for line in lines:
        tmp = line[:3]
        tmp.append(tuple(line[3:]))
        ret.append(tuple(tmp))
    return ret


def test_code(code: str, log_file):
    start_time = time.time()
    with open("tmp.py", "w") as wf:
        wf.write(code)
    p = subprocess.Popen(["python3", "tmp.py"], stdout=log_file, stderr=log_file)
    try:
        p.communicate(timeout=12600)
    except:
        p.kill()
    return time.time() - start_time


def test_driver_generator(downstream):
    if downstream in ("astropy", "matplotlib", "numpy", "pandas", "scipy", "tables", "theano",
                                "sympy", "networkx", "obspy", "statsmodels", "gammapy", "h5py", "skbio",
                                "ccdproc", "numexpr", "asdf", "bottleneck", "photutils", "poppy", "pyregion",
                                "astroplan", "brian2", "radio_beam", "numba", "verde", "astroimtools", 
                                "stginga", "synphot", "pydl"):
        g = __import__("test_driver_generator." + downstream, fromlist=True)
    elif downstream in ("joblib", "sklearn", "dask", "nilearn", "seaborn", "specutils", "xarray",
                        "naima", "patsy", "pyamg", "randomgen", "shared_ndarray", "mahotas", "nrrd",
                        "sparse", "alphalens", "pyjet", "numbagg", "pymc3", "cvxpy", "aplpy", "deap",
                        "mpmath", "oct2py", "atpy", "gwcs", "starfish", "nptdms", "iexfinance",
                        "plydata", "ibis", "imexam", "astroscrappy", "astroML", "astroquery",
                        "baseband", "ginga", "halotools", "poliastro", "stingray", "gala",
                        "astropy_healpix", "dust_extinction", "dipy", "xcessiv", "pystruct",
                        "hdbscan", "gplearn"):
        g = __import__("test_driver_generator.generator0", fromlist=True)
    elif downstream in ("astropy_helpers", "utide", "pyik", "npstreams", "pyxrd", "pvmismatch", "spampy",
                        "pyrr", "hienoi", "molml", "oommftools", "nnlib", "dicom_numpy", "kravatte",
                        "geometer", "slugnet", "zappy", "gfmm", "json_tricks", "pdepy", "tidynamics",
                        "texpy", "numpy_buffer", "feets", "psopy", "randnla", "indi", "pytablewriter",
                        "prince", "coinsta", "kodiak", "phildb", "datacompy", "espandas", "deepgraph",
                        "lens", "validada", "partridge", "finta", "subsync", "tgan", "auto_ml", "skopt",
                        "scikitplot", "onnxmltools", "seqlearn", "kmodes", "spherecluster", "skpro", 
                        "profanity_check", "pailab", "chainer_sklearn", "sklearn_evaluation", "sklearn2", 
                        "sklearn_lvq"):
        g = __import__("test_driver_generator.generator1", fromlist=True)
    return g


def main():
    data = read_data()
    conn = sqlite3.connect('test_info.db')
    pre_upstream = ''
    pre_sha = ''
    for upstream, sha, downstream, files in tqdm.tqdm(data):

        if downstream in ("alphalens", "joblib", "numpy_buffer", "indi", "nilearn", "astroplan", "sympy", "tables", "theano", "pymc3", "numba"):
            continue

        if not len(files):
            files = [""]

        # install environment
        if pre_upstream != upstream or pre_sha != sha:
            pre_upstream = upstream
            pre_sha = sha
            install_upstream(upstream, sha)
        
        g = test_driver_generator(downstream)
        
        log_dir = os.path.join("test_logs", upstream, sha, downstream)
        try:
            os.makedirs(log_dir)
        except:
            pass
        total_cost = 0
        if downstream in ("bottleneck", "brian2", "gammapy", "h5py", "networkx", "numba", "numexpr", "obspy", "pandas",
                        "skbio", "tables", "theano", "verde"):
            # test all
            test_driver_code = g.generate(files, downstream)
            log_file = open(os.path.join(log_dir, downstream + ".log"), mode="w")
            cost = test_code(test_driver_code, log_file)
            log_file.close()
            total_cost = cost
            conn.execute("insert or replace into %s values (?,?,?,?,?,?)" % (upstream, ), (upstream, sha, downstream, "", "", cost))
        elif downstream in ("asdf", "astroimtools", "astroplan", "astropy", "ccdproc", "photutils", "poppy", "pydl",
        "pyregion", "radio_beam", "stginga", "synphot"):
            # test modules
            for f in files:
                test_driver_code = g.generate([f], downstream)
                name = "_".join(f.split("."))
                if not name:
                    name = downstream
                log_file = open(os.path.join(log_dir, name + ".log"), mode="w")
                cost = test_code(test_driver_code, log_file)
                log_file.close()
                total_cost += cost
                conn.execute("insert or replace into %s values (?,?,?,?,?,?)" % (upstream, ), (upstream, sha, downstream, "", f, cost))
        elif downstream in ("numpy", "scipy", "statsmodels"):
            # test modules
            for f in files:
                test_driver_code = g.generate([f], downstream)
                name = "_".join(f.split("."))
                if not name:
                    name = downstream
                log_file = open(os.path.join(log_dir, name + ".log"), mode="w")
                cost = test_code(test_driver_code, log_file)
                log_file.close()
                total_cost += cost
                conn.execute("insert or replace into %s values (?,?,?,?,?,?)" % (upstream, ), (upstream, sha, downstream, "", f, cost))
        else:
            # test files 
            for f in files:
                test_driver_code = g.generate([f], downstream)
                log_file = open(os.path.join(log_dir, "_".join(f.split(".")) + ".log"), mode="w")
                cost = test_code(test_driver_code, log_file)
                log_file.close()
                total_cost += cost
                conn.execute("insert or replace into %s values (?,?,?,?,?,?)" % (upstream, ), (upstream, sha, downstream, f, "", cost))
        conn.execute("insert or replace into %s values (?,?,?,?,?,?)" % (upstream, ), (upstream, sha, downstream, "", "", total_cost))
        conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
