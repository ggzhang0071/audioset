import pandas as pd
import shutil,os 

def read_wav_info(wav_file):
    wav_info=pd.read_csv(wav_file,delimiter=" ",comment="#")
    file_dict=dict()
    for _, row in wav_info.iterrows():
        file_name=row[0][:-1]+"_"+row[1][:-1]+".wav.gz"
        file_dict.update({file_name:row})
    return file_dict

def segment_audioset(baltrain_dict,eval_dict,unbal_train_dict):
    train_list,eval_list,unbal_train_list=list(),list(),list()
    wav_dir="/mnt/work/git/audioset/download"
    for wav in os.listdir(wav_dir):
        if wav.endswith(".wav.gz"):
            if wav in baltrain_dict.keys():
                print("move file {} to {}".format(wav,bal_train_dict[wav]))
                shutil.move(os.path.join(wav_dir,wav),'/mnt/work/git/datasets/audioset/bal_train/'+wav)
                train_list.append(bal_train_dict[wav])
                bal_train_dict.pop(wav)
            elif wav in eval_dict.keys():
                print("move file {} to {}".format(wav,eval_dict[wav]))
                shutil.move(os.path.join(wav_dir,wav),'/mnt/work/git/datasets/audioset/eval/'+wav)
                eval_list.append(eval_dict[wav])
                eval_dict.pop(wav)
            elif wav in unbal_train_dict.keys():
                print("move file {} to {}".format(wav,unbal_train_dict[wav]))
                shutil.move(os.path.join(wav_dir,wav),'/mnt/work/git/datasets/audioset/unbal_train/'+wav)
                unbal_train_list.append(unbal_train_dict[wav])
                unbal_train_dict.pop(wav)
            else:
                print("file {} not in any dict".format(wav))
      
    # save the rest of the files
    with open(".csv","w") as f:
        for wav_info in train_list:
            f.write(wav_info[0]+"\n")
        
    with open("new_train_segments.csv","w") as f:
        for wav_info in eval_list:
            f.write(wav_info[0]+"\n")

if __name__=="__main__":
    eval_segments="/mnt/work/git/audioset/download/eval_segments.csv"
    train_segments="/mnt/work/git/audioset/download/balanced_train_segments.csv"
    unbaltrain_segments="/mnt/work/git/audioset/download/unbalanced_train_segments.csv"
    eval_wav_info=read_wav_info(eval_segments)
    baltrain_wav_info=read_wav_info(train_segments)
    unbaltrain_wav_info=read_wav_info(train_segments)
    segment_audioset(baltrain_wav_info,unbaltrain_wav_info,eval_wav_info)



    






        





