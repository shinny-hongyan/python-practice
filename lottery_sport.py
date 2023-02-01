#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__date__ = '2023/1/30'

"""
体彩大乐透双色球彩票中奖规则
"""

def level(red_match, blue_match):
    # 根据匹配个数判断中奖级别
    if red_match == 5 and blue_match == 2:
        return "一等奖"
    elif red_match == 5 and blue_match == 1:
        return "二等奖"
    elif red_match == 5:
        return "三等奖"
    elif red_match == 4 and blue_match == 2:
        return "四等奖"
    elif red_match == 4 and blue_match == 1:
        return "五等奖"
    elif red_match == 3 and blue_match == 2:
        return "六等奖"
    elif red_match == 4 and blue_match == 0:
        return "七等奖"
    elif (red_match == 3 and blue_match == 1) or (red_match == 2 and blue_match == 2):
        return "八等奖"
    elif (red_match == 3 and blue_match == 0) or (red_match == 1 and blue_match == 2) or (
            red_match == 2 and blue_match == 1) or (red_match == 0 and blue_match == 2):
        return "九等奖"
    else:
        return "未中奖"


def check_prize(winning_red_balls, winning_blue_balls, red_balls, blue_balls):
    red_balls = sorted(red_balls)  # 对红球号码进行排序
    red_match = 0  # 红球匹配个数
    blue_match = 0  # 蓝球匹配个数

    red_balls_result = ""
    blue_balls_result = ""

    # 计算红球匹配个数
    for ball in red_balls:
        if ball in winning_red_balls:
            red_match += 1
            red_balls_result += f"{ball} [√]  "
        else:
            red_balls_result += f"{ball} [×]  "

    # 判断蓝球是否匹配
    for ball in blue_balls:
        if ball in winning_blue_balls:
            blue_match += 1
            blue_balls_result += f"{ball} [√]  "
        else:
            blue_balls_result += f"{ball} [×]  "

    print(f"{red_balls_result} | {blue_balls_result}    {level(red_match, blue_match)}")


if __name__ == '__main__':
    print(f"请参考 http://kaijiang.500.com/shtml/dlt/23009.shtml?0_ala_baidu 中的开奖号码, 进行输入对比")
    winning_red_balls = [int(x) for x in input("请输入开奖红球号码，用空格隔开：").split()]
    winning_blue_balls = [int(x) for x in input("请输入开奖蓝球号码，用空格隔开：").split()]

    while True:
        print(f"")
        red_balls = [int(x) for x in input("请输入红球号码，用空格隔开(直接回车退出)：").split()]
        if red_balls is None or len(red_balls) != 5:
            break
        blue_balls = [int(x) for x in input("请输入蓝球号码，用空格隔开：").split()]
        check_prize(winning_red_balls, winning_blue_balls, red_balls, blue_balls)
