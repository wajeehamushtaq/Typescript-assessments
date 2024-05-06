const nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
const maxSum = maxSubArray(nums);
console.log("Maximum contiguous sum:", maxSum);

function maxSubArray(nums: number[]): number {
    if(nums.length === 0 ) return 0

    let maxEnding = nums[0]
    let resultMax = nums[0]

    for(let i = 1; i < nums.length; i++){
        maxEnding = Math.max(nums[i], maxEnding + nums[i])
        resultMax = Math.max(resultMax, maxEnding)
    }

    return resultMax
}

// TC: O(N)
// SC: O(1)