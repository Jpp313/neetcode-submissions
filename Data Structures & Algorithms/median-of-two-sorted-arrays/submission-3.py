class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        if len(B) < len(A): # make sure A is always smaller
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2
        l = 0
        r = len(A) - 1
        while True:
            i = l + (r - l) // 2
            j = half - i - 2 # easy way to find amt in bigger portion

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # valid partition
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 != 0: # odd
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft) + min(Bright,Aright)) / 2
            elif Aleft > Bright:
                r = i - 1
            elif Bleft > Aright:
                l = i + 1
            