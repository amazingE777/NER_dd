"""
用于语料库的处理
1. 全部处理成小于max_seq_length的序列，这样可以避免解码出现不合法的数据或者在最后算结果的时候出现out of range 的错误。
"""
def deal_data(files, max_seq_length):
    for file in files:
        sentence, cnt, context, num, error_con, tag = [], 0, [], 0, [], "O"
        with open(file, "r") as rf:
            for line in rf.readlines():
                cnt += 1
                sentence.append(line)
                #if cnt > 80 and line[0] in ['。', '！', '？', '，', '；', ','] and tag == "O":
                if cnt > 80 and line[0] in ['。', '！', '？', '，', '；', ','] and ( len(line)==4 or line[2] == "B"):
                    sentence.append("\n")
                    context.extend(sentence)
                    if cnt > 200:
                        num += 1
                    sentence, cnt = [], 0
                if len(line) == 4:
                    tag = line[0]
                elif len(line) == 7:
                    tag = line[2]
                else:
                    tag = "O"
        
        with open(file+".bak", "w") as wf:
            wf.writelines(context)
        with open("./NERdata/error.txt", "a") as af:
            af.writelines(error_con)
        print(file, num)
                    
files = ['./NERdata/train.txt', './NERdata/dev.txt', './NERdata/test.txt']
max_seq_length = 126
deal_data(files, max_seq_length)

