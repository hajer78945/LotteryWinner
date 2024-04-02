# 定义本期中奖号码
winning_numbers = {"red": {5, 7, 14, 17, 22, 32}, "blue": 6}

# 定义用户投注号码
bets = [
    {"red": {6, 11, 15, 22, 25, 27}, "blue": 10}, #6+1
    {"red": {10, 13, 18, 20, 23, 25}, "blue": 10}, #6+1
    {"red": {10, 14, 17, 20, 22, 33}, "blue": 10}, #6+1
    {"red": {1, 11, 13, 17, 24, 31}, "blue": 7}, #6+1
    {"red": {8, 10, 13, 15, 21, 23}, "blue": 6}, #6+1

]

# 定义各等奖的中奖条件（红球匹配数量，蓝球是否匹配）和奖金（仅示例，实际奖金会变动）
prize_conditions = {
    (6, True): ("一等奖", "保底五百万！！！"),
    (6, False): ("二等奖", "一百万！！！（保底6000）"),
    (5, True): ("三等奖", 3000),  # 示例金额
    (5, False): ("四等奖", 200),   # 示例金额
    (4, True): ("四等奖", 200),   # 示例金额
    (4, False): ("五等奖", 10),    # 示例金额
    (3, True): ("五等奖", 10),    # 示例金额
    (2, True): ("六等奖", 5),     # 示例金额
    (1, True): ("六等奖", 5),     # 示例金额
    (0, True): ("六等奖", 5),     # 示例金额
}

# 使用之前的代码计算中奖情况
results = []
for bet in bets:
    red_match = len(winning_numbers["red"].intersection(bet["red"]))
    blue_match = winning_numbers["blue"] == bet["blue"]
    results.append((red_match, blue_match))

# 判断中奖等级和奖金
for index, (red_match, blue_match) in enumerate(results, start=1):
    prize_info = prize_conditions.get((red_match, blue_match), ("未中奖", 0))
    print(f"投注号码【{index}】: 匹配(红)球 {red_match} 个, (蓝)球匹配: {'是' if blue_match else '否'}。|| 中奖情况: {prize_info[0]}, 奖金: {prize_info[1]}")


