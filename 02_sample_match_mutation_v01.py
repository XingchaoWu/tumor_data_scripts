# _*_ conding=utf-8 _*_
# author: xingchaowu
# date：2020-03-23

import csv

# 样本信息表  'Sample_Num': ['Accept_Date', 'Gender', 'Age', 'Smoking_Hist', 'Pathological_diagnosis', 'Sample_Type', 'Pannel_type']
def sample_match_mutation_info(work_path,sample_info,mutation_info,outfile_name):
    sample_dict = {}
    with open(r"%s\%s.csv"%(work_path,sample_info),"r") as sampleinfo:   # 整理后的样本信息表
        for line in sampleinfo:
            sample_dict[line.strip().split(",")[0]] = [line.strip().split(",")[1],line.strip().split(",")[2],
                                                       line.strip().split(",")[3],line.strip().split(",")[4],
                                                       line.strip().split(",")[5],line.strip().split(",")[6],
                                                       line.strip().split(",")[7]]
    sampleinfo.close()

    # 根据突变检出写入新的汇总表
    mutation_sample_list = []
    with open(r"%s\%s.csv"%(work_path,outfile_name),"w",newline="") as outfile:  # 生成含样本诊断信息的突变汇总表
        header = ["#sample_num","lib_num","project","mutation_gene","mutation_site","mutation_frequency","Gender","Age","Smoking_Hist","Pathological_diagnosis"]
        out_csv = csv.DictWriter(outfile,fieldnames=header)
        out_csv.writeheader()
        with open(r"%s\%s.csv"%(work_path,mutation_info),"r") as mutationinfo:
            for line1 in mutationinfo:
                for info_sample in sample_dict.keys():
                    if line1.strip().split(",")[0] == info_sample:
                        mutation_sample_list.append(line1.strip().split(",")[0])
                        out_csv.writerow({"#sample_num":info_sample,
                                     "lib_num":line1.strip().split(",")[1],
                                     "project":sample_dict[info_sample][6],
                                     "mutation_gene": line1.strip().split(",")[3],
                                      "mutation_site": line1.strip().split(",")[4],
                                      "mutation_frequency":line1.strip().split(",")[5],
                                      "Gender":sample_dict[info_sample][1],
                                      "Age":sample_dict[info_sample][2],
                                      "Smoking_Hist":sample_dict[info_sample][3],
                                      "Pathological_diagnosis":sample_dict[info_sample][4]})
    mutationinfo.close()
    outfile.close()
    print("突变信息汇总样本数：%s"%len(list(set(mutation_sample_list))))

if __name__ == '__main__':
    work_path = input("输入输出工作目录绝对路径：")
    sample_info = input("输入整理后的样本信息表名称：")
    mutation_info = input("输入整理后的突变信息表名称：")
    outfile_name = input("输入要保存的文件名称：")
    sample_match_mutation_info(work_path,sample_info,mutation_info,outfile_name)