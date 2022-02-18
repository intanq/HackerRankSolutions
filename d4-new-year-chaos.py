#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
        #
    # initialize the number of moves
    moves = 0 
    #
    # decrease Q by 1 to make index-matching more intuitive
    # so that our values go from 0 to N-1, just like our
    # indices.  (Not necessary but makes it easier to
    # understand.)
    q = [P-1 for P in q]
    #
    # Loop through each person (P) in the queue (Q)
    for i,P in enumerate(q):
        # i is the current position of P, while P is the
        # original position of P.
        #
        # First check if any P is more than two ahead of 
        # its original position
        if P - i > 2:
            print("Too chaotic")
            return
        #
        # From here on out, we don't care if P has moved
        # forwards, it is better to count how many times
        # P has RECEIVED a bribe, by looking at who is
        # ahead of P.  P's original position is the value
        # of P.
        # Anyone who bribed P cannot get to higher than
        # one position in front if P's original position,
        # so we need to look from one position in front
        # of P's original position to one in front of P's
        # current position, and see how many of those 
        # positions in Q contain a number large than P.
        # In other words we will look from P-1 to i-1,
        # which in Python is range(P-1,i-1+1), or simply
        # range(P-1,i).  To make sure we don't try an
        # index less than zero, replace P-1 with
        # max(P-1,0)
        for j in range(max(P-1,0),i):
            if q[j] > P:
                moves += 1
    print(moves)
    
    # # 60% SCORE 
    
    # sorted_q = [] + q
    # sorted_q.sort()
    # num_of_bribes = 0
    # chaotic = False
    
    # for person in q:
    #     given_index = q.index(person)
    #     real_position = sorted_q.index(person)
    #     if real_position - given_index > 2:
    #         chaotic = True
    #         break
        
    #     if given_index < real_position:
    #         num_of_bribes += (real_position - given_index)
    #     else:
    #         for i in range(given_index+1, len(q)):
    #             if person > q[i]:
    #                 num_of_bribes += 1
    # if chaotic:
    #     print("Too chaotic")
    # else:
    #     print(num_of_bribes)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

