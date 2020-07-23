# —*—coding:utf-8_*_
# author: Xingchao Wu
# date: 2020-05-04

import xlrd
import csv,re


def match_tumor_con():
    tumor_con_dict = {}
    # out_csv = open("%s/%s.csv"%(cur_path,args.outfile),"w",newline="",encoding="utf-8")
    out_csv = open(r"E:\厦维生物\99_Sample_Datainfo\tumor_con.csv","w",newline="",encoding="utf-8")
    header = ["SampleID","Tumor_Con"]
    csv_writer = csv.DictWriter(out_csv,fieldnames=header)
    csv_writer.writeheader()
    # read xlsx file
    xls_file = xlrd.open_workbook(r"E:\厦维生物\99_Sample_Datainfo\tumor_concentration_for_NGS.xlsx","r")
    for i in range(2):
        data = xls_file.sheet_by_index(i)
        # n_cols = data.ncols
        n_rows = data.nrows
        for m in range(1,n_rows):
            c_type = data.cell(m,0).ctype
            if c_type == 2 and data.cell(m,0).value % 1 == 0:
                tumor_con_dict[int(data.cell(m,0).value)] = "".join(re.findall(r"\d+\.*\d*%$",str(data.cell(m,4).value)))
                if data.cell(m,4).value == "":
                    csv_writer.writerow({"SampleID":int(data.cell(m,0).value),"Tumor_Con":"-"})
                else:
                    csv_writer.writerow({"SampleID":data.cell(m,0).value,"Tumor_Con":"".join(re.findall(r"\d+\.*\d*%$",str(data.cell(m,4).value)))})
            else:
                tumor_con_dict[data.cell(m, 0).value] = "".join(re.findall(r"\d+\.*\d*%$",str(data.cell(m,4).value)))
                if data.cell(m, 4).value == "":
                    csv_writer.writerow({"SampleID": data.cell(m, 0).value, "Tumor_Con": "-"})
                else:
                    csv_writer.writerow({"SampleID": data.cell(m, 0).value, "Tumor_Con": "".join(re.findall(r"\d+\.*\d*%$",str(data.cell(m,4).value)))})


    with open(r"E:\厦维生物\99_Sample_Datainfo\18_19_mutation_add_tumor_con.csv","w",newline="") as match_file:
        header1 = ["#sample_num","lib_num","project","mutation_gene","mutation_site","mutation_frequency","Gender","Age","Smoking_Hist","Pathological_diagnosis","Con.(ng/ul)","Tumor_Con"]
        write = csv.DictWriter(match_file,fieldnames=header1)
        write.writeheader()
        with open(r"E:\厦维生物\99_Sample_Datainfo\18and19Sample_concentration_total.csv","r") as info_file:
            for line in info_file:
                if not line.startswith("#"):
                    if line.strip().split(",")[0][:9] in tumor_con_dict and "PD" not in line.strip().split(",")[1]:
                        write.writerow({"#sample_num":line.strip().split(",")[0],
                                        "lib_num":line.strip().split(",")[1],
                                        "project":line.strip().split(",")[2],
                                        "mutation_gene":line.strip().split(",")[3],
                                        "mutation_site":line.strip().split(",")[4],
                                        "mutation_frequency":line.strip().split(",")[5],
                                        "Gender":line.strip().split(",")[6],
                                        "Age":line.strip().split(",")[7],
                                        "Smoking_Hist":line.strip().split(",")[8],
                                        "Pathological_diagnosis":line.strip().split(",")[9],
                                        "Tumor_Con":tumor_con_dict[line.strip().split(",")[0][:9]]})
                    else:
                        write.writerow({"#sample_num": line.strip().split(",")[0],
                                        "lib_num": line.strip().split(",")[1],
                                        "project": line.strip().split(",")[2],
                                        "mutation_gene": line.strip().split(",")[3],
                                        "mutation_site": line.strip().split(",")[4],
                                        "mutation_frequency": line.strip().split(",")[5],
                                        "Gender": line.strip().split(",")[6],
                                        "Age": line.strip().split(",")[7],
                                        "Smoking_Hist": line.strip().split(",")[8],
                                        "Pathological_diagnosis": line.strip().split(",")[9],
                                        "Con.(ng/ul)":line.strip().split(",")[10],
                                        "Tumor_Con": "-"})
    match_file.close()
    info_file.close()


if __name__ == '__main__':
    match_tumor_con()