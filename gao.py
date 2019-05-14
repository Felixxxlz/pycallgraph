import os
import csv


def main():
    ups = os.listdir("results")
    for up in ups:
        repo_results_path = os.path.join("results", up)
        commit_results = os.listdir(repo_results_path)
        with open(os.path.join("results", up + ".csv"), mode="w") as wf:
            writer = csv.writer(wf)
            for commit_result in commit_results:
                commit_result_csv = os.path.join(repo_results_path, commit_result)
                with open(commit_result_csv, mode="r", encoding="gbk") as rf:
                    reader = csv.reader(rf)
                    next(reader)
                    cnt = 0
                    for row in reader:
                        if int(row[4]):
                            cnt += 1
                writer.writerow((commit_result.split(".")[0], cnt))


if __name__ == "__main__":
    main()
