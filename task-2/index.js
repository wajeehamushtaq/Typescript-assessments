function sortedArray(arr) {
    var _a, _b;
    var low = 0;
    var mid = 0;
    var high = arr.length - 1;
    while (mid <= high) {
        if (arr[mid] === 0) {
            _a = [arr[mid], arr[low]], arr[low] = _a[0], arr[mid] = _a[1];
            low++;
            mid++;
        }
        else if (arr[mid] === 1) {
            mid++;
        }
        else if (arr[mid] === 2) {
            _b = [arr[high], arr[mid]], arr[mid] = _b[0], arr[high] = _b[1];
            high--;
        }
    }
}
var arr = [1, 0, 0, 1, 2, 1, 1, 2];
sortedArray(arr);
console.log(arr);
