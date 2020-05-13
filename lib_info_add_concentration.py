# _*_ coding=utf-8 _*_
# date 2020-04-09
# author xingchaowu
import os
import csv
import argparse

def generate_sample_con_dict(con_dict):
    # with open("%s"%args.concentration,"r") as infile1:
    with open(r"E:\厦维生物\95_CDX\样本信息\18and19Sample_concentration_total_filter.csv","r") as infile1:
        for info in infile1:
            if not info.startswith("#"):
                con_dict[info.strip().split(",")[0]] = info.strip().split(",")[1]
    infile1.close()
# def lib_add_con(cur_path,con_dict):
def lib_add_con(con_dict):
    # with open("%s/%s"%(cur_path,args.outfile),"w") as out:
    with open(r"E:\厦维生物\95_CDX\样本信息\18and19样本浓度汇总\18and19Sample_concentration_total.csv","w",newline="") as out:
        header = ["#sample_num","lib_num","project","mutation_gene","mutation_site","mutation_frequency","Gender","Age","Smoking_Hist","Pathological_diagnosis","Con.(ng/ul)"]
        new_out = csv.DictWriter(out,fieldnames=header)
        new_out.writeheader()
        # with open("%s"%args.lib_info,"r") as infile2:
        with open(r"E:\厦维生物\99_Sample_Datainfo\18_19_mutation_all.csv","r") as infile2:
            for libinfo in infile2:
                if not libinfo.startswith("#"):
                    if libinfo.strip().split(",")[1] in con_dict:
                        new_out.writerow({"#sample_num":libinfo.strip().split(",")[0],
                                         "lib_num":libinfo.strip().split(",")[1],
                                          "project":libinfo.strip().split(",")[2],
                                          "mutation_gene":libinfo.strip().split(",")[3],
                                          "mutation_site":libinfo.strip().split(",")[4],
                                          "mutation_frequency":libinfo.strip().split(",")[5],
                                          "Gender":libinfo.strip().split(",")[6],
                                          "Age":libinfo.strip().split(",")[7],
                                          "Smoking_Hist":libinfo.strip().split(",")[8],
                                          "Pathological_diagnosis":libinfo.strip().split(",")[9],
                                          "Con.(ng/ul)":con_dict[libinfo.strip().split(",")[1]]})
                    else:
                        new_out.writerow({"#sample_num": libinfo.strip().split(",")[0],
                                          "lib_num": libinfo.strip().split(",")[1],
                                          "project": libinfo.strip().split(",")[2],
                                          "mutation_gene": libinfo.strip().split(",")[3],
                                          "mutation_site": libinfo.strip().split(",")[4],
                                          "mutation_frequency": libinfo.strip().split(",")[5],
                                          "Gender": libinfo.strip().split(",")[6],
                                          "Age": libinfo.strip().split(",")[7],
                                          "Smoking_Hist": libinfo.strip().split(",")[8],
                                          "Pathological_diagnosis": libinfo.strip().split(",")[9],
                                          "Con.(ng/ul)":"-"})
    infile2.close()
    out.close()

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(usage="\npython3 path/lib_info_add_concentration.py -l [lib_info_file.csv] -c [concentration.csv] -o [outputfile]")
    # parser.add_argument("-l","--lib_info",type=str,help="The file contains a sample of all the mutation information")
    # parser.add_argument("-c","--concentration",type=str,help="The file contains a sample of concentration")
    # parser.add_argument("-o","--outfile",type=str,help="The file contains a sample of concentration")
    # args = parser.parse_args()
    con_dict = {}
    # cur_path = os.getcwd()
    cur_path = ""
    generate_sample_con_dict(con_dict)
    lib_add_con(con_dict)
