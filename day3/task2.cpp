#include <fstream>
#include <iostream>
#include <regex>
#include <string>
#include <vector>
using namespace std;

int main(void) {
    ifstream file{"input.txt"};
    string text{istreambuf_iterator<char>{file}, istreambuf_iterator<char>{}};
    file.close();

    regex d{R"(do\(\)|don't\(\))"};
    vector<string> blocks{
        sregex_token_iterator{text.begin(), text.end(), d, -1},
        sregex_token_iterator{}};

    vector<string> delims{sregex_token_iterator{text.begin(), text.end(), d},
                          sregex_token_iterator{}};
    delims.insert(delims.begin(), "do()");

    regex mul{R"(mul\(\d{1,3},\d{1,3}\))"};
    vector<string> commands;
    for (size_t i = 0; i < blocks.size(); ++i) {
        if (delims[i] == "don't()")
            continue;

        commands.insert(
            commands.end(),
            sregex_token_iterator{blocks[i].begin(), blocks[i].end(), mul},
            sregex_token_iterator{});
    }

    int res{0};

    for (auto c : commands) {
        string left{string(c.begin() + 4, c.begin() + c.find(','))};
        string right{string(c.begin() + c.find(',') + 1, c.end() - 1)};
        res += stoi(left) * stoi(right);
    }

    cout << res << '\n';

    return 0;
}
