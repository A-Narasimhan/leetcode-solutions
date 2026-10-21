class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = j = 0
        res = []
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        res.extend(nums1[i:m])
        res.extend(nums2[j:n])
        nums1[:]=res