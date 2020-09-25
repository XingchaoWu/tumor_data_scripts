# _*_ coding=utf-8 _*_
# author: xingchaowu
# date: 2020-09-25

"""
extract fusion mutation
"""
import csv
import xlwt

# filter sample info (tissue or plasma)
def  sample_filter(work_path,sample_type):
    sample_list = []
    file_filter = open(r"{}\{}_fileter.txt".format(work_path,sample_type), "w")
    total_data_file = open(r"{}\18_19_mutation_total.csv".format(work_path), "r")
    if sample_type == "tissue":
        for line in total_data_file:
            if "FD" in line.strip().split(",")[1] or "TD" in line.strip().split(",")[1]:
                file_filter.write(line)
                sample_list.append(line.strip().split(",")[1])
    elif sample_type == "plasma":
        for line in total_data_file:
            if "PD" in line.strip().split(",")[1] or "EPD" not in line.strip().split(",")[1]:
                file_filter.write(line)
                sample_list.append(line.strip().split(",")[1])
    else:
        for line in total_data_file:
            file_filter.write(line)
            sample_list.append(line.strip().split(",")[1])
    statistics_file.write("Total {} sample : {}\n".format(sample_type,len(set(sample_list))))


def fusion_filter_by_gene(work_path,sample_type,gene_name):
    gene_dict = {}
    gene_list = []
    with open(r"{}\{}_fileter.txt".format(work_path,sample_type), "r") as infile1:
        for line1 in infile1:
            if "{}".format(gene_name) in line1.strip().split(",")[4]:
                gene_list.append(line1.strip().split(",")[1].strip())
                ros_key = line1.strip().split(",")[4].strip()
                ros_value = line1.strip().split(",")[1].strip()
                if ros_value is not "":
                    if ros_key in gene_dict:
                        gene_dict.get(ros_key).append(ros_value)
                    else:
                        gene_dict.setdefault(ros_key, []).append(ros_value)
    statistics_file.write("{}检出样本数\t{}\n".format(gene_name,len(set(gene_list))))
    statistics_file.write("#Mutation_Site\tSample_Stat\tSample_Num\n")
    for r_k, r_v in gene_dict.items():
        statistics_file.write("{}\t{}\t{}\n".format(r_k, len(r_v), ",".join(r_v)))

def SNVIndel_filter_by_gene(work_path,sample_type,gene_name):
    gene_dict = {}
    gene_list = []
    with open(r"{}\{}_fileter.txt".format(work_path,sample_type), "r") as infile1:
        for line1 in infile1:
            if "{}".format(gene_name) in line1.strip().split(",")[3]:
                gene_list.append(line1.strip().split(",")[1].strip())
                ros_key = line1.strip().split(",")[4].strip()
                ros_value = line1.strip().split(",")[1].strip()
                if ros_value is not "":
                    if ros_key in gene_dict:
                        gene_dict.get(ros_key).append(ros_value)
                    else:
                        gene_dict.setdefault(ros_key, []).append(ros_value)
    statistics_file.write("{}检出样本数\t{}\n".format(gene_name,len(set(gene_list))))
    statistics_file.write("#Mutation_Site\tSample_Stat\tSample_Num\n")
    for r_k, r_v in gene_dict.items():
        statistics_file.write("{}\t{}\t{}\n".format(r_k, len(r_v), ",".join(r_v)))

if __name__ == '__main__':
    work_path = input("Input current work path:")
    sample_type = input("Input sample type for filtering (tissue/plasma/all):")
    mutation_type = input("Input mutation type(fusion or SnvIndel):")
    gene_name = input("Input gene name:")
    statistics_file = open(r"{}\tissue_{}_stat.txt".format(work_path,gene_name), "w")
    # statistics_file_book = xlwt.Workbook(r"{}\tissue_{}_stat.txt".format(work_path,gene_name), "w")
    # statistics_file = statistics_file_book.active_sheet("{}".format(gene_name))
    sample_filter(work_path,sample_type)
    if mutation_type == "fusion":
        fusion_filter_by_gene(work_path,sample_type,gene_name)
    else:
        SNVIndel_filter_by_gene(work_path,sample_type,gene_name)
