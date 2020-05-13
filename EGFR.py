# _*_ coding=utf-8 _*_
# author: xingchaowu
# date: 202-03-27
sample_list = []
EGFR_list = []


# 筛选出EGFR突变的信息
with open(r"E:\厦维生物\99_Sample_Datainfo\EGFR\EGFR_mutation_total.txt","w") as outfile:
    outfile.write("#sample_num\tlib_num\tproject\tmutation_gene\tmutation_site\tmutation_frequency\tGender\tAge\tSmoking_Hist\tPathological_diagnosis\n")
    with open(r"E:\厦维生物\99_Sample_Datainfo\18_19_mutation_total.csv","r") as infile:
        for line in infile:
            if not line.startswith("#"):
                sample_list.append(line.strip().split(",")[0])
                if line.strip().split(",")[3] == "EGFR":
                    EGFR_list.append(line.strip().split(",")[0])
                    outfile.write(line.strip().replace(",","\t")+"\n")
print("18年10月-19年12月总样本数：%s"%(len(list(set(sample_list)))))
print("18年10月-19年12月 EGFR 突变样本数：%s"%(len(list(set(EGFR_list)))))

# # 样本数统计文件
coutfille = open(r"E:\厦维生物\99_Sample_Datainfo\EGFR\EGFR_mutation_stat.txt","w")
coutfille.write("18年10月-19年12月总样本数：%s\n"%(len(list(set(sample_list)))))
coutfille.write("18年10月-19年12月 EGFR突变样本数：%s\n"%(len(list(set(EGFR_list)))))





