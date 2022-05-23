from multiprocessing import Pool, cpu_count
import numpy as np
import pandas as pd 
import os

# 
def split_chunks(file_name):
    wav_name=os.path.splitext(file_name)[0]
    wav_info=pd.read_csv(file_name,header=None,sep=" ",comment="#", engine='python')
    wav_chunks=np.array_split(wav_info,cpu_count())
    split_file_list=[]
    for i in range(cpu_count()):
        split_file_name="{}_{}.csv".format(wav_name,i)
        wav_chunks[i].to_csv(split_file_name,float_format=int,header=None,sep=" ",index=None)
        split_file_list.append(split_file_name)
    return split_file_list

def func(chunk_file_name):
    os.system("cat {} | ./download.sh".format(chunk_file_name))

# split data 

if __name__=="__main__":
    split_file_list=split_chunks("/mnt/work/git/audioset/download/eval_segments.csv")
    with Pool(cpu_count()) as p:
        p.map(func,split_file_list)
    os.system("rm eval_segments_*.csv")
    print("download finished {}".format("eval_segments.csv"))


