#include <bits/stdc++.h>
using namespace std;

bool check(const vector<string> &matr, int x, int y, int i, int j,
           string word) {
    size_t curr{0};
    while (curr < word.length() && x == clamp(x, 0, (int)matr.size() - 1) &&
           y == clamp(y, 0, (int)matr[0].length())) {
        if (word[curr] != matr[x][y])
            break;
        x += i;
        y += j;
        ++curr;
    }
    return word.length() == curr;
}

int main(void) {
    vector<string> lines;
    string line;
    ifstream file{"input.txt"};
    while (file >> line)
        lines.push_back(line);
    file.close();

    namespace views = ranges::views;
    auto rng_x = views::iota(0, (int)lines.size());
    auto rng_y = views::iota(0, (int)lines[0].size());
    auto rng_i = views::iota(-1, 2);
    auto rng_j = views::iota(-1, 2);
    auto cartesian = views::cartesian_product(rng_x, rng_y, rng_i, rng_j);
    auto filtered = cartesian | views::filter([](const auto &tpl) {
                        auto [_, _, i, j] = tpl;
                        return i || j;
                    });
    auto transformed = views::transform(filtered, [&lines](const auto &tpl) {
        auto [x, y, i, j] = tpl;
        return check(lines, x, y, i, j, "XMAS");
    });
    int res{accumulate(transformed.begin(), transformed.end(), 0)};

    cout << res << '\n';
    return 0;
}
