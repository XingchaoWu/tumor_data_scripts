# _*_coding:utf-8_*_
# author: Xingchao Wu
# date: 2020-06-13

"""
根据原始样本对应的突变信息从数据分析文件中提取检出结果，如：
原始样本LC-BR3对应的突变信息如下：
NM_000245.2:exon14_intron14:c.3028_3028+16del17:p.?
NM_005228.3:exon20:c.2290_2291ins12:p.A763_Y764insFQEA
NM_000245.2:intron13:c.2888-41_2888-2delTAGCCGTCTTTAACAAGCTCTTTCTTTCTCTCTGTTTTAA:p.?
即：需要从分析文件中提取该突变信息对应的sample_name,Depth,frequency,CDS_change,Var_ss对应的文件内index(0,9,10,14,28)
"""

import xlrd
import csv
import pandas as pd

# 根据样本对应突变list生成样本和突变的字典
def generate_sample_dict(work_path,mutation_dict):
    sample_type = input("请输入要提取信息样本类型(tissue or plasma):")  # 修改于2020-09-07
    list_file = open(r"%s\%s.txt"%(work_path,sample_type),"r")
    for line in list_file:
        s_key = line.strip().split("\t")[0]
        s_value = line.strip().split("\t")[1]
        if s_value is not '':
            if s_key in mutation_dict:
                mutation_dict.get(s_key).append(s_value)
            else:
                mutation_dict.setdefault(s_key,[]).append(s_value)
    print(mutation_dict)
    return mutation_dict

def extract_info(work_path,data_xlxs_name,mutation_dict):
    data_xlxs = xlrd.open_workbook(r"%s\%s.xlsx"%(work_path,data_xlxs_name),"r")
    data_sheet = data_xlxs.sheet_by_name("SNVIndelHotSpot")
    n_rows = data_sheet.nrows
    # print(data_sheet.ncols)
    # 遍历源数据文件和样本list信息提取数据
    with open(r"%s\%s_filter_data.csv"%(work_path,data_xlxs_name),"w",newline="")as outfile:
        header = ["#sample_name","Depth","frequency","CDS_change","Var_ss","Var_Ds"]
        # header = ["#sample_name","Depth","frequency","CDS_change","Var_Ds"]
        write_csv = csv.DictWriter(outfile,fieldnames=header)
        write_csv.writeheader()
        for n in range(1,n_rows):
            for k,v in mutation_dict.items():
                if k in data_sheet.cell(n,0).value and data_sheet.cell(n,14).value in v:
                    write_csv.writerow({"#sample_name":data_sheet.cell(n,0).value,
                                        "Depth":data_sheet.cell(n,9).value,
                                        "frequency":data_sheet.cell(n,10).value,
                                        "CDS_change":data_sheet.cell(n,14).value,
                                        # "Var_ss":data_sheet.cell(n,21).value})
                                        "Var_ss":data_sheet.cell(n,28).value,
                                        "Var_Ds":data_sheet.cell(n,31).value})
def csv2xls(work_path,data_xlxs_name):
    csv_file = pd.read_csv(r"%s\%s_filter_data.csv"%(work_path,data_xlxs_name),encoding="utf-8",index_col=0,engine='python')
    csv_file.to_excel(r"%s\%s_filter_data.xlsx"%(work_path,data_xlxs_name),sheet_name="filter_data")


if __name__ == '__main__':
    mutation_dict = {}
    work_path = input("输入list及源分析文件路径: ")
    generate_sample_dict(work_path,mutation_dict)
    data_xlxs_name = input("输入需要提取数据的源文件名称：")
    extract_info(work_path,data_xlxs_name,mutation_dict)
    csv2xls(work_path, data_xlxs_name)
