class Solution {
public:
    bool isPalindrome(string s) {
        string new_str="";
        string rev_str="";
        for(int i = 0; i < s.length(); i++){
            if(isalnum(s[i])){
                new_str += tolower(s[i]);
            }
        }
        for(int j =new_str.length()-1; j >= 0;j--){
            rev_str += new_str[j];
        }
        if(new_str == rev_str){
            return true;
        }
        else{
            return false;
        }
    }
};
