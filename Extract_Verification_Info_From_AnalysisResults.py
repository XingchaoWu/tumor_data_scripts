# _*_ coding=utf-8 _*_
# author: xingchaowu
# date: 2020-09-24


import xlrd
import csv
import pandas as pd

# generate the dictionary contain Sample_Name and Mutation_Info
def generate_sample_dict(work_path,mutation_dict,sample_type):
    list_file = open(r"%s\%s.txt"%(work_path,sample_type),"r")
    for line in list_file:
        s_key = line.strip().split("\t")[0].strip()
        s_value = line.strip().split("\t")[1].strip()
        if s_value is not '':  # merge the same sample with multiple mutation
            if s_key in mutation_dict:
                mutation_dict.get(s_key).append(s_value)
            else:
                mutation_dict.setdefault(s_key,[]).append(s_value)
    print(mutation_dict)
    return mutation_dict


# extract info of SNV and Indel which from hotspot and discard
def Extract_SnvAndIndel_Info(work_path,data_xlxs_name,mutation_dict):
    data_xlxs = xlrd.open_workbook(r"%s\%s.xlsx"%(work_path,data_xlxs_name),"r")
    sheet_name_list = ["SNVIndelHotSpot", "SNVIndelDiscard"]
    with open(r"%s\%s_SNVIndel_filter.csv"%(work_path,data_xlxs_name),"a+",newline="")as outfile:
        header = ["#sample_name","Depth","frequency","CDS_change","Var_ss","Var_Ds","Type"]
        write_csv = csv.DictWriter(outfile,fieldnames=header)
        write_csv.writeheader()
        for sn_l in sheet_name_list:
            data_sheet = data_xlxs.sheet_by_name("{}".format(sn_l))
            n_rows = data_sheet.nrows
            for n in range(1,n_rows):
                for k,v in mutation_dict.items():
                    if k in data_sheet.cell(n,0).value and data_sheet.cell(n,14).value in v:
                        write_csv.writerow({"#sample_name":data_sheet.cell(n,0).value,
                                            "Depth":data_sheet.cell(n,9).value,
                                            "frequency":data_sheet.cell(n,10).value,
                                            "CDS_change":data_sheet.cell(n,14).value,
                                            "Var_ss":data_sheet.cell(n,28).value,
                                            "Var_Ds":data_sheet.cell(n,31).value,
                                            "Type":sn_l[8:]})

# extract cnv info from the result of analysis in the sheetname by CNV
def Extract_CNV_Info(work_path,data_xlxs_name,mutation_dict):
    data_xlxs = xlrd.open_workbook(r"%s\%s.xlsx" % (work_path, data_xlxs_name), "r")
    data_sheet = data_xlxs.sheet_by_name("CNV")
    n_rows = data_sheet.nrows
    with open(r"%s\%s_CNV_filter.csv" % (work_path, data_xlxs_name), "w", newline="")as outfile:
        header = ["#sample_name", "Gene", "CopyNum"]
        write_csv = csv.DictWriter(outfile, fieldnames=header)
        write_csv.writeheader()
        for n in range(1, n_rows):
            for k,v in mutation_dict.items():
                if k in data_sheet.cell(n,0).value and v[0] == "CNV":
                    write_csv.writerow({"#sample_name": data_sheet.cell(n, 0).value,
                                        "Gene": data_sheet.cell(n,3).value,
                                        "CopyNum": data_sheet.cell(n, 4).value,})
# formate csv transform xlsx
def csv2xls(sample_type，work_path,data_xlxs_name):
    if sample_type == "tissue":
        for t in ["SNVIndel","CNV"]:
            csv_file = pd.read_csv(r"%s\%s_%s_filter.csv"%(work_path,data_xlxs_name,t),encoding="utf-8",index_col=0,engine='python')
            csv_file.to_excel(r"%s\%s_%s_filter.xlsx"%(work_path,data_xlxs_name,t),sheet_name="{}".format(t))
    else:
        csv_file = pd.read_csv(r"%s\%s_SNVIndel_filter.csv" % (work_path, data_xlxs_name), encoding="utf-8", index_col=0, engine='python')
        csv_file.to_excel(r"%s\%s_SNVIndel_filter.xlsx" % (work_path, data_xlxs_name), sheet_name="SNVIndel")


if __name__ == '__main__':
    mutation_dict = {}
    work_path = input("Input the list and source analysis file path: ")
    sample_type = input("Please input the type of sample(tissue or plasma):")
    generate_sample_dict(work_path,mutation_dict,sample_type)
    data_xlxs_name = input("Input the name of the source file:")
    if sample_type == "tissue":
        Extract_SnvAndIndel_Info(work_path,data_xlxs_name,mutation_dict)
        Extract_CNV_Info(work_path,data_xlxs_name,mutation_dict)
    else:
        Extract_SnvAndIndel_Info(work_path, data_xlxs_name, mutation_dict)
    csv2xls(sample_type,work_path, data_xlxs_name)
