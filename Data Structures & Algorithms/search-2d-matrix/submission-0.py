class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        '''

        this is just double binary search, we search for our array and then we search based off of that



        '''

        l = 0
        r = len(matrix) - 1



        while l <= r:
            mid = (l + r) // 2 


            if matrix[mid][0] <= target <= matrix[mid][-1]:

                left = 0
                right = len(matrix[mid]) - 1

                while left <= right:
                    middle = (left + right) // 2

                    if matrix[mid][middle] == target:
                        return True

                    if matrix[mid][middle] > target:
                        right = middle - 1

                    else:
                        left = middle + 1




            if matrix[mid][0] > target:
                r = mid - 1

            else:
                l = mid + 1



        return False


        