# _*_ coding=utf-8 _*_
# author: xingchaowu
# date: 2020-08-25

import xlrd
import datetime
import csv
import os , argparse

def gennerate_index(index_dict):
    index_file = open("/home/wuxingchao/scripts/Index/Index.txt","r")
    for line in index_file:
        index_dict[line.strip().split("\t")[0]] = line.strip().split("\t")[1]

def generate_sample_dict(cur_path,sample_lib_dict):
    sample_file = xlrd.open_workbook("%s/%s"%(cur_path,args.xlsfile))
    data = sample_file.sheet_by_index(0)
    n_rows = data.nrows
    for i in range(1,n_rows):
        sample_lib_dict[data.cell(i,2).value] = [data.cell(i,1).value,data.cell(i,8).value,data.cell(i,9).value]
    print(len(sample_lib_dict))
    return sample_lib_dict


def generate_samplesheet(cur_path,sample_lib_dict,index_dict):
    cur_time = datetime.datetime.now().strftime('%Y/%m/%d')
    with open("%s/Samplesheet_%s.csv"%(cur_path,datetime.datetime.now().strftime('%Y%m%d')), "w", newline="") as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(["[Header]"])
        csv_writer.writerow(["IEMFileVersion", 4])
        csv_writer.writerow(["Date", cur_time])  # 通过datetime获取当前时间，并规定其格式（yy/mm/dd）
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
    parser = argparse.ArgumentParser("")
    parser.add_argument("-i", "--xlsfile",type=str,help="the xlsx file of lib")
    parser.add_argument("-o","--outfile",type=str,help="outputpath")
    args = parser.parse_args()
    cur_path = os.getcwd()
    index_dict = {}
    sample_lib_dict = {}
    gennerate_index(index_dict)
    generate_sample_dict(cur_path,sample_lib_dict)
    generate_samplesheet(cur_path,sample_lib_dict,index_dict)