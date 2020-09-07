# _*_ coding=utf-8 _*_
# author: xingchaowu


"""
初期版本
从汇总样本突变信息表中提取10基因Panel血浆样本检出信息以及样本及突变总数统计
"""

PosNum = 0
NegNum = 0
genelist = []
samplelist = []

# 
with open(r"E:\厦维生物\汇总结果\检验所2018-2019临检样本信息汇总\20200814.csv","r") as infile:
    with open(r"E:\厦维生物\汇总结果\检验所2018-2019临检样本信息汇总\10基因adddiagnosis.txt","w") as outfile:
        outfile.write("#sample_num\tlib_num\tproject\tmutation_gene\tmutation_site\tmutation_frequency\tmutation_type\tPathological_diagnosis\n")
        for line in infile：
            if ("P" in line.strip().split(",")[1] and "EP" not in line.strip().split(",")[1]) and ("10" in line.strip().split(",")[2] and "组织" not in line.strip().split(",")[2]):
                samplelist.append(line.strip().split(",")[0])
                genelist.append(line.strip().split(",")[3])
                # if line.strip().split(",")[3] != "-":
                outfile.write(line.strip().split(",")[0] + "\t"
                              + line.strip().split(",")[1] + "\t"
                              +line.strip().split(",")[2] + "\t"
                              +line.strip().split(",")[3] + "\t"
                              +line.strip().split(",")[4] + "\t"
                              +line.strip().split(",")[5] + "\t"
                              +line.strip().split(",")[6] + "\t"
                              +line.strip().split(",")[10] + "\n")
                PosNum += 1
print("参与统计的血浆阳性样本总数:%s"%len(set(samplelist)))
print("参与统计的血浆阳性样本总数:%s"%PosNum)
print("参与统计的血浆阴性样本总数:%s"%NegNum)
print("血浆样本已检测到基因类型：%s"%set(genelist))


with open(r"E:\厦维生物\汇总结果\检验所2018-2019临检样本信息汇总\10基因.txt", "r") as infile:
    for line in infile:
        if not line.strip().startswith("#"):
            genelist.append(line.strip().split("\t")[3])
    print(set(genelist))

  
EGFR = []
HIP1_ALK = []
TRIM24_RET = []
TPM3_ROS1 = []
NCOA4_RET = []
CCDC6_RET =[]
MET =[]
RET = []
BRAF =[]
ALK =[]
KIF5B_RET = []
EML4_ALK = []
NRAS =[]
KIF5B_ALK = []
KRAS = []
RET_ALK = []
ERBB2 = []
YES1_RET = []
EZR_ROS1 = []
PIK3CA = []
CDK4 = []
ROS1 = []

with open(r"E:\厦维生物\汇总结果\检验所2018-2019临检样本信息汇总\10基因.txt", "r") as infile:
    for line in infile:
        if not line.strip().startswith("#"):
            if line.strip().split("\t")[3] == "EGFR":
                EGFR.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "HIP1-ALK":
                HIP1_ALK.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "TRIM24-RET":
                TRIM24_RET.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "TPM3-ROS1":
                TPM3_ROS1.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "NCOA4-RET":
                NCOA4_RET.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "MET":
                MET.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "RET":
                RET.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "BRAF":
                BRAF.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "ALK":
                ALK.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "KIF5B-RET":
                KIF5B_RET.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "EML4-ALK":
                EML4_ALK.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "KIF5B-ALK":
                KIF5B_ALK.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "CDK4":
                CDK4.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "KRAS":
                KRAS.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "RET-ALK":
                RET_ALK.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "ERBB2":
                ERBB2.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "YES1-RET":
                YES1_RET.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "EZR-ROS1":
                EZR_ROS1.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "PIK3CA":
                PIK3CA.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "CCDC6-RET":
                CCDC6_RET.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "NRAS":
                NRAS.append(line.strip().split("\t")[0])
            elif line.strip().split("\t")[3] == "ROS1":
                ROS1.append(line.strip().split("\t")[0])

    print(len(set(EGFR)))
    print(len(set(HIP1_ALK)))
    print(len(set(TRIM24_RET)))
    print(len(set(TPM3_ROS1)))
    print(len(set(NCOA4_RET)))
    print(len(set(MET)))
    print(len(set(RET)))
    print(len(set(BRAF)))
    print(len(set(ALK)))
    print(len(set(KIF5B_RET)))
    print(len(set(EML4_ALK)))
    print(len(set(KIF5B_ALK)))
    print(len(set(CDK4)))
    print(len(set(KRAS)))
    print(len(set(RET_ALK)))
    print(len(set(ERBB2)))
    print(len(set(YES1_RET)))
    print(len(set(EZR_ROS1)))
    print(len(set(PIK3CA)))
    print(len(set(CCDC6_RET)))
    print(len(set(NRAS)))
    print(len(set(ROS1)))




