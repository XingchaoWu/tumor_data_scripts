# _*_ coding=utf-8 _*_
# author: xingchaowu
# date: 2020-09-24


import xlrd
import csv
import pandas as pd
import threading


# 1.1 generate the dictionary contain Sample_Name and Mutation_Info
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
    return mutation_dict


# 2.1 extract info of SNV and Indel which from hotspot and discard
def Extract_SnvAndIndel_Info(work_path,data_xlxs_name,mutation_dict):
    data_xlxs = xlrd.open_workbook(r"%s\%s.xlsx"%(work_path,data_xlxs_name),"r")
    sheet_name_list = ["SNVIndelHotSpot", "SNVIndelDiscard"]
    with open(r"%s\%s_SNVIndel_filter.csv"%(work_path,data_xlxs_name),"a+",newline="")as outfile:
        header = ["#sample_name","Follow_Cell","Site_Type","Depth","frequency","CDS_change","Var_ss","Var_Ds"]
        write_csv = csv.DictWriter(outfile,fieldnames=header)
        write_csv.writeheader()
        for sn_l in sheet_name_list:
            data_sheet = data_xlxs.sheet_by_name("{}".format(sn_l))
            n_rows = data_sheet.nrows
            for n in range(1,n_rows):
                for k,v in mutation_dict.items():
                    if k in data_sheet.cell(n,0).value and data_sheet.cell(n,0).value[:(len(k)+1)] != k and data_sheet.cell(n,14).value in v:
                        write_csv.writerow({"#sample_name":data_sheet.cell(n,0).value,
                                            "Follow_Cell":data_sheet.cell(n,2).value[:-2],
                                            "Site_Type":sn_l[8:],
                                            "Depth":int(data_sheet.cell(n,9).value),
                                            "frequency":float(data_sheet.cell(n,10).value),
                                            "CDS_change":data_sheet.cell(n,14).value,
                                            "Var_ss":int(data_sheet.cell(n,28).value),
                                            "Var_Ds":int(data_sheet.cell(n,31).value)})

        # 2.2 extract negative sample lib number and run number
        negative_data_sheet = data_xlxs.sheet_by_name("DataProduction")
        n_negative_rows = negative_data_sheet.nrows
        for m in range(1,n_negative_rows):
            for k, v in mutation_dict.items():
                if "-" in v:
                    if k in negative_data_sheet.cell(m, 0).value:
                        write_csv.writerow({"#sample_name": negative_data_sheet.cell(m, 0).value,
                                            "Follow_Cell": negative_data_sheet.cell(m, 2).value[:-2],
                                            "Site_Type": "DataProduction",
                                            "Depth": "-",
                                            "frequency": "-",
                                            "CDS_change": "-",
                                            "Var_ss": "-",
                                            "Var_Ds": "-"})

# 3.1 extract cnv info from the result of analysis in the sheetname by CNV
def Extract_CNV_Info(work_path,data_xlxs_name,mutation_dict):
    data_xlxs = xlrd.open_workbook(r"%s\%s.xlsx" % (work_path, data_xlxs_name), "r")
    data_sheet = data_xlxs.sheet_by_name("CNV")
    n_rows = data_sheet.nrows
    with open(r"%s\%s_CNV_filter.csv" % (work_path, data_xlxs_name), "w", newline="")as outfile:
        header = ["#sample_name", "Follow_Cell","Gene", "CopyNum"]
        write_csv = csv.DictWriter(outfile, fieldnames=header)
        write_csv.writeheader()
        for n in range(1, n_rows):
            for k,v in mutation_dict.items():
                if k in data_sheet.cell(n,0).value and v[0] == "CNV":
                    write_csv.writerow({"#sample_name": data_sheet.cell(n, 0).value,
                                        "Follow_Cell": data_sheet.cell(n, 2).value[:-2],
                                        "Gene": data_sheet.cell(n,3).value,
                                        "CopyNum": data_sheet.cell(n, 4).value,})
# 4.1 formate csv transform xlsx
def csv2xls(sample_type,work_path,data_xlxs_name):
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
    # names = ["20200519_SHXW_M009874_ADXLC10_v3.0.0","20200522_SHXW_M009914_ADXLC10_v3.0.0","20200522_SHXW_M009917_ADXLC10_v3.0.0","20200524_SHXW_M009936_ADXLC10_v3.0.0","20200514_SHXW_M009837_ADXLC10_v3.0.0"]
    # for i in names:
    data_xlxs_name = input("Input the name of the source file:")
        # data_xlxs_name = i
    extract_snv_job = threading.Thread(target=Extract_SnvAndIndel_Info,args=(work_path,data_xlxs_name,mutation_dict))
    extract_cnv_job = threading.Thread(target=Extract_CNV_Info,args=(work_path,data_xlxs_name,mutation_dict))
    if sample_type == "tissue":
        extract_snv_job.start()
        extract_cnv_job.start()
        extract_snv_job.join()
        extract_cnv_job.join()
    else:
        Extract_SnvAndIndel_Info(work_path, data_xlxs_name, mutation_dict)
    csv2xls(sample_type,work_path, data_xlxs_name)