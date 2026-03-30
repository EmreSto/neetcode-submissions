class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char ,int> dict_s;
        unordered_map<char ,int> dict_t;
        for(int i =0; i< s.length();i++){
            dict_s[s[i]]++;
        }
        for(int j =0; j< t.length();j++){
            dict_t[t[j]]++;
        }
        if(dict_s == dict_t){
            return true;
        }
        else{
            return false;
        }
        
    }
};
