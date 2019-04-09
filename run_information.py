import os
import json


repo = "astropy"
test_dir = "test."
with open(os.path.join("callgraph", "%s_callgraph.json" % (repo, )), mode='r', encoding='utf-8') as rf:
    callgraph = json.load(rf)
s = set()
edges = 0
for caller in callgraph:
    s.add(caller)
    callees = callgraph[caller]
    for callee in callees:
        s.add(callee)
        if (caller.startswith(repo) or caller.startswith(test_dir) or caller.startswith("test_")) and callee.startswith(repo):
            edges += 1

with open(os.path.join("traces", "%s_trace.txt" % (repo, )), mode="r", encoding="utf-8") as rf:
    lines = rf.readlines()

# 1. `tests`目录下(joblib的测试目录为`test`, IPython的测试目录为testing, sympy的测试目录为runtests, patsy没有测试目录, shared_ndarray, autoptim没有.tests.)，且模块名以test_开头，项目名repo开头(xlrd这类直接在clone下来的repo中用pytest测试的，以test.开头)
# tot_testcases = len([func for func in list(s) if test_dir in func and "test_" in func and func.startswith(repo)])
# tot_testcases = len([func for func in list(s) if "test_" in func and func.startswith(repo)])
# 用来统计放在tests放在src外面的测试用例数
tot_testcases = len([func for func in list(s) if (func.startswith(test_dir) or func.startswith("test_")) and not func.startswith(repo)])
# tot_testcases = 0
# for line in lines:
#     line = line.strip().split("$")
#     if line[0].startswith(repo+".") and ".tests." in line[0] and "test_" in line[0] and line[1].startswith(repo+"."):
    # sympy
    # if line[0].startswith(repo+".") and ".runtests." in line[0] and "test_" in line[0] or \
    #     "test_" in line[0] and line[1].startswith(repo+"."):
        # tot_testcases += 1
print(tot_testcases)
# 2. 节点个数直接统计以项目名repo开头的函数/方法个数
print(len([si for si in s if si.startswith(repo) or si.startswith(test_dir) or si.startswith("test_")]))
# 3. 边数直接统计调用图中调用者和被调用者都以repo开头的调用个数
print(edges)
