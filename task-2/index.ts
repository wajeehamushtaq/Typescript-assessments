function sortedArray(arr: number[]): void{
    let low = 0
    let mid = 0
    let high = arr.length - 1

    while(mid <= high){
        if(arr[mid] === 0){
            [arr[low], arr[mid]] = [arr[mid], arr[low]]
            low++
            mid++
        } else if(arr[mid] === 1){
            mid++
        }  else if(arr[mid] === 2){
            [arr[mid], arr[high]] = [arr[high], arr[mid]]
            high--
        }
    }
}

const arr: number[] = [1,0,0,1,2,1,1,2]
sortedArray(arr)
console.log(arr)