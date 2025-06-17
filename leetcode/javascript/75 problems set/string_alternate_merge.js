/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */

function print(...args){
    console.log(args);
}

var mergeAlternately = function(word1, word2) {
    [min_len, max_word] = word1.length > word2.length ? [word2.length, word1] : [word1.length, word2];
    var op = "";
    for(var i = 0; i < min_len; i++){
        op += word1[i] + word2[i];
    }
    return op + max_word.slice(min_len);
};

mergeAlternately("abc","xy")