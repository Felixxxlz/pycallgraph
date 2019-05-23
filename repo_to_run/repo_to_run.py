import os
import csv


def main():
    upstream = "sklearn"
    results_dir = "results"
    commits = []
    with open(upstream + ".csv") as rf:
        reader = csv.reader(rf)
        for row in reader:
            if int(row[1]) >= 10:
                commits.append(row[0])
    print(commits)
    print(len(commits))


if __name__ == "__main__":
    main()
