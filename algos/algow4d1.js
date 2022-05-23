function recursiveFactorial(input) {
    if (input <= 1) {
        return 1;
    }

    return input * recursiveFactorial(input - 1);
}