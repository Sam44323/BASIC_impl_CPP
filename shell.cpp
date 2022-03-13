#include <iostream>
#include "Core/basic.h"

using namespace std;

int main()
{
  while (true)
  {
    string text;
    cout << "basic > ";
    getline(cin, text);
    cin.clear();
    cout << text << endl;
  }
  return 0;
}