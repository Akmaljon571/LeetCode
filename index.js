var myAtoi = function (s) {
    let count = 0
    s = s.split(' ').join('')
    if (!Number(s[0] + 1))
        return 0
    for (let i = 0; i < s.length; i++) {
        if (Number(s[i] + 1))
            count += 1
        else
            break
    }
    return Number(s.slice(0, count))
};

console.log(myAtoi("5yftdftf56"))