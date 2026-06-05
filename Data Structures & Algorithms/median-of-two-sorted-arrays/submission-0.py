class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_array = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sorted_array.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                sorted_array.append(nums2[j])
                j += 1
            else:
                sorted_array.append(nums1[i])
                sorted_array.append(nums2[j])
                i += 1
                j += 1
        sorted_array.extend(nums1[i:])
        sorted_array.extend(nums2[j:])
        if len(sorted_array) % 2 == 0:
            mid_ele = len(sorted_array)//2
            return (sorted_array[mid_ele] + sorted_array[mid_ele - 1])/2
        else:
            mid_ele = len(sorted_array)//2
            return sorted_array[mid_ele]
