// 1461. Check If a String Contains All Binary Codes of Size K

// Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

 
// Example 1:

// Input: s = "00110110", k = 2
// Output: true
// Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
// Example 2:

// Input: s = "0110", k = 1
// Output: true
// Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring. 
// Example 3:

// Input: s = "0110", k = 2
// Output: false
// Explanation: The binary code "00" is of length 2 and does not exist in the array.

class Solution {
public:
    bool hasAllCodes(string s, int k) {
        
        set<string> all_substrings;
        int total = 1 <<k; // this is equal to 2 power k (2^k)

        // get all the substring of len k and store it in a set
        for(int i =0;i+k<=s.length();i++){
            all_substrings.insert(s.substr(i,k));
            // size of set equals 2 power k
            if (all_substrings.size() == total){
                return true;
            }
        }
        
        return false;
    }
};
