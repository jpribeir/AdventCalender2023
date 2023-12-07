# Day 7 of the 2023 Advent of Code
class Hand():
    def __init__(self,hand,bet,score):
        self.hand = hand
        self.bet = int(bet)
        self.score = score

def giveScore(hand,joker):
    unique_dict = {each: 0 for each in set(list(hand))}
    score = 0
    # Calculate score
    for card in list(hand):
        unique_dict[card] += 1
        if unique_dict[card] == 2: score += 1
        elif unique_dict[card] > 2: score += 2
    # Check for jokers
    if joker and "J" in unique_dict.keys() and hand != "JJJJJ":
        max_count = 0
        for card in unique_dict:
            if unique_dict[card] > max_count and card != "J":
                max_count = unique_dict[card]
                max_card = card
        # Replace jokers for most common card and recalculate score
        new_hand = hand.replace("J",max_card)
        unique_dict = {each: 0 for each in set(list(new_hand))}
        score = 0
        for card in list(new_hand):
            unique_dict[card] += 1
            if unique_dict[card] == 2: score += 1
            elif unique_dict[card] > 2: score += 2
    return score

def compareHands(handA,handB):
    for card in range(len(handA)):
        if strength_dict[handA[card]] > strength_dict[handB[card]]: return True
        elif strength_dict[handA[card]] < strength_dict[handB[card]]: return False

def rankHands(joker):
    rank_dict = {}
    hand_count = 0
    for line in hand_list:
        hand,bet = line.split()[0],line.split()[1]
        score = giveScore(hand,joker)
        # Compare new hand with every ranked hand starting from the bottom
        for each in range(1,hand_count+1):
            # If it loses it found its rank
            if score < rank_dict[each].score:
                rank = each
                break
            # If it ties, compare each card starting from the first
            elif score == rank_dict[each].score:
                if compareHands(rank_dict[each].hand,hand):
                    rank = each
                    break
        # If no other hand beats it, get max rank
        else: rank = hand_count + 1
        # Update rest of the ranking table
        for x in range(hand_count+1,rank,-1): rank_dict[x] = rank_dict[x-1]
        rank_dict[rank] = Hand(hand,bet,score)
        hand_count += 1
    return sum(rank_dict[hand].bet*hand for hand in rank_dict)

# Read input file
with open("../include/input7.inc","r") as hand_file:
    hand_list = list(map(lambda a: a.strip(),hand_file.readlines()))

########################### Part 1 ###########################
strength_dict = {"2":0,"3":1,"4":2,"5":3,"6":4,"7":5,"8":6,"9":7,"T":8,"J":9,"Q":10,"K":11,"A":12}
print("Part1: %s"%rankHands(False))

########################### Part 2 ###########################
strength_dict = {"J":0,"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7,"9":8,"T":9,"Q":10,"K":11,"A":12}
print("Part2: %s"%rankHands(True))