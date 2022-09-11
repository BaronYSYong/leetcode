"""
Initially, there is a Robot at position (0, 0). 
Given a sequence of its moves, judge if this robot makes a circle, 
which means it moves back to the original place.

The move sequence is represented by a string. 
And each move is represent by a character. 
The valid robot moves are R (Right), L (Left), U (Up) and D (down). 
The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true

Example 2:
Input: "LL"
Output: false
"""
class Solution(object):
    def judgeCircle1(self, moves):
        """
        :type moves: str
        :rtype: bool
        time: 172
        """
        pos = [0,0]
        for move in moves:
            if move == 'U':
                pos[1] += 1
            elif move == 'D':
                pos[1] -= 1
            elif move == 'L':
                pos[0] -= 1
            elif move == 'R':
                pos[0] += 1
        if pos == [0,0]:
            return True
        else:
            return False

    def judgeCircle2(self, moves):
        """
        :type moves: str
        :rtype: bool
        time: 39 ms
        """
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

    def judgeCircle3(self, moves):
        """
        :type moves: str
        :rtype: bool
        time: 125 ms
        """
        direct = {'U': 1, 'D': -1, 'L': 1j, 'R': -1j}
        return 0 == sum(direct[m] for m in moves)

    def judgeCircle4(self, moves):
        """
        :type moves: str
        :rtype: bool
        time: 116 ms
        """
        return not sum(map({'U': 1, 'D': -1, 'L': 1j, 'R': -1j}.get, moves))

    def judgeCircle5(self, moves):
        """
        :type moves: str
        :rtype: bool
        time: 198 ms
        """        
        return not sum(1j**'RUL'.find(m) for m in moves)

if __name__ == '__main__':
    jc = Solution()
    moves = "UUDDLLRUD"
    print jc.judgeCircle1(moves)
    print jc.judgeCircle2(moves)
    print jc.judgeCircle3(moves)
    print jc.judgeCircle4(moves)
    print jc.judgeCircle5(moves)
