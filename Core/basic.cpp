/*
            TOKENS
-----------------------------
*/
#include <iostream>
#include <string>
#define TT_INT = 'INT'
#define TT_FLOAT = 'FLOAT'
#define TT_PLUS = 'PLUS'
#define TT_MINUS = 'MINUS'
#define TT_MUL = 'MUL'
#define TT_DIV = 'DIV'
#define TT_LPAREN = 'LPAREN'
#define TT_RPAREN = 'RPAREN'

using namespace std;

class Token
{
private:
  string type;
  string value;

public:
  Token(string &type, string &value)
  {
    this->type = type;
    this->value = value;
  }

  void print()
  {
    if (this->value != "")
    {
      cout << "Token: " << this->type << " Value: " << this->value << endl;
    }
    else
    {
      cout << "Token: " << this->type << endl;
    }
  }
};