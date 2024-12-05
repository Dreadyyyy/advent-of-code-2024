#include <bits/stdc++.h>
using namespace std;

int main(void) {
    unordered_map<string, int> cmp;
    string line{"|"};

    ifstream file{"input.txt"};

    while (line.find('|') != string::npos) {
        cmp[line] = true;
        cmp[string{line.begin() + line.find('|') + 1, line.end()} + "|" +
            string{line.begin(), line.begin() + line.find('|')}] = false;
        file >> line;
    }

    vector<vector<string>> updates;
    while (file >> line) {
        stringstream ss(line);
        vector<string> v;
        while (ss.good()) {
            string substr;
            getline(ss, substr, ',');
            v.push_back(substr);
        }
        updates.push_back(v);
    }
    file.close();

    int res{0};
    for (auto u : updates) {
        vector<string> su = u;
        sort(su.begin(), su.end(),
             [&cmp](auto x, auto y) { return cmp[x + "|" + y]; });
        if (su != u)
            res += stoi(su[su.size() / 2]);
    }

    cout << res << '\n';

    return 0;
}
