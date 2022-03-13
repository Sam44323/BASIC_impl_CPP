/*
-----------------------------
            TOKENS
-----------------------------
*/
#include <iostream>
#include <string>
#define TT_INT = 'INT'       // integer
#define TT_FLOAT = 'FLOAT'   // float
#define TT_PLUS = 'PLUS'     // plus
#define TT_MINUS = 'MINUS'   // minus
#define TT_MUL = 'MUL'       // multiply
#define TT_DIV = 'DIV'       // division
#define TT_LPAREN = 'LPAREN' // left-parenthesis
#define TT_RPAREN = 'RPAREN' // right-parenthesis

using namespace std;

// creating the class for the token

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

/*
-----------------------------
            LEXER (for converting the streams to tokens)
-----------------------------
*/

// creating the class for the lexer

class Lexer
{
private:
  string text;

public:
  Lexer(string &text)
  {
    this->text = text; // text that we need to convert to tokens
  }
};