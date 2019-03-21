import os
import json


repo = "numexpr"
with open(os.path.join("callgraph", "%s_callgraph.json" % (repo, )), mode='r', encoding='utf-8') as rf:
    callgraph = json.load(rf)
s = set()
edges = 0
for caller in callgraph:
    s.add(caller)
    callees = callgraph[caller]
    for callee in callees:
        s.add(callee)
        if caller.startswith(repo) and callee.startswith(repo):
            edges += 1

with open(os.path.join("traces", "%s_trace.txt" % (repo, )), mode="r", encoding="utf-8") as rf:
    lines = rf.readlines()

# 1. 测试用例的caller需要在trace中统计（否则把对同个API的多个测试用例都去重了），`tests`目录下(joblib的测试目录为`test`, IPython的测试目录为testing, sympy的测试目录为runtests)，且模块名以test_开头，项目名repo开头
tot_testcases = len([func for func in list(s) if ".tests." in func and "test_" in func and func.startswith(repo)])
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
print(len([si for si in s if si.startswith(repo)]))
# 3. 边数直接统计调用图中调用者和被调用者都以repo开头的调用个数
print(edges)
