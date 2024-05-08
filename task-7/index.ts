function countInversions(arr: number[]): number {
    let count = 0;

    const mergeSort = (arr: number[]): number[] => {
        if (arr.length <= 1) {
            return arr;
        }

        const mid = Math.floor(arr.length / 2);
        const left = mergeSort(arr.slice(0, mid));
        const right = mergeSort(arr.slice(mid));

        return merge(left, right);
    };

    const merge = (left: number[], right: number[]): number[] => {
        let merged: number[] = [];
        let i = 0;
        let j = 0;

        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                merged.push(left[i]);
                i++;
            } else {
                // If arr[i] > arr[j], it's an inversion
                merged.push(right[j]);
                j++;
                count += left.length - i; // Increment count by remaining elements in left
            }
        }

        merged = merged.concat(left.slice(i)).concat(right.slice(j));
        return merged;
    };

    mergeSort(arr);
    return count;
}

const arr = [8, 4, 2, 1];
const inversions = countInversions(arr);
console.log("Number of inversions:", inversions);

// Time Complexity: O(n log n) - where n is the size of the array, due to the merge sort algorithm.
// Space Complexity: O(n) - additional space is used for merging arrays during the merge step.