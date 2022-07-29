from readline import set_pre_input_hook
from sys import setprofile


process of insertion sort
 [22,27,16,2,18,6]
 [2,27,16,22,18,6]
 [2,6,16,22,18,27]
 [2,6,16,18,22,27]

big O notation: O(n^2)

Time Complexity : 
Average case : the number we are looking for is in the middle
Worst case : the number we are looking for is at the end
Best case : the number we are looking for is in the beginning

for 18 -> average case

[7,3,5,8,2,9,4,15,6] write first 4 step
[2,3,5,8,7,9,4,15,6]
[2,3,4,8,7,9,5,15,6]
[2,3,4,5,7,9,8,15,6]
[2,3,4,5,6,9,8,15,7]