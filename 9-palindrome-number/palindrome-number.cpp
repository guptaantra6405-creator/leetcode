class Solution {
public:
    bool isPalindrome(int x) {
        if(x<0) return false;
        int original = x;
        long rev_x=0;
        while(x!=0){
            rev_x=rev_x*10 + x%10;
            x=x/10;
        }return original==rev_x;
    }
};