# _*_ coding=utf-8 _*_
# author: xingchaowu


import xlrd
import csv
import pandas as pd

# read run info in txt
run_list = []
run_txt = open(r"E:\厦维生物\samplesheet\数据拆分\run_info.txt")
for run_line in run_txt:
    run_list.append(run_line.strip())
print(run_list)
print(len(run_list))

# match info with run info in totalinfo
data = xlrd.open_workbook(r"E:\厦维生物\samplesheet\数据拆分\tmp\10基因性能验证-上机数据汇总-重拆-2020.09.18.xlsx")
table = data.sheet_by_index(0)
n_rows = table.nrows
for run in run_list:
    save_file = open(r"E:\厦维生物\samplesheet\数据拆分\tmp\%s.csv"%run,"w",newline="")
    header = ["SampleName","LibName","Confidence","CheckName","OriName","OriLab","Primer","I7","I5","verfication","RUN_Info","SeqMechine"]
    write_csv = csv.DictWriter(save_file,fieldnames=header)
    write_csv.writeheader()
    for i in range(1,n_rows):
        if run == table.cell(i,10).value:
            write_csv.writerow({"SampleName":table.cell(i,0).value,
                                "LibName":table.cell(i,1).value,
                                "Confidence":table.cell(i,2).value,
                                "CheckName":table.cell(i,3).value,
                                "OriName":table.cell(i,4).value,
                                "OriLab":table.cell(i,5).value,
                                "Primer":table.cell(i,6).value,
                                "I7":table.cell(i,7).value,
                                "I5":table.cell(i,8).value,
                                "verfication":table.cell(i,9).value,
                                "RUN_Info":table.cell(i,10).value,
                                "SeqMechine":table.cell(i,11).value})
    save_file.close()

with open(r"E:\厦维生物\samplesheet\数据拆分\tmp\xlsx\run.txt","w+") as tmp:
    for r in run_list:
        df = pd.read_csv(r"E:\厦维生物\samplesheet\数据拆分\tmp\%s.csv"%r,index_col=0, engine="python")
        print("%s:%s"%(r,len(df)))
        df.to_excel(r"E:\厦维生物\samplesheet\数据拆分\tmp\xlsx\%s_%s.xlsx"%(r,len(df)),sheet_name="Sheet1")
        tmp.write("%s_%s\n"%(r,len(df)))



