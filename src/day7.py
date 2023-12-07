# Day 7 of the 2023 Advent of Code
class Hand():
    def __init__(self,hand,bet,score):
        self.hand = hand
        self.bet = int(bet)
        self.score = score
    def downGrade(self):
        self.rank += 1
    def calcResult(self):
        return self.bet*self.rank

def giveScore(hand,joker):
    unique_dict = {each: 0 for each in set(list(hand))}
    score = 0
    for card in list(hand):
        unique_dict[card] += 1
        if unique_dict[card] == 2: score += 1
        elif unique_dict[card] > 2: score += 2
    if joker and "J" in unique_dict.keys():
        max_count = 0
        for card in unique_dict:
            if unique_dict[card] > max_count and card != "J":
                max_score = unique_dict[card]
                max_card = card
        if max_count: score = 
    return score

def compareHands(handA,handB):
    for card in range(len(handA)):
        if strength_dict[handA[card]] > strength_dict[handB[card]]: return True
        elif strength_dict[handA[card]] < strength_dict[handB[card]]: return False

# Read input file
with open("../include/input7.inc","r") as hand_file:
    hand_list = list(map(lambda a: a.strip(),hand_file.readlines()))

########################### Part 1 ###########################
strength_dict = {"2":0,"3":1,"4":2,"5":3,"6":4,"7":5,"8":6,"9":7,"T":8,"J":9,"Q":10,"K":11,"A":12}
rank_dict = {}
hand_count = 0
rankFound = False
for i,line in enumerate(hand_list):
    hand,bet = line.split()[0],line.split()[1]
    score = giveScore(hand,False)
    for each in range(1,hand_count+1):
        if score < rank_dict[each].score:
            rank = each
            break
        elif score == rank_dict[each].score:
            if compareHands(rank_dict[each].hand,hand):
                rank = each
                break
    else: rank = hand_count + 1
    for x in range(hand_count+1,rank,-1): rank_dict[x] = rank_dict[x-1]
    rank_dict[rank] = Hand(hand,bet,score)
    hand_count +=1
result_sum = 0
for hand in rank_dict: result_sum += rank_dict[hand].bet*hand
print("Part1: %s"%result_sum)

########################### Part 2 ###########################
strength_dict = {"J":0,"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7,"9":8,"T":9,"Q":10,"K":11,"A":12}
rank_dict = {}
hand_count = 0
rankFound = False
for i,line in enumerate(hand_list):
    hand,bet = line.split()[0],line.split()[1]
    score = giveScore(hand,True)
    for each in range(1,hand_count+1):
        if score < rank_dict[each].score:
            rank = each
            break
        elif score == rank_dict[each].score:
            if compareHands(rank_dict[each].hand,hand):
                rank = each
                break
    else: rank = hand_count + 1
    for x in range(hand_count+1,rank,-1): rank_dict[x] = rank_dict[x-1]
    rank_dict[rank] = Hand(hand,bet,score)
    hand_count +=1
result_sum = 0
for hand in rank_dict: result_sum += rank_dict[hand].bet*hand
print("Part1: %s"%result_sum)