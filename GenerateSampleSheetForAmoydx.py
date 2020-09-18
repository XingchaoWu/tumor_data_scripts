# _*_ coding=utf-8 _*_
# author: xingchaowu

import xlrd
import datetime
import csv
from Bio.Seq import Seq



# generate run info list
def generate_run_info_list(run_list):
    txt_file = open(r"E:\厦维生物\samplesheet\数据拆分\tmp\xlsx\run.txt")
    for run in txt_file:
        run_list.append(run.strip())
    print(run_list)
    print(len(run_list))

# build index dictory
def gennerate_index(index_dict):
    index_file0 = open(r"E:\厦维生物\samplesheet\Index_I7.txt","r")
    for line0 in index_file0:
        index_dict[line0.strip().split("\t")[0]] = line0.strip().split("\t")[1]
    SeqType = input("Please enter the type of sequencer(NovaSeq or NextSeq): ")
    if SeqType == "NextSeq":
        index_file1 = open(r"E:\厦维生物\samplesheet\Index_I5.txt","r")
        for line1 in index_file1:
            index_dict[line1.strip().split("\t")[0]] = Seq(line1.strip().split("\t")[1]).reverse_complement()  # 方向互补序列

    else:
        index_file1 = open(r"E:\厦维生物\samplesheet\Index_I5.txt","r")
        for line1 in index_file1:
            index_dict[line1.strip().split("\t")[0]] = line1.strip().split("\t")[1]


# build sample and lib info dictory
def generate_sample_dict(sample_file,sample_lib_dict):
    data = sample_file.sheet_by_index(0)
    n_rows = data.nrows
    for i in range(1,n_rows):
        sample_lib_dict[data.cell(i,1).value] = [data.cell(i,0).value,data.cell(i,7).value,data.cell(i,8).value]
    print(len(sample_lib_dict))
    return sample_lib_dict

# generate samplesheet
# def generate_samplesheet(path,file_name,sample_lib_dict,index_dict):
def generate_samplesheet(file_name,sample_lib_dict,index_dict):
    cur_time = datetime.datetime.now().strftime('%Y/%m/%d')
    # with open(r"%s\%s_%s.csv"%(path,file_name,datetime.datetime.now().strftime('%Y%m%d')), "w", newline="") as outfile:
    with open(r"E:\厦维生物\samplesheet\数据拆分\SampleSheet\%s_%s.csv"%(file_name,datetime.datetime.now().strftime('%Y%m%d')), "w", newline="") as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(["[Header]"])
        csv_writer.writerow(["IEMFileVersion", 4])
        csv_writer.writerow(["Date", cur_time,])
        csv_writer.writerow(["Workflow", "GenerateFASTQ"])
        csv_writer.writerow(["Application", "NextSeq FASTQ Only"])
        csv_writer.writerow(["Assay", "AmoyDx kit"])
        csv_writer.writerow(["Description"])
        csv_writer.writerow(["Chemistry", "Amplicon"])
        csv_writer.writerow([])
        csv_writer.writerow(["[Reads]"])
        csv_writer.writerow([151])
        csv_writer.writerow([151])
        csv_writer.writerow([])
        csv_writer.writerow(["[Settings]"])
        csv_writer.writerow(["Adapter","AGATCGGAAGAGCACACGTCTGAACTCCAGTCA"])
        csv_writer.writerow(["AdapterRead2","AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT"])
        csv_writer.writerow([])
        csv_writer.writerow(["[Data]"])
        col_name = ["Sample_ID","Sample_Name","Sample_Plate","Sample_Well","I7_Index_ID","index","I5_Index_ID","index2","Sample_Project","Description"]
        csv_writer = csv.DictWriter(outfile,fieldnames=col_name)
        csv_writer.writeheader()
        for sample_key,sample_val in sample_lib_dict.items():
            if sample_val[1] in index_dict and sample_val[2] in index_dict:
                csv_writer.writerow({"Sample_ID": sample_key, "Sample_Name": sample_val[0],
                                     "I7_Index_ID": sample_val[1], "index": index_dict[sample_val[1]],
                                     "I5_Index_ID":sample_val[2], "index2":index_dict[sample_val[2]] ,
                                     "Sample_Project": "", "Description": ""})

if __name__ == '__main__':
    path = r"E:\厦维生物\samplesheet\数据拆分\tmp\xlsx"
    # file_name = input("请输入文库信息文件：")
    # print(file_name)
    index_dict = {}
    run_list = []
    generate_run_info_list(run_list)
    gennerate_index(index_dict)
    for r in run_list:
        sample_lib_dict = {}
        sample_file = xlrd.open_workbook(r"%s\%s.xlsx" % (path, r))
        generate_sample_dict(sample_file,sample_lib_dict)
        generate_samplesheet(r,sample_lib_dict,index_dict)