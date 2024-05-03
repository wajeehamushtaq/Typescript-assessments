function mergeSortedArraysSameLength(arr1: number[], arr2: number[]): void {
    let m: number = arr1.length;
    let n: number = arr2.length;

    for (let i = 0; i < m; i++) {
        if (arr1[i] > arr2[0]) {
            // Swap elements
            let temp = arr1[i];
            arr1[i] = arr2[0];
            arr2[0] = temp;

            // Sort arr2 to maintain the order
            let firstElement = arr2[0];
            let k;
            for (k = 1; k < n && arr2[k] < firstElement; k++) {
                arr2[k - 1] = arr2[k]; // insertion  sort
            }
            arr2[k - 1] = firstElement;
        }
    }
}

// Test cases
let arr1: number[] = [10];
let arr2: number[] = [2, 3];
mergeSortedArraysSameLength(arr1, arr2);
console.log(arr1, arr2);

arr1 = [10, 4, 5];
arr2 = [2, 3];
mergeSortedArraysSameLength(arr1, arr2);
console.log(arr1, arr2);

//  TC = O(N*M)
//  SC = O(1)
