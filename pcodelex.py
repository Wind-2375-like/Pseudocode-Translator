import re
import sys

import ply.lex as lex
from ply.lex import TOKEN

class pcodeLexer:
    """ A lexer for the C language. After building it, set the
        input text with input(), and call token() to get new
        tokens.
    """
    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
    
    # Test it output
    def test(self, data):
        self.lexer.input(data)
        for tok in self.lexer:
            print(tok)

    ##
    ## Reserved keywords
    ##
    keywords = {
        'if'      : 'IF',
        'else'    : 'ELSE', 
        'while'   : 'WHILE',
        'for'     : 'FOR',
        'break'   : 'BREAK',
        'continue': 'CONTINUE',
        'return'  : 'RETURN',
        'int'     : 'INT',
        'float'   : 'FLOAT',
        'string'  : 'STRING',
        'const'   : 'CONST',
        'bool'    : 'BOOL',
        'and'     : 'AND',
        'not'     : 'NOT',
        'or'      : 'OR',           # 有问题
        'true'    : 'TRUE',         # 有问题
        'True'    : 'TRUE',
        'false'   : 'FALSE',
        'False'   : 'FALSE',
        'to'      : 'TO',
        'by'      : 'BY',
        'char'    : 'CHAR',
        'main'    : 'MAIN',
        'swap'    : 'SWAP',
    }

    ##
    ## All the tokens recognized by the lexer
    ##
    tokens = list(keywords.values()) + [
        # Identifiers
        'ID',

        # Constants
        'INT_CONST_DEC', 'FLOAT_CONST_DEC', 'STRING_CONST',

        # Operators
        'NE', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
        'LT', 'LE', 'GT', 'GE', 'EQ', 

        # Assignment
        'EQUAL', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL',
        'PLUSEQUAL', 'MINUSEQUAL',

        # Increment/decrement
        'PLUSPLUS', 'MINUSMINUS',

        # Delimeters
        'LPAREN', 'RPAREN',         # ( )
        'LBRACKET', 'RBRACKET',     # [ ]
        'LBRACE', 'RBRACE',         # { }
        'COMMA', 'PERIOD',          # , .
        'SEMI', 'COLON'            # ; :
    ]

    ##
    ## Rules for the normal state
    ##

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Discard comments
    def t_COMMENT(self, t):
        r'(\/\/|\#).*'
        pass
        # No return value. Token discarded

    # Identifiers
    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.keywords.get(t.value,'ID')    # Check for reserved words
        return t

    # Constants
    t_FLOAT_CONST_DEC           = r'\d+\.\d+'
    t_INT_CONST_DEC             = r'\d+'
    t_STRING_CONST              = r'("|\').*("|\')'

    # Operators
    t_LE                        = r'<='
    t_GE                        = r'>='
    t_EQ                        = r'=='
    t_NE                        = r'!='
    t_LT                        = r'<'
    t_GT                        = r'>'
    t_PLUS                      = r'\+'
    t_MINUS                     = r'\-'
    t_TIMES                     = r'\*'
    t_DIVIDE                    = r'/'
    t_MOD                       = r'%'
    t_OR                        = r'\|\|'      
    t_AND                       = r'&&'
    t_NOT                       = r'!'

    # t_BI_BOOL_OP                = r'(\|\|)|(&&)|(>=)|(<=)|(==)|(!=)|(<)|(>)'
    # t_MON_BOOL_OP               = r'!'

    # Assignments
    t_EQUAL                    = r'='
    t_TIMESEQUAL                = r'\*='
    t_DIVEQUAL                  = r'/='
    t_MODEQUAL                  = r'%='
    t_PLUSEQUAL                 = r'\+='
    t_MINUSEQUAL                = r'\-='

    # Increment/decrement
    t_PLUSPLUS          = r'\+\+'
    t_MINUSMINUS        = r'\-\-'

    # Delimeters
    t_LPAREN            = r'\('
    t_RPAREN            = r'\)'
    t_LBRACKET          = r'\['
    t_RBRACKET          = r'\]'
    t_LBRACE            = r'\{'
    t_RBRACE            = r'\}'
    t_COMMA             = r','
    t_PERIOD            = r'\.'
    t_SEMI              = r';'
    t_COLON             = r':'
    
    ##
    ## Internal auxiliary methods
    ##

    # Error handling rule
    def t_error(self, t):
        print ("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

if __name__ == '__main__':
    # Build the lexer and try it out
    m = pcodeLexer()
    m.build()           # Build the lexer
    with open("./pcode_sample.txt", "r", encoding="utf-8") as f:
        data = f.readlines()
    data = "".join(data)
    m.test(data)       # Test it
