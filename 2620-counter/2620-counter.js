/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    count = -1
    return function() {
        count += 1
        return n + count
        
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */