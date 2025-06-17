
function gcd(num1, num2){
    while (num2!=0){
        [num1, num2] = [num2, num1%num2]
    }
    return num1
}

function gcdOfStrings(str1: string, str2: string): string {
    var leng;
    if (str1+str2!==str2+str1){return ""}
    leng = gcd(str1.length, str2.length);
    return str1.slice(0,leng);
};