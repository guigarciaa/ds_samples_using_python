let names = ['Alice', 'Bob', 'Tiff', 'Bruce', 'Alice'];

function linear_search(arr, item) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === item) {
            return i;
        }
    }
    return -1;  // if the item is not found
}

console.log(linear_search(names, 'Bruce')); // 3