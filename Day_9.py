# (leetcode) 1: Palindrome
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers or numbers ending in 0 (but not 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even digits: x == reversed_half
        # For odd digits: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10

#Example
x = 121
reversed_half = 0

Step 1: reversed_half = 1, x = 12
Step 2: reversed_half = 12, x = 1

Now x <= reversed_half → stop

Compare:
x == reversed_half // 10 → 1 == 1 → True

# (leetcode) 2: Find the Richest Costomer
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(customer) for customer in accounts)


#Example
Input accounts =
[[1,2,3],[3,2,1]]
Output
6
Expected
6

# (HakerRank) 3: Stair Case

def staircase(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        hashes = "#" * i
        print(spaces + hashes)

# Input
n = int(input().strip())
staircase(n)

#Example
Input (stdin)
6
Your Output (stdout)
     #
    ##
   ###
  ####
 #####
######
Expected Output
     #
    ##
   ###
  ####
 #####
######

# (HakerRank) 4: Min-Max Sum
def miniMaxSum(arr):
    total = sum(arr)
    min_val = min(arr)
    max_val = max(arr)
    
    min_sum = total - max_val
    max_sum = total - min_val
    
    print(min_sum, max_sum)

# Input
arr = list(map(int, input().split()))
miniMaxSum(arr)

#Example
Input (stdin)
1 2 3 4 5
Your Output (stdout)
10 14
Expected Output
10 14


# (HakerRank) 5: Birthday Cake Candles
def birthdayCakeCandles(candles):
    # Write your code here
    max_val = max(candles)
    return candles.count(max_val)

#Example
Input (stdin)
4
3 2 1 3
Your Output (stdout)
2
Expected Output
2

# (HakerRank) 6: Time Conversion
def timeConversion(s):
    # Get the AM/PM part (last two characters)
    meridiem = s[-2:]
    # Get the hour part (first two characters)
    hour = int(s[:2])
    # Get the middle part (minutes and seconds)
    time_rest = s[2:-2]
    
    if meridiem == "AM":
        if hour == 12:
            hour = 0
    else: # It's PM
        if hour != 12:
            hour += 12
            
    # Format the hour back to two digits and join
    return f"{hour:02}{time_rest}"

#Example
Input (stdin)
07:05:45PM
Your Output (stdout)
19:05:45
Expected Output
19:05:45
