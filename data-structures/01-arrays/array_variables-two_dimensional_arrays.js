let names = [
  ["John", "Jane", "Jack", "Jill", "Jenny", "Jerry"],
  ["Blue", "Black", "Cat", "Marik", "Joel", "Doe"],
];


function linear_search(arr, item) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      if (arr[i][j] === item) {
        return [i, j];
      }
    }
  }
  return -1;  // if the item is not found
}

console.log(linear_search(names, "Jill")); // [0, 3]