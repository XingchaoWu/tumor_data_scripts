# _*_ coding=utf-8 _*_
# author: xingchaowu
# date: 20200323

import csv
import re
# 生成突变类型统计文件
infile_name = input("输入统计的文件名称:")
outfile_name = input("输出统计的文件名称:")
mut_type_list = []
mut_dict = {}

with open(r"E:\厦维生物\EGFR_METEX14\EGFR_METEX14\检验所2018-2019临检样本信息汇总\EGFR_ex19del\%s.txt"%infile_name,"r") as infile:
    for info_mut_type in infile:
        mut_type_list.append(info_mut_type.strip().split("\t")[4])
        mut_dict[info_mut_type.strip().split("\t")[0]] = [info_mut_type.strip().split("\t")[1],info_mut_type.strip().split("\t")[2]
                                                          ,info_mut_type.strip().split("\t")[3],info_mut_type.strip().split("\t")[4]]
redup_mut_type_list = list(set(mut_type_list))
infile.close()
# 生成字典
mut_count_dict = {}

for mut_type in redup_mut_type_list:
    mut_count_dict[mut_type] = []
    for info_k,info_v in mut_dict.items():
        if mut_type == info_v[3]:
            mut_count_dict[mut_type].append(info_k)
print(mut_count_dict)

# *.txt文件生成
with open(r"E:\厦维生物\EGFR_METEX14\EGFR_METEX14\检验所2018-2019临检样本信息汇总\EGFR_ex19del\%s.txt"%outfile_name,"w") as outfile:
    outfile.write("mutation_type\tsample_num\tFrequency\tsample\n")
    for k,v in mut_count_dict.items():
        outfile.write(k+"\t"+str(len(v))+"\t"+str((len(v)/6207*100))+"\t"+",".join(v)+"\n")

