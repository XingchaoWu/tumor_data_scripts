# _*_ coding=utf-8 _*_
# author: xingchaowu
# date: 2020-09-10


import pandas as pd
from scipy import stats
import re
import math


def judge_Gaussian():
    global p_value,data_list,data_std,data_mean
    data_list = []
    # 判断数据是否符合正态分布
    # 读取测试结果（结果按列整理在txt文件中）并存入列表中
    data = open(r"E:\New_Project\05_空白限与检测限计算\demo_LoB.txt")
    for d in data.readlines():
        if not d.startswith("#"):
            for i in d.split():
                data_list.append(float(i))
    df = pd.DataFrame(data_list,columns=["values"])
    # 正态分布判定
    data_mean = df["values"].mean()  # 计算平均数
    data_std = df["values"].std()  # 计算标准差
    result = stats.kstest(df["values"],"norm",(data_mean,data_std))  # p-value > 0.05 即符合正态分布
    p_value = float(re.findall(r'0.\d+',str(result))[1])  # 提取K-Stest正态检验计算的P值
    if p_value > 0.05:  # 判断是否符合正态分布并返回P值
        print("LoB数据符合正态分布,p-value:{}".format(p_value))
    else:
        print("LoB数据不符合正态分布,p-value:{}".format(p_value))
    return p_value,data_mean,data_std
# calculate blank
def calculate_blank(data_list):
    judge_Gaussian()
    # 空白值计算
    if p_value > 0.05:
        k = eval(input("请输入空白样本数:"))
        blank_cp = 1.645 / (1 - (1/(4*(len(data_list)-k))))
        LoB = data_mean + blank_cp * data_std  # LoB = M + cp * SD
        print("计算的LoB值:{}".format(LoB))
    else:
        data_sorted_list = sorted(data_list)
        Rank_position = len(data_list) * (95 / 100) + 0.5
        LoB =data_sorted_list[int(Rank_position)] \
             + (Rank_position - int(Rank_position)) \
             * (data_sorted_list[math.ceil(Rank_position)]
                - data_sorted_list[int(Rank_position)])  # LoB = X(R) + 0.5(X(R+1)-X(R))
        print("计算的LoB值:{}".format(LoB))
    return LoB

# calculate limit of detection
def calculate_detection():
    global LoD, p_value_detection
    data_Lod = pd.read_csv(r"E:\New_Project\05_空白限与检测限计算\demo_loD.txt",sep="\t",)
    print(data_Lod)
    # 判断数据是否符合正态分布
    # 读取测试结果（结果按列整理在txt文件中）并存入列表中
    # data_list_LoD = []
    # data_LoD = open(r"E:\New_Project\05_空白限与检测限计算\demo_loD.txt")
    # for d in data_LoD.readlines():
    #     if not d.startswith("#"):
    #         for i in d.split():
    #             data_list_LoD.append(float(i))
    # df = pd.DataFrame(data_list_LoD,columns=["values"])
    # print(len(df))
    # 正态分布判定
    # data_LoD_mean_list = []
    # data_LoD_std_list = []
    # J = eval(input("请输入低浓度样本数:"))
    # for i in range(int(len(df)/12)+1):
        # print(i, df[0,12])

        # data_LoD_mean_list = df[0,12].mean()
        # data_LoD_mean_list.append(df["values"][12*i,12*i])
        # data_LoD_std_list = df[0,12].std()
        # data_LoD_std_list.append(df["values"][12*i,12*i])
        # data_LoD_mean = df["values"].mean()  # 计算平均数
        # data_LoD_std = df["values"].std()  # 计算标准差
        # print(data_LoD_mean_list,data_LoD_std_list)

        # result = stats.kstest(df["values"],"norm",(data_LoD_mean,data_LoD_std))  # p-value > 0.05 即符合正态分布
        # p_value_detection = float(re.findall(r'0.\d+',str(result))[1])  # 提取K-Stest正态检验计算的P值
        # if p_value_detection > 0.05:  # 判断是否符合正态分布并返回P值
        #     print("LoD数据符合正态分布,p-value:{}".format(p_value_detection))
        # else:
        #     print("LoD数据不符合正态分布,p-value:{}".format(p_value_detection))
        #
        # # 空白值计算
        # if p_value_detection > 0.05:
        #     print("LoD数据符合正态分布")
        #     detection_cp = 1.645 / (1 - (1/(4*(len(data_list)-J))))
        #     LoD = LoB + detection_cp * data_std  # LoB = M + cp * SD
        #     print("计算的LoD值:{}".format(LoB))
        # else:
        #     print("LoD数据不符合正态分布")
        #     data_sorted_list = sorted(data_list)
        #     print(data_sorted_list)
        #     LoD = data_sorted_list[int(len(data_list)/2)]
        #     print("计算的LoD值:{}".format(LoB))
        # return LoD, p_value_detection


if __name__ == '__main__':

    # calculate_blank(data_list)
    calculate_detection()