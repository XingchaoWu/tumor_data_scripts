# _*_ coding=utf-8 _*_
# author: xingchaowu
# date: 2020-03-27

import csv

def generate_stat(file_path,in_file):
    # 统计总的样本数
    total_sample = []
    with open(r"%s\18_19_mutation_total.csv"%"\\".join(file_path.split("\\")[:-1]),"r") as infile: # 总的样本文件
        for info in infile:
            if not info.startswith("#"):
                total_sample.append(info.strip().split(",")[0])
    # print("整理后有突变信息的样本数：%s"%len(list(set(total_sample))))

    # 按照突变位点信息整理数据
    # step1:生成突变类型列表
    mut_type_file = open(r"%s\%s_type.txt"%(file_path,in_file),"w")
    mut_type = []  # 突变类型列表
    sample_dict = {}  # 样本与突变类型对应的字典
    mut_match_sample_dict = {}  # 汇总突变位点对应的所有样本数

    with open(r"%s\%s.txt"%(file_path,in_file),"r") as infile1:  # 读取筛选后的样本信息
        for info1 in infile1:
            if not info1.startswith("#"):
                mut_type.append(info1.strip().split("\t")[4])
                sample_dict[info1.strip().split("\t")[0]] = info1.strip().split("\t")[4]
    for info_type in list(set(mut_type)):
        mut_match_sample_dict[info_type] = []
        mut_type_file.write(info_type+"\n")
        # step2:根据突变类型生成统计文件
        for k,v in sample_dict.items():
            if info_type == v:
                mut_match_sample_dict[info_type].append(k)

    # step3:将结果写入统计的文件中
    with open(r"%s\%s_MutationType_Frequency_SampleName_stat.txt"%(file_path,in_file),"w") as outfile:
        outfile.write("#mutation_type\tsample_num\tFrequency(%)\tsample_name\n")
        for k,v in mut_match_sample_dict.items():
            outfile.write(k+"\t"+str(len(v))+"\t"+str("%.4f"%float(len(v)/len(list(set(total_sample)))*100))+"\t"+",".join(v)+"\n")
    with open(r"%s\%s_MutationType_Frequency_SampleName_stat.csv"%(file_path,in_file),"w",newline="") as outcsv:
        header = ["#mutation_type","sample_num","Frequency(%)","sample_name"]
        write_csv = csv.DictWriter(outcsv, fieldnames=header)
        write_csv.writeheader()
        for k,v in mut_match_sample_dict.items():
            write_csv.writerow({"#mutation_type":k,"sample_num":str(len(v)),"Frequency(%)":str("%.4f"%float(len(v)/len(list(set(total_sample)))*100)),
                                    "sample_name":",".join(v)+"\n"})

if __name__ == '__main__':
    file_path =input("输入工作目录绝对路径：")   # "E:\厦维生物\99_Sample_Datainfo"
    in_file = input("输入需要统计突变类型的文件名称：")  # EGFR_ex19_mutation_del
    generate_stat(file_path,in_file)