# —*—coding:utf-8_*_
# author: Xingchao Wu
# date: 2020-05-04


import xlrd
import csv
import argparse,os,io
import re
def pre_prepration(cur_path,sample_list):
    # sample_list_file = open("%s/%s"%(cur_path,args.list),"r")
    sample_list_file = open("%s/list.txt"%(cur_path),"r")
    for s in sample_list_file:
        sample_list.append(s.strip())


def match_tumor_con(cur_path,sample_list):
    tumor_con_dict = {}
    # write for txt formate
    # out_txt = open(r"D:\PycharmProjects\Tumor\tumor_con.txt","w")
    out_txt = io.open("%s/tumor_con.txt"%(cur_path),"w")
    out_txt.write("SampleID\tTumor_Con\n")
    # write for csv formate
    out_csv = open("%s/tumor_con.csv"%(cur_path),"w",newline="")
    # out_csv = io.open("%s/%s.csv"%(cur_path,args.outfile),"w",encoding="utf-8")
    header = ["SampleID","Tumor_Con"]
    csv_writer = csv.DictWriter(out_csv,fieldnames=header)
    csv_writer.writeheader()
    # read xlsx file
    xls_file = xlrd.open_workbook("%s/tumor_concentration_for_NGS.xlsx"%(cur_path),"r")
    for i in range(2):
        data = xls_file.sheet_by_index(i)
        n_cols = data.ncols
        n_rows = data.nrows
        for m in range(1,n_rows):
            c_type = data.cell(m,0).ctype
            if c_type == 2 and data.cell(m,0).value % 1 == 0:
                tumor_con_dict[int(data.cell(m,0).value)] = "".join(re.findall(r"\d+\.*\d*%$",str(data.cell(m,4).value)))
                if data.cell(m,4).value == "":
                    out_txt.write(str(int(data.cell(m,0).value)) + "\t" + "-"  + "\n")
                    csv_writer.writerow({"SampleID":int(data.cell(m,0).value),"Tumor_Con":"-"})
                else:
                    out_txt.write(str(int(data.cell(m,0).value)) + "\t" + str(data.cell(m,4).value) + "\n")
                    csv_writer.writerow({"SampleID":data.cell(m,0).value,"Tumor_Con":"".join(re.findall(r"\d+\.*\d*%$",str(data.cell(m,4).value)))})
            else:
                # 正则匹配数字
                tumor_con_dict[data.cell(m, 0).value] = "".join(re.findall(r"\d+\.*\d*%$",str(data.cell(m,4).value)))
                if data.cell(m, 4).value == "":
                    out_txt.write(str(data.cell(m, 0).value) + "\t" + "-" + "\n")
                    csv_writer.writerow({"SampleID": data.cell(m, 0).value, "Tumor_Con": "-"})
                else:
                    out_txt.write(str(data.cell(m, 0).value) + "\t" + str(data.cell(m, 4).value) + "\n")
                    csv_writer.writerow({"SampleID": data.cell(m, 0).value, "Tumor_Con": "".join(re.findall(r"\d+\.*\d*%$",str(data.cell(m,4).value)))})
    print(tumor_con_dict)

    with open("%s/tumor_con_match.csv"%(cur_path),"w",newline="") as match_file:
        # match_file.write("Lib_ID\tTumor_Con\n")
        header1 = ["Lib_ID","Tumor_Con"]
        writer = csv.DictWriter(match_file,fieldnames=header1)
        writer.writeheader()
        for sample in list(set(sample_list)):
            if sample[:9] in tumor_con_dict:
                writer.writerow({"Lib_ID":sample,"Tumor_Con":tumor_con_dict[sample[:9]]})
            else:
                writer.writerow({"Lib_ID": sample, "Tumor_Con":"-"})
    match_file.close()


if __name__ == '__main__':
    sample_list = []
    cur_path = r"E:\厦维生物\99_Sample_Datainfo"
    pre_prepration(cur_path,sample_list)
    match_tumor_con(cur_path,sample_list)