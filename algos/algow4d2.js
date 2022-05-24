function fibonacci(n) {

    if (n <= 0) {
        return 0;
    }

    if (n == 1) {
        return 1;
    }

    return fibonacci(n - 1) + fibonacci(n - 2);
}

// Memo-ization

function fibonacci(n, memo = {}) {
    // default parameter

    if (n <= 0) {
        return 0;
    }

    if (n == 1) {
        return 1;
    }
    else {
        if (memo[n] != undefined) {
            return memo[n];
        } else {
            let x = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
            memo[n] = x;
            return x;
        }
    }
}