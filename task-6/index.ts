function mergeIntervals(intervals: number[][]): number[][] {
    if (intervals.length <= 1) return intervals;

    // whether the intervals sorted  or  not
    intervals.sort((a, b) => a[0] - b[0]);

    const mergedIntervals: number[][] = [intervals[0]];

    for (let i = 1; i < intervals.length; i++) {
        const currentInterval = intervals[i];

        const lastMergedInterval = mergedIntervals[mergedIntervals.length - 1];

        if (currentInterval[0] <= lastMergedInterval[1]) {
            lastMergedInterval[1] = Math.max(currentInterval[1], lastMergedInterval[1]); // merge the interval
        } else {
            mergedIntervals.push(currentInterval); // add new interval
        }
    }

    return mergedIntervals;
}

const intervals = [[1, 3], [2, 6], [8, 10], [15, 18]];
const mergedIntervals = mergeIntervals(intervals);
console.log(mergedIntervals);

// Time Complexity: O(n log n), where n is the number of intervals, due to sorting.
// Space Complexity: O(n), where n is the number of intervals, to store the merged intervals.