class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(B) < len(A):
            A,B = B, A

        total = len(A) + len(B)
        half = total // 2
        l = 0
        r = len(A) - 1
        while True:
            i = l + (r - l) // 2 # mid of smaller array
            j = half - i - 2 # leftover from smaller array to fill out mid


            Aleft = A[i] if i >= 0 else float("-infinity") 
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright: # valid median boundaries
                if total % 2 != 0: # odd
                    return min(Aright,Bright)
                else: # even
                    return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

