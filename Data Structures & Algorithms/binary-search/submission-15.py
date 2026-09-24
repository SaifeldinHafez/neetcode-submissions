class Solution:
    def search(self, nums: List[int], target: int) -> int:

        upper_bound = (len(nums) - 1)
        lower_bound = 0

        if target == nums[upper_bound]:
            return upper_bound
        elif target == nums[lower_bound]:
            return lower_bound

        for i in range(0, math.ceil(math.log2(len(nums)) + 1)):

            print(f"The lower bound is at {nums[lower_bound]} and the upper bound is at {nums[upper_bound]}")
            pointer = math.ceil((upper_bound + lower_bound) / 2)
            print(f"PASS {i + 1} \n the pointer is at {nums[pointer]}")

            if nums[pointer] == target:
                print(f"The target is found at index {pointer} and it is {nums[pointer]}")
                return pointer
                break
            elif target > nums[pointer]:
                lower_bound = pointer 
                print(f"the target is larger")
            elif target < nums[pointer]:
                upper_bound = pointer
                print(f"the target is smaller")
        
        return -1