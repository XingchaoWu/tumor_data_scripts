
lung_total_list = []
total_list = []
sample_info_dict = {}
with open(r"E:\厦维生物\99_Sample_Datainfo\lib_info_03_15_new.csv","r") as incsv:
    for line in incsv:
        total_list.append(line.strip().split(",")[0])
        sample_info_dict[line.strip().split(",")[0]] = line.strip().split(",")[5]
        if "肺" in line.strip().split(",")[5]:
            lung_total_list.append(line.strip().split(",")[0])
print("18年10月19日-19年12月31日肺癌样本总数:%s"%(len(list(set(total_list)))-1))
print(lung_total_list)
print("18年10月19日-19年12月31日肺癌样本总数:%s"%(len(list(set(lung_total_list)))-1))
print(sample_info_dict)
print(len(sample_info_dict))

lung_list = []
with open(r"E:\厦维生物\汇总结果\检验所2018-2019临检样本信息汇总\EGFR_ex20ins\info_18and19_EGFR_exon20ins_filter_add_diagnosis.txt","w") as outfile:
    outfile.write("sample_num\tlib_num\tproject\tmutation_gene\tmutation_site\tmutation_frequency\tPathological_diagnosis\n")
    with open(r"E:\厦维生物\汇总结果\检验所2018-2019临检样本信息汇总\EGFR_ex20ins\info_18and19_EGFR_filter_all.txt","r") as infile:
        for line_info in infile:
            for k, v in sample_info_dict.items():
                if line_info.strip().split("\t")[0] == k:
                    lung_list.append(k)
                    outfile.write(line_info.strip("\n")+"\t"+v+"\n")

print(len(list(set(lung_list))))
