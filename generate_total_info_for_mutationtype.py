# _*_ coding= utf-8 _*_
# date: 2020-04-09
# author: xingchao

import csv
def generate_total_info():
    """
    根据突变类型匹配出所有样本的突变频率及浓度信息
    :return:
    """
    match_list = []
    null_list = []
    # 生成突变类型的列表
    mutation_list = []
    # with open(r"E:\厦维生物\95_CDX\样本信息\样本筛选\mutation_info_v3.txt","r") as tmp:
    with open(r"E:\厦维生物\95_CDX\样本信息\样本筛选\ex20ins.txt","r") as tmp:
    # with open(r"E:\厦维生物\95_CDX\样本信息\样本筛选\mutation_info_v3.txt","r") as tmp:
    # with open(r"E:\厦维生物\95_CDX\样本信息\样本筛选\mutation_info_v3.txt","r") as tmp:
        for line in tmp:
            if not line.startswith("#"):
                mutation_list.append(line.strip())
    # 生成样本信息文件

    # 保存非参考品盘的样本信息
    outfile1 = open(r"E:\厦维生物\95_CDX\样本信息\样本筛选\blood_sample_mutation_info_ex20ins_unmatch_v3.csv","w",newline="")
    header = ["#gene","type","mutation_type","num","sample_num","lib_num","Mut_Frequency(%)","Con.(ng/ul)"]
    write_csv1 = csv.DictWriter(outfile1,fieldnames=header)
    write_csv1.writeheader()

    # 生成匹配上的参考品盘的样本信息
    with open(r"E:\厦维生物\95_CDX\样本信息\样本筛选\blood_sample_mutation_info_ex20ins.csv","w",newline="") as outfile:
        header = ["#type_num","type","mutation_type","num","sample_num","lib_num","Mut_Frequency(%)","Con.(ng/ul)"]
        write_csv = csv.DictWriter(outfile,fieldnames=header)
        write_csv.writeheader()
        with open(r"E:\厦维生物\95_CDX\样本信息\18and19样本浓度汇总\18and19Sample_concentration_total.csv") as infile:
            for info in infile:
                if not info.startswith("#"):
                    if info.strip().split(",")[4] in mutation_list and "PD" in info.strip().split(",")[1] and "EPD" not in info.strip().split(",")[1]:
                        match_list.append(info.strip().split(",")[4])
                        write_csv.writerow({"#type_num":mutation_list.index(info.strip().split(",")[4])+1,
                                            "type":"type_%s"%(mutation_list.index(info.strip().split(",")[4])+1),
                                           "mutation_type":info.strip().split(",")[4],
                                            "num":1,
                                            "sample_num":info.strip().split(",")[0],
                                            "lib_num":info.strip().split(",")[1],
                                            "Mut_Frequency(%)":float(info.strip().split(",")[5])*100,
                                            "Con.(ng/ul)":info.strip().split(",")[10]})
                    elif info.strip().split(",")[4] not in mutation_list and "PD" in info.strip().split(",")[1] and "EPD" not in info.strip().split(",")[1]:
                        write_csv1.writerow({"#gene": info.strip().split(",")[3],
                                            "type": info.strip().split(",")[2],
                                            "mutation_type": info.strip().split(",")[4],
                                            "num": 1,
                                            "sample_num": info.strip().split(",")[0],
                                            "lib_num": info.strip().split(",")[1],
                                            "Mut_Frequency(%)":info.strip().split(",")[5],
                                            "Con.(ng/ul)": info.strip().split(",")[10]})
    for i in mutation_list:
        if i not in list(set(match_list)):
            null_list.append(i)
    print("未匹配到样本的突变类型:%s"%null_list)
    print("未匹配到样本的突变类型数:%s"%len(null_list))


    return None

if __name__ == '__main__':
    generate_total_info()