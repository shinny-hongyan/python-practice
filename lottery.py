#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__date__ = '2023/1/30'


winning_red_balls = [3, 4, 19, 23, 30, 32] # 红球
winning_blue_ball = 6 # 蓝色球

def check_prize(red_balls, blue_ball):
    red_balls = sorted(red_balls)  # 对红球号码进行排序
    red_match = 0  # 红球匹配个数
    blue_match = 0  # 蓝球匹配个数

    # 计算红球匹配个数
    for ball in red_balls:
        if ball in winning_red_balls:
            red_match += 1

    # 判断蓝球是否匹配
    if blue_ball == winning_blue_ball:
        blue_match = 1

    # 根据匹配个数判断中奖级别
    if red_match == 6 and blue_match == 1:
        return "一等奖"
    elif red_match == 6:
        return "二等奖"
    elif red_match == 5 and blue_match == 1:
        return "三等奖"
    elif red_match == 5 or (red_match == 4 and blue_match == 1):
        return "四等奖"
    elif red_match == 4 or (red_match == 3 and blue_match == 1):
        return "五等奖"
    elif red_match == 2 and blue_match == 1 or red_match == 1 and blue_match == 1 or red_match == 0 and blue_match == 1:
        return "六等奖"
    else:
        return "未中奖"


print(check_prize([3, 8, 9, 12, 13, 15], 14))
print(check_prize([3, 7, 12, 21, 30, 33], 1))
print(check_prize([6, 13, 14, 19, 21, 28], 7))
print(check_prize([7, 9, 12, 13, 19, 24], 4))
print(check_prize([4, 7, 19, 26, 29, 31], 1))
