from multiprocessing import Pool, cpu_count
import numpy as np
import pandas as pd 
import os



def download_oneline(line_input):
    os.system("./download.sh {}".format(line_input))

if __name__=="__main__":
    #csv_list=["eval_segments.csv","unbalanced_train_segments.csv"]
    csv_list=["test.csv"]
    for csv_file in csv_list:
        wav_info_list=[]
        with open(csv_file,"r") as f:   
            for line in f.readlines():
                wav_info_list.append(line.strip())
        with Pool(cpu_count()) as p:
            p.map(download_oneline,wav_info_list)
