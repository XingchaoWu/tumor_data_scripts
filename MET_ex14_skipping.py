# _*_ coding=utf-8 _*_
# author xingchao
# date 2020-03-27

# 统计MET ex14 skippling
sample_list = []
MET_list = []

# mutation NM_005228.3:exon19:c.2240_2254delTAAGAGAAGCAACAT:p.L747_T751del
# sample_num	lib_num	project	mutation_gene	mutation_site	mutation_frequency	Gender	Age	Smoking_Hist	Pathological_diagnosis
intron13_file = open(r"E:\厦维生物\99_Sample_Datainfo\MET\MET_mutation_intron13.txt","w")
intron13_file.write("#sample_num\tlib_num\tproject\tmutation_gene\tmutation_site\tmutation_frequency\tGender\tAge\tSmoking_Hist\tPathological_diagnosis\n")
intron13_list = []

exon14_file = open(r"E:\厦维生物\99_Sample_Datainfo\MET\MET_mutation_exon14.txt","w")
exon14_file.write("#sample_num\tlib_num\tproject\tmutation_gene\tmutation_site\tmutation_frequency\tGender\tAge\tSmoking_Hist\tPathological_diagnosis\n")
exon14_list = []

intron14_file = open(r"E:\厦维生物\99_Sample_Datainfo\MET\MET_mutation_intron14.txt", "w")
intron14_file.write("#sample_num\tlib_num\tproject\tmutation_gene\tmutation_site\tmutation_frequency\tGender\tAge\tSmoking_Hist\tPathological_diagnosis\n")
snp_list = []

# 筛选出EGFR和exon19突变的信息
with open(r"E:\厦维生物\99_Sample_Datainfo\MET\MET_mutation_total.txt","w") as outfile:
    outfile.write("#sample_num\tlib_num\tproject\tmutation_gene\tmutation_site\tmutation_frequency\tGender\tAge\tSmoking_Hist\tPathological_diagnosis\n")
    with open(r"E:\厦维生物\99_Sample_Datainfo\18_19_mutation_total.csv","r") as infile:
        for line in infile:
            if not line.startswith("#"):
                sample_list.append(line.strip().split(",")[0])
                if line.strip().split(",")[3] == "MET":
                    MET_list.append(line.strip().split(",")[0])
                    outfile.write(line.strip().replace(",","\t")+"\n")
print("18年10月-19年12月总样本数：%s"%(len(list(set(sample_list)))))
print("18年10月-19年12月 MET 突变样本数：%s"%(len(list(set(MET_list)))))


with open(r"E:\厦维生物\99_Sample_Datainfo\MET\MET_mutation_total.txt","r") as infile1:
    for line1 in infile1:
        if not line1.startswith("#"):
            if line1.strip().split("\t")[3] == "MET" and "intron14" in line1.strip().split("\t")[4] and "exon14" not in line1.strip().split("\t")[4]:  #
            # if line1.strip().split("\t")[3] == "MET" and line1.strip().split("\t")[4].split(":")[2] == "intron14":
                intron14_file.write(line1.strip()+"\n")
                intron13_list.append(line1.strip().split("\t")[0])
            elif line1.strip().split("\t")[3] == "MET" and "exon14" in line1.strip().split("\t")[4]:
                exon14_file.write(line1.strip()+"\n")
                exon14_list.append(line1.strip().split("\t")[0])
            elif line1.strip().split("\t")[3] == "MET" and "intron13" in line1.strip().split("\t")[4] and "exon14" not in line1.strip().split("\t")[4]:
                intron13_file.write(line1.strip()+"\n")
                snp_list.append(line1.strip().split("\t")[0])


print("18年10月-19年12月 MET_intron13突变样本数：%s"%(len(list(set(intron13_list)))))
print("18年10月-19年12月 MET_exon14突变样本数：%s"%(len(list(set(exon14_list)))))
print("18年10月-19年12月 MET_intron14突变样本数：%s"%(len(list(set(snp_list)))))

# 样本数统计文件
coutfille = open(r"E:\厦维生物\99_Sample_Datainfo\MET\MET_mutation_stat.txt","w")
coutfille.write("18年10月-19年12月总样本数：%s\n"%(len(list(set(sample_list)))))
coutfille.write("18年10月-19年12月 MET 突变样本数：%s\n"%(len(list(set(MET_list)))))
coutfille.write("18年10月-19年12月 MET intron13 突变样本数：%s\n"%(len(list(set(intron13_list)))))
coutfille.write("18年10月-19年12月 EGFR exon14 突变样本数：%s\n"%(len(list(set(exon14_list)))))
coutfille.write("18年10月-19年12月 EGFR intron14 突变样本数：%s\n"%(len(list(set(snp_list)))))