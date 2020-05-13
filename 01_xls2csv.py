# _*_ conding=utf-8 _*_
# author: xingchao wu
# date: 20200319

import xlrd
import csv

# 原始样本信息整理
def xls2csv(work_path,in_sample_info,out_sample_info):
    data = xlrd.open_workbook(r"%s\%s.xlsx"%(work_path,in_sample_info))
    table = data.sheet_by_index(0)
    n_rows = table.nrows
    with open(r"%s\%s.csv"%(work_path,out_sample_info),"w",newline="") as outfile:  # python3
    # with open("%s/%s.csv"%(cur_path,args.csv_file),"w",encoding="UTF-8") as outfile:  # python2
        header = ["#Sample_Num","Accept_Date","Gender","Age","Smoking_Hist","Pathological_diagnosis","Sample_Type","Pannel_type"]
        out_csv = csv.DictWriter(outfile,fieldnames=header)
        out_csv.writeheader()
        for i in range(1,n_rows):
            out_csv.writerow({"#Sample_Num":table.cell(i,2).value,
                               "Accept_Date":table.cell(i,4).value,
                               "Gender":table.cell(i,8).value,
                               "Age":table.cell(i,9).value,
                               "Smoking_Hist":table.cell(i,10).value,
                               "Pathological_diagnosis":table.cell(i,12).value,
                               "Sample_Type":table.cell(i,15).value.replace(",","_"),
                               "Pannel_type":table.cell(i,19).value})
    outfile.close()


if __name__ == '__main__':
    work_path = input("输入原始样本信息文件的绝对路径：")
    in_sample_info = input("请输入原始样本信息文件：")
    out_sample_info = input("请输入保存样本信息文件：")
    xls2csv(work_path,in_sample_info,out_sample_info)
    # xls2csv()
