function isPrime(x) {
  if (x > 2) {
    for (var i = 2; i <= x-1; i++) {
      if (x % i === 0) {
        return false;
      }
    }
    return true;
  }
  else {
    return false;
  }
}

console.log(isPrime(13));