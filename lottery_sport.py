#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__date__ = '2023/1/30'

"""
体彩大乐透双色球彩票中奖规则
"""

winning_red_balls = [1, 5, 11, 15, 33]
winning_blue_balls = [1, 10]


def check_prize(red_balls, blue_balls):
    red_balls = sorted(red_balls)  # 对红球号码进行排序
    red_match = 0  # 红球匹配个数
    blue_match = 0  # 蓝球匹配个数

    # 计算红球匹配个数
    for ball in red_balls:
        if ball in winning_red_balls:
            red_match += 1

    # 判断蓝球是否匹配
    for ball in blue_balls:
        if ball in winning_blue_balls:
            blue_match += 1

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


print(check_prize([1, 5, 11, 15, 33], [5, 7]))
print(check_prize([6, 21, 27, 31, 33], [4, 6]))
print(check_prize([4, 14, 24, 27, 34], [6, 12]))
print(check_prize([2, 10, 13, 29, 32], [6, 12]))
print(check_prize([1, 4, 14, 24, 31], [8, 11]))
