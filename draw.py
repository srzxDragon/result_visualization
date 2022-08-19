from collections.abc import Collection

import pandas as pd
import matplotlib.pyplot as plt

metrics = [
    'ACCMean',
    'purityMean',
    'ARIMean',
    'AMIMean',
    'NMIMean',
    'homogeneityMean',
    'completenessMean',
    'VMean',
    'KPredNumMean'
]

metric_performance = {}
csv_file_path = "News-TS_sigma_S3_iter_15.csv"


param = "iter"
data = pd.read_csv(csv_file_path)
x_label = list(data[param])
print(x_label)


for metric in metrics:
    metric_performance[metric] = list(data[metric])

# print(metric_performance)



plt.rcParams["figure.figsize"] = [10, 10]

index = 1
for metric in metrics:
    y_label = metric_performance[metric]
    
    plt.plot(x_label, y_label, linewidth=2.5)
    for x, y in zip(x_label, y_label):
        plt.text(x, y, '%.3f' % y, ha = 'center', va = 'bottom', fontsize=10.5)
    plt.xlabel(param, fontsize = 20)
    plt.ylabel(metric, fontsize = 20)

    plt.xticks(x_label, fontsize=10)#嗯调调字体
    plt.yticks(fontsize=10)

    index += 1
    plt.savefig("{}.png".format(metric))
    plt.close()
    break


    