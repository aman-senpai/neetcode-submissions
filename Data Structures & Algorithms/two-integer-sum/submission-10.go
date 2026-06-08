func twoSum(nums []int, target int) []int {    
    var res []int
    for i, n := range nums {
        for j := i + 1; j < len(nums); j++ {
            if n + nums[j] == target {
                res = append(res, i)
                res = append(res, j)
                return res
            }
        }
    }
    return res
}