function findMissingAndRepeatedNumbers(nums: number[]): [number, number] {
    const seen = new Set<number>();
    let missing = -1;
    let repeated = -1;

    // FOR DUPLICATE
    for (const num of nums) {
        if (seen.has(num)) { //  has() method of a set to check if the set contains the specified entry. 
            repeated = num;
        } else {
            seen.add(num);
        }
    }

    // FOR MISSING
    for (let i = 1; i <= nums.length; i++) {
        if (!seen.has(i)) {
            missing = i;  // find idex of repeating element
            break;
        }
    }

    return [repeated, missing];
}

const nums = [3, 1, 2, 5, 5];
const [repeated, missing] = findMissingAndRepeatedNumbers(nums);
console.log("Repeated:", repeated);
console.log("Missing:", missing);

// TC: O(N)
// sC: O(N)
