import subprocess
import os
import tqdm
import sqlite3
import time


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
                p.communicate(timeout=10800)
            except:
                p.kill()


def test_code(code_path: str, log_file):
    start_time = time.time()
    p = subprocess.Popen(["python3", code_path], stdout=log_file, stderr=log_file)
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
    upstreams = ("numpy", "scipy", "astropy", "pandas", "sklearn")
    with open("exp3_config_related_downstreams.json", mode="r") as rf:
        config = json.load(rf)
    for upstream in upstreams:
        init_environment()
        versions = [sha for sha in config[upstream]]
        conn = sqlite3.connect('test_logs/databases/test_info.db')
        for version in versions:
            try:
                p = Popen("find repos -name \"pycache\" | xargs rm -r", shell=True)
                p.communicate()
            except:
                pass
            install_upstream(upstream, version)
            for item in config[upstream][version]:
                downstream = item["downstream"]
                files = item["files"]

                if downstream in ("alphalens", "joblib", "numpy_buffer", "indi", "nilearn", "astroplan", "sympy", "tables", "theano", "pymc3", "numba"):
                    continue

                if not len(files):
                    files = [""]
                
                g = test_driver_generator(downstream)
                
                log_dir = os.path.join("test_logs", upstream, version, downstream)
                try:
                    os.makedirs(log_dir)
                except:
                    pass
                total_cost = 0
                test_driver_dir = os.path.join("test_drivers", upstream, version, downstream)
                try:
                    os.makedirs(test_driver_dir)
                except:
                    pass
                if downstream in ("bottleneck", "brian2", "gammapy", "h5py", "networkx", "numba", "numexpr", "obspy", "pandas",
                                "skbio", "tables", "theano", "verde"):
                    # test all
                    test_driver_code = g.generate(files, downstream)
                    test_driver_code_path = os.path.join(test_driver_dir, downstream + ".py")
                    with open(test_driver_code_path, mode="w") as wf:
                        wf.write(test_driver_code)
                    
                    log_file = open(os.path.join(log_dir, downstream + ".log"), mode="w")
                    cost = test_code(test_driver_code_path, log_file)
                    log_file.close()
                    total_cost = cost
                    conn.execute("insert or replace into %s values (?,?,?,?,?,?)" % (upstream, ), (upstream, version, downstream, "", "", cost))
                elif downstream in ("asdf", "astroimtools", "astroplan", "astropy", "ccdproc", "photutils", "poppy", "pydl",
                "pyregion", "radio_beam", "stginga", "synphot"):
                    # test modules
                    for f in files:
                        test_driver_code = g.generate([f], downstream)
                        name = "_".join(f.split("."))
                        if not name:
                            name = downstream
                        test_driver_code_path = os.path.join(test_driver_dir, name + ".py")
                        with open(test_driver_code_path, mode="w") as wf:
                            wf.write(test_driver_code)
                        log_file = open(os.path.join(log_dir, name + ".log"), mode="w")
                        cost = test_code(test_driver_code_path, log_file)
                        log_file.close()
                        total_cost += cost
                        conn.execute("insert or replace into %s values (?,?,?,?,?,?)" % (upstream, ), (upstream, version, downstream, "", f, cost))
                elif downstream in ("numpy", "scipy", "statsmodels"):
                    # test modules
                    for f in files:
                        test_driver_code = g.generate([f], downstream)
                        name = "_".join(f.split("."))
                        if not name:
                            name = downstream
                        test_driver_code_path = os.path.join(test_driver_dir, name + ".py")
                        with open(test_driver_code_path, mode="w") as wf:
                            wf.write(test_driver_code)
                        log_file = open(os.path.join(log_dir, name + ".log"), mode="w")
                        cost = test_code(test_driver_code_path, log_file)
                        log_file.close()
                        total_cost += cost
                        conn.execute("insert or replace into %s values (?,?,?,?,?,?)" % (upstream, ), (upstream, version, downstream, "", f, cost))
                else:
                    # test files 
                    for f in files:
                        test_driver_code = g.generate([f], downstream)
                        test_driver_code_path = os.path.join(test_driver_dir, "_".join(f.split(".")) + ".py")
                        with open(test_driver_code_path, mode="w") as wf:
                            wf.write(test_driver_code)
                        log_file = open(os.path.join(log_dir, "_".join(f.split(".")) + ".log"), mode="w")
                        cost = test_code(test_driver_code_path, log_file)
                        log_file.close()
                        total_cost += cost
                        conn.execute("insert or replace into %s values (?,?,?,?,?,?)" % (upstream, ), (upstream, version, downstream, f, "", cost))
                conn.execute("insert or replace into %s values (?,?,?,?,?,?)" % (upstream, ), (upstream, version, downstream, "", "", total_cost))
                conn.commit()
        conn.close()


if __name__ == "__main__":
    main()
