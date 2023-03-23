// 팰린드롬
#include <iostream>
#include <vector>
using namespace std;
bool sees(string word)
{
    int j = 0;
    for (int i = 0; i < word.length() / 2; i++)
    {
        if (word[i] != word[word.length() - i - 1])
        {
            j++;
        }
    }

    if (j == 0)
        return true;
    else
        return false;
}

int main()
{
    string i;
    while (1)
    {
        cin >> i;
        // 검사
        if (i == "0")
            break;
        else if (sees(i) == true)
            cout << "yes" << endl;
        else if (sees(i) == false)
            cout << "no" << endl;
    }
}