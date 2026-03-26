// Generated from /home/lina/Descargas/ACTIVIDAD_ANALISISSINTACTICO/ACTIVIDADAST/Ejercicio2/Ejercicio2.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class Ejercicio2Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, WS=8;
	public static final int
		RULE_s = 0, RULE_expr = 1, RULE_term = 2, RULE_factor = 3;
	private static String[] makeRuleNames() {
		return new String[] {
			"s", "expr", "term", "factor"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'+'", "'-'", "'*'", "'/'", "'a'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Ejercicio2.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public Ejercicio2Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public SContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s; }
	}

	public final SContext s() throws RecognitionException {
		SContext _localctx = new SContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_s);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(8);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(10);
			term();
			setState(15);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0 || _la==T__1) {
				{
				{
				setState(11);
				_la = _input.LA(1);
				if ( !(_la==T__0 || _la==T__1) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(12);
				term();
				}
				}
				setState(17);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			factor();
			setState(23);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__2 || _la==T__3) {
				{
				{
				setState(19);
				_la = _input.LA(1);
				if ( !(_la==T__2 || _la==T__3) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(20);
				factor();
				}
				}
				setState(25);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_factor);
		try {
			setState(31);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__4:
				enterOuterAlt(_localctx, 1);
				{
				setState(26);
				match(T__4);
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 2);
				{
				setState(27);
				match(T__5);
				setState(28);
				expr();
				setState(29);
				match(T__6);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\b\"\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0005\u0001\u000e\b\u0001\n\u0001\f\u0001"+
		"\u0011\t\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002\u0016\b"+
		"\u0002\n\u0002\f\u0002\u0019\t\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0003\u0003 \b\u0003\u0001\u0003\u0000\u0000"+
		"\u0004\u0000\u0002\u0004\u0006\u0000\u0002\u0001\u0000\u0001\u0002\u0001"+
		"\u0000\u0003\u0004 \u0000\b\u0001\u0000\u0000\u0000\u0002\n\u0001\u0000"+
		"\u0000\u0000\u0004\u0012\u0001\u0000\u0000\u0000\u0006\u001f\u0001\u0000"+
		"\u0000\u0000\b\t\u0003\u0002\u0001\u0000\t\u0001\u0001\u0000\u0000\u0000"+
		"\n\u000f\u0003\u0004\u0002\u0000\u000b\f\u0007\u0000\u0000\u0000\f\u000e"+
		"\u0003\u0004\u0002\u0000\r\u000b\u0001\u0000\u0000\u0000\u000e\u0011\u0001"+
		"\u0000\u0000\u0000\u000f\r\u0001\u0000\u0000\u0000\u000f\u0010\u0001\u0000"+
		"\u0000\u0000\u0010\u0003\u0001\u0000\u0000\u0000\u0011\u000f\u0001\u0000"+
		"\u0000\u0000\u0012\u0017\u0003\u0006\u0003\u0000\u0013\u0014\u0007\u0001"+
		"\u0000\u0000\u0014\u0016\u0003\u0006\u0003\u0000\u0015\u0013\u0001\u0000"+
		"\u0000\u0000\u0016\u0019\u0001\u0000\u0000\u0000\u0017\u0015\u0001\u0000"+
		"\u0000\u0000\u0017\u0018\u0001\u0000\u0000\u0000\u0018\u0005\u0001\u0000"+
		"\u0000\u0000\u0019\u0017\u0001\u0000\u0000\u0000\u001a \u0005\u0005\u0000"+
		"\u0000\u001b\u001c\u0005\u0006\u0000\u0000\u001c\u001d\u0003\u0002\u0001"+
		"\u0000\u001d\u001e\u0005\u0007\u0000\u0000\u001e \u0001\u0000\u0000\u0000"+
		"\u001f\u001a\u0001\u0000\u0000\u0000\u001f\u001b\u0001\u0000\u0000\u0000"+
		" \u0007\u0001\u0000\u0000\u0000\u0003\u000f\u0017\u001f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}