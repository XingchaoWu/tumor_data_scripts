# _*_ coding=utf-8 _*_
# author: xingchaowu
# date: 202-03-27

# 统计EGFR exon19 del
import re
sample_list = []
EGFR_ex20_list = []

# mutation NM_005228.3:exon19:c.2240_2254delTAAGAGAAGCAACAT:p.L747_T751del
# sample_num	lib_num	project	mutation_gene	mutation_site	mutation_frequency	Gender	Age	Smoking_Hist	Pathological_diagnosis
insfile = open(r"E:\厦维生物\99_Sample_Datainfo\EGFR_ex20ins\EGFR_ex20_mutation_ins.txt","w")
insfile.write("#sample_num\tlib_num\tproject\tmutation_gene\tmutation_site\tmutation_frequency\tGender\tAge\tSmoking_Hist\tPathological_diagnosis\n")
ins_list = []

delinsfile = open(r"E:\厦维生物\99_Sample_Datainfo\EGFR_ex20ins\EGFR_ex20_mutation_delins.txt","w")
delinsfile.write("#sample_num\tlib_num\tproject\tmutation_gene\tmutation_site\tmutation_frequency\tGender\tAge\tSmoking_Hist\tPathological_diagnosis\n")
delins_list = []

otherfile = open(r"E:\厦维生物\99_Sample_Datainfo\EGFR_ex20ins\EGFR_ex20_mutation_other.txt", "w")
otherfile.write("#sample_num\tlib_num\tproject\tmutation_gene\tmutation_site\tmutation_frequency\tGender\tAge\tSmoking_Hist\tPathological_diagnosis\n")
snp_list = []

# 筛选出EGFR和exon19突变的信息
with open(r"E:\厦维生物\99_Sample_Datainfo\EGFR_ex20ins\EGFR_ex20_mutation_total.txt","w") as outfile:
    outfile.write("#sample_num\tlib_num\tproject\tmutation_gene\tmutation_site\tmutation_frequency\tGender\tAge\tSmoking_Hist\tPathological_diagnosis\n")
    with open(r"E:\厦维生物\99_Sample_Datainfo\18_19_mutation_total.csv","r") as infile:
        for line in infile:
            if not line.startswith("#"):
                sample_list.append(line.strip().split(",")[0])
                if line.strip().split(",")[3] == "EGFR" and "exon20" in line.strip().split(",")[4]:
                    EGFR_ex20_list.append(line.strip().split(",")[0])
                    outfile.write(line.strip().replace(",","\t")+"\n")
print("18年10月-19年12月总样本数：%s"%(len(list(set(sample_list)))))
print("18年10月-19年12月 EGFR exon20 突变样本数：%s"%(len(list(set(EGFR_ex20_list)))))


with open(r"E:\厦维生物\99_Sample_Datainfo\EGFR_ex20ins\EGFR_ex20_mutation_total.txt","r") as infile1:
    for line1 in infile1:
        if not line1.startswith("#"):
            info = line1.strip().split("\t")[4].split(":")[2]
            if re.findall("c.[0-9]*_[0-9]*ins[0-9A-Z]*",info) and "delins" not in line1.strip().split("\t")[4]:
                insfile.write(line1.strip()+"\n")
                ins_list.append(line1.strip().split("\t")[0])
            elif "delins" in line1.strip().split("\t")[4]:
                delinsfile.write(line1.strip()+"\n")
                delins_list.append(line1.strip().split("\t")[0])
            else:
                otherfile.write(line1.strip()+"\n")
                snp_list.append(line1.strip().split("\t")[0])

print("18年10月-19年12月 EGFR exon20 ins突变样本数：%s"%(len(list(set(ins_list)))))
print("18年10月-19年12月 EGFR exon20 delins突变样本数：%s"%(len(list(set(delins_list)))))
print("18年10月-19年12月 EGFR exon20 snv突变样本数：%s"%(len(list(set(snp_list)))))

# 样本数统计文件
coutfille = open(r"E:\厦维生物\99_Sample_Datainfo\EGFR_ex20ins\EGFR_ex20_mutation_stat.txt","w")
coutfille.write("18年10月-19年12月总样本数：%s\n"%(len(list(set(sample_list)))))
coutfille.write("18年10月-19年12月 EGFR exon20 突变样本数：%s\n"%(len(list(set(EGFR_ex20_list)))))
coutfille.write("18年10月-19年12月 EGFR exon20 ins突变样本数：%s\n"%(len(list(set(ins_list)))))
coutfille.write("18年10月-19年12月 EGFR exon20 delins突变样本数：%s\n"%(len(list(set(delins_list)))))
coutfille.write("18年10月-19年12月 EGFR exon20 snv突变样本数：%s\n"%(len(list(set(snp_list)))))




