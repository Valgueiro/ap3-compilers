// Generated from autogen/Cymbol.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CymbolLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		TYPEINT=1, TYPEFLOAT=2, TYPEBOOLEAN=3, TYPEVOID=4, TYPESTRING=5, IF=6, 
		ELSE=7, RETURN=8, LP=9, RP=10, COMMA=11, SEMICOLON=12, LB=13, RB=14, QUOTE=15, 
		AS=16, EQ=17, NE=18, NOT=19, GT=20, LT=21, GE=22, LE=23, MUL=24, DIV=25, 
		PLUS=26, MINUS=27, AND=28, OR=29, INT=30, FLOAT=31, STRING=32, BOOLEAN=33, 
		ID=34, BLOCKCOMMENT=35, LINECOMMENT=36, WS=37;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"NUMBER", "LETTER", "UNDERLINE", "TYPEINT", "TYPEFLOAT", "TYPEBOOLEAN", 
			"TYPEVOID", "TYPESTRING", "IF", "ELSE", "RETURN", "LP", "RP", "COMMA", 
			"SEMICOLON", "LB", "RB", "QUOTE", "AS", "EQ", "NE", "NOT", "GT", "LT", 
			"GE", "LE", "MUL", "DIV", "PLUS", "MINUS", "AND", "OR", "INT", "FLOAT", 
			"STRING", "BOOLEAN", "ID", "BLOCKCOMMENT", "LINECOMMENT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'int'", "'float'", "'boolean'", "'void'", "'string'", "'if'", 
			"'else'", "'return'", "'('", "')'", "','", "';'", "'{'", "'}'", "'\"'", 
			"'='", "'=='", "'!='", "'!'", "'>'", "'<'", "'>='", "'<='", "'*'", "'/'", 
			"'+'", "'-'", "'&&'", "'||'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "TYPEINT", "TYPEFLOAT", "TYPEBOOLEAN", "TYPEVOID", "TYPESTRING", 
			"IF", "ELSE", "RETURN", "LP", "RP", "COMMA", "SEMICOLON", "LB", "RB", 
			"QUOTE", "AS", "EQ", "NE", "NOT", "GT", "LT", "GE", "LE", "MUL", "DIV", 
			"PLUS", "MINUS", "AND", "OR", "INT", "FLOAT", "STRING", "BOOLEAN", "ID", 
			"BLOCKCOMMENT", "LINECOMMENT", "WS"
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


	public CymbolLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Cymbol.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\'\u010a\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\3\2\3\2\3\3\3"+
		"\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7"+
		"\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3"+
		"\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\16\3"+
		"\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3"+
		"\25\3\25\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3"+
		"\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3"+
		"!\3\"\6\"\u00b8\n\"\r\"\16\"\u00b9\3#\6#\u00bd\n#\r#\16#\u00be\3#\3#\6"+
		"#\u00c3\n#\r#\16#\u00c4\3$\3$\3$\3$\7$\u00cb\n$\f$\16$\u00ce\13$\3$\3"+
		"$\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u00db\n%\3&\3&\5&\u00df\n&\3&\3&\3&\7"+
		"&\u00e4\n&\f&\16&\u00e7\13&\3\'\3\'\3\'\3\'\7\'\u00ed\n\'\f\'\16\'\u00f0"+
		"\13\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\7(\u00fb\n(\f(\16(\u00fe\13(\3("+
		"\3(\3(\3(\3)\6)\u0105\n)\r)\16)\u0106\3)\3)\4\u00ee\u00fc\2*\3\2\5\2\7"+
		"\2\t\3\13\4\r\5\17\6\21\7\23\b\25\t\27\n\31\13\33\f\35\r\37\16!\17#\20"+
		"%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67\329\33;\34=\35?\36A\37"+
		"C E!G\"I#K$M%O&Q\'\3\2\5\3\2\62;\4\2C\\c|\5\2\13\f\17\17\"\"\2\u0114\2"+
		"\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2"+
		"\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2"+
		"\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2"+
		"\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2"+
		"\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2"+
		"\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O"+
		"\3\2\2\2\2Q\3\2\2\2\3S\3\2\2\2\5U\3\2\2\2\7W\3\2\2\2\tY\3\2\2\2\13]\3"+
		"\2\2\2\rc\3\2\2\2\17k\3\2\2\2\21p\3\2\2\2\23w\3\2\2\2\25z\3\2\2\2\27\177"+
		"\3\2\2\2\31\u0086\3\2\2\2\33\u0088\3\2\2\2\35\u008a\3\2\2\2\37\u008c\3"+
		"\2\2\2!\u008e\3\2\2\2#\u0090\3\2\2\2%\u0092\3\2\2\2\'\u0094\3\2\2\2)\u0096"+
		"\3\2\2\2+\u0099\3\2\2\2-\u009c\3\2\2\2/\u009e\3\2\2\2\61\u00a0\3\2\2\2"+
		"\63\u00a2\3\2\2\2\65\u00a5\3\2\2\2\67\u00a8\3\2\2\29\u00aa\3\2\2\2;\u00ac"+
		"\3\2\2\2=\u00ae\3\2\2\2?\u00b0\3\2\2\2A\u00b3\3\2\2\2C\u00b7\3\2\2\2E"+
		"\u00bc\3\2\2\2G\u00c6\3\2\2\2I\u00da\3\2\2\2K\u00de\3\2\2\2M\u00e8\3\2"+
		"\2\2O\u00f6\3\2\2\2Q\u0104\3\2\2\2ST\t\2\2\2T\4\3\2\2\2UV\t\3\2\2V\6\3"+
		"\2\2\2WX\7a\2\2X\b\3\2\2\2YZ\7k\2\2Z[\7p\2\2[\\\7v\2\2\\\n\3\2\2\2]^\7"+
		"h\2\2^_\7n\2\2_`\7q\2\2`a\7c\2\2ab\7v\2\2b\f\3\2\2\2cd\7d\2\2de\7q\2\2"+
		"ef\7q\2\2fg\7n\2\2gh\7g\2\2hi\7c\2\2ij\7p\2\2j\16\3\2\2\2kl\7x\2\2lm\7"+
		"q\2\2mn\7k\2\2no\7f\2\2o\20\3\2\2\2pq\7u\2\2qr\7v\2\2rs\7t\2\2st\7k\2"+
		"\2tu\7p\2\2uv\7i\2\2v\22\3\2\2\2wx\7k\2\2xy\7h\2\2y\24\3\2\2\2z{\7g\2"+
		"\2{|\7n\2\2|}\7u\2\2}~\7g\2\2~\26\3\2\2\2\177\u0080\7t\2\2\u0080\u0081"+
		"\7g\2\2\u0081\u0082\7v\2\2\u0082\u0083\7w\2\2\u0083\u0084\7t\2\2\u0084"+
		"\u0085\7p\2\2\u0085\30\3\2\2\2\u0086\u0087\7*\2\2\u0087\32\3\2\2\2\u0088"+
		"\u0089\7+\2\2\u0089\34\3\2\2\2\u008a\u008b\7.\2\2\u008b\36\3\2\2\2\u008c"+
		"\u008d\7=\2\2\u008d \3\2\2\2\u008e\u008f\7}\2\2\u008f\"\3\2\2\2\u0090"+
		"\u0091\7\177\2\2\u0091$\3\2\2\2\u0092\u0093\7$\2\2\u0093&\3\2\2\2\u0094"+
		"\u0095\7?\2\2\u0095(\3\2\2\2\u0096\u0097\7?\2\2\u0097\u0098\7?\2\2\u0098"+
		"*\3\2\2\2\u0099\u009a\7#\2\2\u009a\u009b\7?\2\2\u009b,\3\2\2\2\u009c\u009d"+
		"\7#\2\2\u009d.\3\2\2\2\u009e\u009f\7@\2\2\u009f\60\3\2\2\2\u00a0\u00a1"+
		"\7>\2\2\u00a1\62\3\2\2\2\u00a2\u00a3\7@\2\2\u00a3\u00a4\7?\2\2\u00a4\64"+
		"\3\2\2\2\u00a5\u00a6\7>\2\2\u00a6\u00a7\7?\2\2\u00a7\66\3\2\2\2\u00a8"+
		"\u00a9\7,\2\2\u00a98\3\2\2\2\u00aa\u00ab\7\61\2\2\u00ab:\3\2\2\2\u00ac"+
		"\u00ad\7-\2\2\u00ad<\3\2\2\2\u00ae\u00af\7/\2\2\u00af>\3\2\2\2\u00b0\u00b1"+
		"\7(\2\2\u00b1\u00b2\7(\2\2\u00b2@\3\2\2\2\u00b3\u00b4\7~\2\2\u00b4\u00b5"+
		"\7~\2\2\u00b5B\3\2\2\2\u00b6\u00b8\5\3\2\2\u00b7\u00b6\3\2\2\2\u00b8\u00b9"+
		"\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00baD\3\2\2\2\u00bb"+
		"\u00bd\5\3\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bc\3\2"+
		"\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c2\7\60\2\2\u00c1"+
		"\u00c3\5\3\2\2\u00c2\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c2\3\2"+
		"\2\2\u00c4\u00c5\3\2\2\2\u00c5F\3\2\2\2\u00c6\u00cc\5%\23\2\u00c7\u00cb"+
		"\5\7\4\2\u00c8\u00cb\5\5\3\2\u00c9\u00cb\5\3\2\2\u00ca\u00c7\3\2\2\2\u00ca"+
		"\u00c8\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2"+
		"\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00cf\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf"+
		"\u00d0\5%\23\2\u00d0H\3\2\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3\7t\2\2\u00d3"+
		"\u00d4\7w\2\2\u00d4\u00db\7g\2\2\u00d5\u00d6\7h\2\2\u00d6\u00d7\7c\2\2"+
		"\u00d7\u00d8\7n\2\2\u00d8\u00d9\7u\2\2\u00d9\u00db\7g\2\2\u00da\u00d1"+
		"\3\2\2\2\u00da\u00d5\3\2\2\2\u00dbJ\3\2\2\2\u00dc\u00df\5\7\4\2\u00dd"+
		"\u00df\5\5\3\2\u00de\u00dc\3\2\2\2\u00de\u00dd\3\2\2\2\u00df\u00e5\3\2"+
		"\2\2\u00e0\u00e4\5\7\4\2\u00e1\u00e4\5\5\3\2\u00e2\u00e4\5\3\2\2\u00e3"+
		"\u00e0\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4\u00e7\3\2"+
		"\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6L\3\2\2\2\u00e7\u00e5"+
		"\3\2\2\2\u00e8\u00e9\7\61\2\2\u00e9\u00ea\7,\2\2\u00ea\u00ee\3\2\2\2\u00eb"+
		"\u00ed\13\2\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee\u00ef\3"+
		"\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f1\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1"+
		"\u00f2\7,\2\2\u00f2\u00f3\7\61\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5\b\'"+
		"\2\2\u00f5N\3\2\2\2\u00f6\u00f7\7\61\2\2\u00f7\u00f8\7\61\2\2\u00f8\u00fc"+
		"\3\2\2\2\u00f9\u00fb\13\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fe\3\2\2\2"+
		"\u00fc\u00fd\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00ff\3\2\2\2\u00fe\u00fc"+
		"\3\2\2\2\u00ff\u0100\7\f\2\2\u0100\u0101\3\2\2\2\u0101\u0102\b(\2\2\u0102"+
		"P\3\2\2\2\u0103\u0105\t\4\2\2\u0104\u0103\3\2\2\2\u0105\u0106\3\2\2\2"+
		"\u0106\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109"+
		"\b)\2\2\u0109R\3\2\2\2\17\2\u00b9\u00be\u00c4\u00ca\u00cc\u00da\u00de"+
		"\u00e3\u00e5\u00ee\u00fc\u0106\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}