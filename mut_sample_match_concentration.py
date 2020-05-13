# _*_ coding=utf-8 _*_
# author: xingchaowu
# date: 2020-03-27

import xlrd
import csv
import os

import pandas as pd

def match_sample_con(file_path,work_path,file_list):
    # step1: 读取excel 文件
    for file in file_list:
        if os.path.exists(r"%s\%s"%(file_path,file)) == True:
            xl = pd.ExcelFile(r"%s\%s"%(file_path,file))
            sheet_name = xl.sheet_names
            for name in sheet_name:
                if "打断" in name and "非打断" not in name:
                    index = sheet_name.index(name)
                    print("tissue:%s"%file)
                    data = xlrd.open_workbook(r"%s\%s"%(file_path,file))
                    table = data.sheet_by_index(index)
                    n_row = table.nrows
                    with open(r"%s\18and19Sample_concentration_tissue_total.txt"%(work_path),"a+") as outfile:
                        for i in range(8,n_row):
                            if table.cell(i,1).value == "":
                                pass
                            else:
                                # if "FD" in table.cell(i,1).value or "UD" in table.cell(i,1).value or "TD" in table.cell(i,1).value:
                                tmp_list = [table.cell(i,1).value,table.cell(i,2).value,table.cell(i,3).value]
                                outfile.write(table.cell(i,1).value+"\t"+str(table.cell(i,2).value)+"\t"+"100"+"\t"+str(table.cell(i, 3).value)+"\t"+"-\n")
                elif "非打断" in name:
                    index = sheet_name.index(name)
                    print("cfDNA:%s"%file)
                    data = xlrd.open_workbook(r"%s\%s" % (file_path, file))
                    # data = xlrd.open_workbook(r"E:\厦维生物\2018年文库构建表\2018年10月\Library sheet-20181022.xlsx")
                    # step2: 获取excel文件的book数
                    # step3: 获取excel文件中"打断样本"sheet内的数据
                    table = data.sheet_by_index(index)
                    # table = data.sheet_by_index(n_sheet-2)
                    n_row = table.nrows
                    with open(r"%s\18and19Sample_concentration_cfDNA_total.txt" % (work_path), "a+") as outfile:
                        for i in range(8, n_row):
                            if table.cell(i, 1).value == "":
                                pass
                            else:
                                outfile.write(table.cell(i,1).value+"\t"+str(table.cell(i,2).value)+"\t"+"50"+"\t"+str(table.cell(i, 3).value)+"\t"+"-\n")

def filter_info(work_path):
    for name in ["tissue","cfDNA"]:
        with open(r"%s\18and19Sample_concentration_%s_total.csv"%(work_path,name),"r") as infile1:
            tmp_info_dict = {}
            for line in infile1:
                tmp_info_dict[line.strip().split(",")[0]] = [line.strip().split(",")[1],line.strip().split(",")[2],line.strip().split(",")[3],line.strip().split(",")[4]]
        # with open(r"%s\18and19Sample_concentration_%s_total_filter.csv"%(work_path,name),"w",newline="") as outfile1:
        with open(r"%s\18and19Sample_concentration_total_filter.csv"%(work_path),"a+",newline="") as outfile1:
            header = ["#sample_num", "con.(ng/ul)", "total_v(ul)", "use_v(ul)", "remain_amount(ng)"]
            outcsv1 = csv.DictWriter(outfile1,fieldnames=header)
            outcsv1.writeheader()
            for k,v in tmp_info_dict.items():
                outcsv1.writerow({"#sample_num":k, "con.(ng/ul)":v[0], "total_v(ul)":v[1],
                                  "use_v(ul)":v[2], "remain_amount(ng)":v[3]})
    infile1.close()
    outfile1.close()


if __name__ == '__main__':
# file_path = input("输入文件存放位置的绝对路径：")
    file_path = "E:\厦维生物\95_CDX\样本信息\info"
    work_path = "E:\厦维生物\95_CDX\样本信息"
    file_list = []
    with open(r"%s\tmp"%file_path) as infile1:
        for i in infile1:
            file_list.append(i.strip())
    match_sample_con(file_path,work_path,file_list)
    # filter_info(work_path)

