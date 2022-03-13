/*
-----------------------------
            CONSTANTS
-----------------------------
*/

const string DIGITS = "0123456789.";

const string TT_INT = "INT", TT_FLOAT = "FLOAT", TT_PLUS = "PLUS", TT_MINUS = "MINUS", TT_MUL = "MUL", TT_DIV = "DIV", TT_LPAREN = "LPAREN", TT_RPAREN = "RPAREN";

/*
-----------------------------
            TOKENS
-----------------------------
*/
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// creating the class for the token

namespace TokenName
{

  class Token
  {
  private:
    string type;
    string value;

  public:
    Token(string type, string value)
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
};

/*
-----------------------------
            LEXER (for converting the streams to tokens)
-----------------------------
*/

// creating the class for the lexer

namespace LexerName
{

  class Lexer
  {
  private:
    string text;
    int currentPos;
    char currChar;

  public:
    Lexer(string &text)
    {
      this->text = text; // text that we need to convert to tokens
      this->currentPos = -1;
      this->currChar = '\0';
      this->advance();
    }

    // for traversing over the text
    void advance()
    {
      this->currentPos++;
      if (this->currentPos < this->text.length())
      {
        this->currChar = this->text[this->currentPos];
      }
      else
      {
        this->currChar = '\0';
      }
    }

    // method for making the tokens
    void makeTokens()
    {
      std::vector<TokenName::Token> tokens;

      while (this->currChar != '\0')
      {
        if (this->currChar == '\t' || this->currChar == ' ')
          this->advance();
        else if (this->currChar == '+')
          tokens.push_back(TokenName::Token(TT_PLUS, "+"));
        else if (this->currChar == '-')
        {
          tokens.push_back(TokenName::Token(TT_MINUS, "-"));
          this->advance();
        }
        else if (this->currChar == '*')
        {
          tokens.push_back(TokenName::Token(TT_MUL, "*"));
          this->advance();
        }
        else if (this->currChar == '/')
        {
          tokens.push_back(TokenName::Token(TT_DIV, "/"));
          this->advance();
        }
        else if (this->currChar == '(')
        {
          tokens.push_back(TokenName::Token(TT_LPAREN, "("));
          this->advance();
        }
        else if (this->currChar == ')')
        {
          tokens.push_back(TokenName::Token(TT_RPAREN, ")"));
          this->advance();
        }
        else if (this->currChar == '(')
        {
          tokens.push_back(TokenName::Token(TT_LPAREN, "("));
          this->advance();
        }
        else if (DIGITS.find(this->currChar) != string::npos)
        {
          tokens.push_back(this->numberResolver());
          this->advance();
        }
      }
    }

    TokenName::Token numberResolver()
    {
      string num_str = "";
      int dot_count = 0;

      while (this->currChar != '\0' && DIGITS.find(this->currChar) != string::npos)
      {
        if (this->currChar == '.')
        {
          if (dot_count == 1)
            break;
          num_str += '.';
          dot_count++;
        }
        else
        {
          num_str += this->currChar;
        }
        this->advance();
      }

      if (dot_count == 0)
        return TokenName::Token(TT_INT, num_str);
      else
        return TokenName::Token(TT_FLOAT, num_str);
    }
  };
}