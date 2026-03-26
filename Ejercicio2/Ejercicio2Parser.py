# Generated from Ejercicio2.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,34,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,1,1,1,1,1,5,1,
        14,8,1,10,1,12,1,17,9,1,1,2,1,2,1,2,5,2,22,8,2,10,2,12,2,25,9,2,
        1,3,1,3,1,3,1,3,1,3,3,3,32,8,3,1,3,0,0,4,0,2,4,6,0,2,1,0,1,2,1,0,
        3,4,32,0,8,1,0,0,0,2,10,1,0,0,0,4,18,1,0,0,0,6,31,1,0,0,0,8,9,3,
        2,1,0,9,1,1,0,0,0,10,15,3,4,2,0,11,12,7,0,0,0,12,14,3,4,2,0,13,11,
        1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,3,1,0,0,0,17,
        15,1,0,0,0,18,23,3,6,3,0,19,20,7,1,0,0,20,22,3,6,3,0,21,19,1,0,0,
        0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,5,1,0,0,0,25,23,1,
        0,0,0,26,32,5,5,0,0,27,28,5,6,0,0,28,29,3,2,1,0,29,30,5,7,0,0,30,
        32,1,0,0,0,31,26,1,0,0,0,31,27,1,0,0,0,32,7,1,0,0,0,3,15,23,31
    ]

class Ejercicio2Parser ( Parser ):

    grammarFileName = "Ejercicio2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'a'", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WS" ]

    RULE_s = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_factor = 3

    ruleNames =  [ "s", "expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(Ejercicio2Parser.ExprContext,0)


        def getRuleIndex(self):
            return Ejercicio2Parser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)




    def s(self):

        localctx = Ejercicio2Parser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Ejercicio2Parser.TermContext)
            else:
                return self.getTypedRuleContext(Ejercicio2Parser.TermContext,i)


        def getRuleIndex(self):
            return Ejercicio2Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = Ejercicio2Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.term()
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 11
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 12
                self.term()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Ejercicio2Parser.FactorContext)
            else:
                return self.getTypedRuleContext(Ejercicio2Parser.FactorContext,i)


        def getRuleIndex(self):
            return Ejercicio2Parser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = Ejercicio2Parser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.factor()
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 19
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 20
                self.factor()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(Ejercicio2Parser.ExprContext,0)


        def getRuleIndex(self):
            return Ejercicio2Parser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = Ejercicio2Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.match(Ejercicio2Parser.T__4)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(Ejercicio2Parser.T__5)
                self.state = 28
                self.expr()
                self.state = 29
                self.match(Ejercicio2Parser.T__6)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





