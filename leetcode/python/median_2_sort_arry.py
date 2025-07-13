# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

a = [1,2,3]
b = [2,3]


# median 
"""
[1,2,3]
if odd:
     arr[len()/2]
else:
    (arr[int(len()/2)] + arr[len()/2 + 1]) / 2
"""

def median(nums1, nums2):
    nums1 = sorted(nums1+nums2)
    print(nums1)
    mid_ix = int(len(nums1)/2)
    if len(nums1) % 2 == 1:
        return nums1[mid_ix]
    else:
        mid_ix -=1
        print(mid_ix, len(nums1)/2)
        return (nums1[mid_ix] + nums1[mid_ix + 1]) / 2

a = [1,2]
b = [3,4]
print(median(a,b))

a = [1,3]
b = [2]
print(median(a,b))

a = [2,2,4,4]
b = [2,2,2,4,4]
print(median(a,b))