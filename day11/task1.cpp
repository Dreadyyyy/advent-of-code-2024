#include <bits/stdc++.h>
using namespace std;

size_t length_after(size_t num, size_t blinks_left,
                    unordered_map<string, size_t> &memo) {
    string key = to_string(num) + ";" + to_string(blinks_left);
    if (memo.count(key) == 1) {
        return memo[key];
    }

    size_t res;
    string str_num{to_string(num)};
    if (blinks_left == 0) {
        res = 1;
    } else if (num == 0) {
        res = length_after(1, blinks_left - 1, memo);
    } else if (str_num.length() % 2 == 0) {
        size_t left, right;
        istringstream{string{str_num.begin(),
                             str_num.begin() + (str_num.length() / 2)}} >>
            left;
        istringstream{
            string{str_num.begin() + (str_num.length() / 2), str_num.end()}} >>
            right;
        res = length_after(left, blinks_left - 1, memo) +
              length_after(right, blinks_left - 1, memo);
    } else {
        res = length_after(num * 2024, blinks_left - 1, memo);
    }

    memo[key] = res;
    return res;
}

int main(void) {
    ifstream file{"input.txt"};
    istringstream is{
        string{istreambuf_iterator<char>{file}, istreambuf_iterator<char>{}}};
    file.close();

    int curr;
    vector<size_t> list;
    while (is >> curr) {
        list.push_back(curr);
    }

    size_t res = 0;
    unordered_map<string, size_t> memo;
    for (auto x : list) {
        res += length_after(x, 25, memo);
    }
    cout << res << '\n';

    return 0;
}
