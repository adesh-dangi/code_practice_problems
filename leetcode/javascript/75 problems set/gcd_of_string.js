function gcd(a, b) {
    while (b !== 0) {
        [a, b] = [b, a % b];
    }
    return a;
}
function gcdOfStrings(str1, str2) {
    var leng;
    if (str1+str2!==str2+str1){return ""}
    leng = gcd(str1.length, str2.length);
    return str1.slice(0,leng);
};
console.log(gcd("abcabc","abc"))