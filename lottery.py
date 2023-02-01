#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__date__ = '2023/1/30'

def check_prize(winning_red_balls, winning_blue_ball, red_balls, blue_ball):
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
        print("一等奖")
    elif red_match == 6:
        print( "二等奖")
    elif red_match == 5 and blue_match == 1:
        print("二等奖")
    elif red_match == 5 or (red_match == 4 and blue_match == 1):
        print("四等奖")
    elif red_match == 4 or (red_match == 3 and blue_match == 1):
        print("五等奖")
    elif red_match == 2 and blue_match == 1 or red_match == 1 and blue_match == 1 or red_match == 0 and blue_match == 1:
        print("六等奖")
    else:
        print("未中奖")

if __name__ == '__main__':
    print(f"请参考 http://kaijiang.500.com/shtml/dlt/23009.shtml?0_ala_baidu 中的开奖号码, 进行输入对比")
    winning_red_balls = [int(x) for x in input("请输入开奖红球号码，用空格隔开：").split()]
    winning_blue_ball = int(input("请输入开奖蓝球号码："))

    while True:
        print(f"")
        red_balls = [int(x) for x in input("请输入红球号码，用空格隔开(直接回车退出)：").split()]
        if red_balls is None:
            break
        blue_ball = int(input("请输入蓝球号码："))
        check_prize(winning_red_balls, winning_blue_ball, red_balls, blue_ball)
