from tokenize import tokenize, untokenize
import locale


#NăpârcaScript este un fel de Python "romanesc", in sensul in care sunt traduse cuvintele din python in romana, NăpârcaScript nu este un limbaj de programare in adevaratul sens al cuvantului.
#Am ales cuvantul "naparca", deoarece naparca este o soparla care arata cau un sarpe, exact cum acest limbaj arata a python, dar defapt e doar un DSL incorporat in python folosit pentru "code.py".

def set_locale():
    locale.setlocale(locale.LC_ALL, 'ro_RO.utf8')

def run_code(file: str):
    set_locale()
    try:
        exec(open(file).read(), globals())
    except Exception as e:
        error_message = str(e)

#pentru schimbarea unei traduceri trebuie scris în blocul de mai jos numit KEYS, in partea dreapta e limba romana, iar in stanga e python.
#la module precum: time, asyncio, pygame, Cirq...etc trebuiesc adaugate traduceri mai jos:
    keys = {
	'și' : 'and',
	'ca' : 'as',
	'impune' : 'assert',
	'rupe' : 'break',
	'clasa' : 'class',
	'continuă' : 'continue',
	'șterg' : 'del',
	'iardacă' : 'elif',
	'altfel' : 'else',
	'Fals' : 'False',
	'înfinal' : 'finally',
	'ptrfiecare' : 'for', # functia ”for” in python e mai degraba un ”foreach” astfel ca varianta ”pentru” nu este tocmai recomandata. Acum fiecare decide ce varianta vrea>>> "ptr"; ""pentru"; "perfiece"/”ptrfiece”; "pentrufiece"; "pentrufiecare"; "ptrfiecare"/"perfiecare"
	'din' : 'from',
	'dacă' : 'if',
	# 'în' : 'in',
	'îi' : 'is',
	'Fleac' : 'None',
	'non' : 'not', #ar putea fi folosit si ”nui” de la ”nu-i” dar in anumite contexte suna ca ”nuca in perete”. Spre exemplu la o linie de genul: ”if is not False” suna mult mai bine ”dacă este non Fals” decat ”dacă este nui Fals” deoarece ”nu-i” e format din verbul ”a fi”+ negatie...si mda.
	'trecila' : 'pass',
	'ridică' : 'raise',
	'Adevărat' : 'True',
	'încearcă' : 'try',
	'câtimp' : 'while',
	'cu' : 'with',
	'rodește' : 'yield',
	'așteaptă' : 'await',
	# 'asinc' : 'async', de la asincronizare
	'Elipsă' : 'Ellipsis',
	
	# până acum am vorbit de cuvinte cheie(keywords), de acum vom discuta despre funcții deja implementate în python(nu cred că toate aste sunt implementate, poate am băgat în plus, vom vedea)
	
	#parametrii
	'sinele' : 'self',
	'valoare' : 'value',
	'__nume__' : '__name__',
	'__depanare__' : '__debug__',
	'__debază__' : '__main__',
	#parametrii
	'curăță' : 'clear',
	'rulare' : 'run',
	'adormi' : 'sleep',
	'copiază' : 'copy',
	'DinChei' : 'fromkeys',
	'obține' : 'get',
	'articole' : 'items',
	'chei' : 'keys',
	'poc' : 'pop', # poc este de la pocnește
	'pocarticol' : 'popitem',
	'setimplicit' : 'setdefault',
	'înoire' : 'update',
	'valori' : 'values',
	'anexează' : 'append',
	'numără' : 'count',
	'extinde' : 'extend',
	'inserează' : 'insert',
	'scoate' : 'remove',
	'invers' : 'reverse',
	'adaugă' : 'add',
	'diferență' : 'difference',
	'diferențăînoire' : 'difference_update',
	'decartă' : 'discard',
	'intersecție' : 'intersection',
	'intersecțieînoire' : 'intersection_update',
	'îiseparat' : 'isdisjoint',
	'îisubset' : 'issubset',
	'îisuperset' : 'issuperset',
	'simetric_diferență' : 'symmetric_difference',
	'simetric_diferență_înoire' : 'symmetric_difference_update',
	'uniune' : 'union',
	'închis' : 'close',
	'detașat' : 'detach',
	'fișiernr' : 'fileno',
	'fișier' : 'file',
	'lăut' : 'flush',            #flush e ca un lăut sau un fel de spălare
	'îiteletip' : 'isatty',  # /îiinteractiv
	'citire' : 'read',
	'citeț' : 'readable',
	'citeștelinia' : 'readline',
	'citeștelinile' : 'readlines',
	'lămurire' : 'seek',              #  străduie/poziționare/cercetare
	'lămuritor' : 'seekable',
	'spune' : 'tell',
	'trunchiază' : 'truncate',
	'scriptibil' : 'writable',
	'scrie' : 'write',
	'scrielini' : 'writelines',
	'capitalizare' : 'capitalize',
	'plieredecaz' : 'casefold',
	'centru' : 'center',
	'codifică' : 'encode',
	'terminăcu' : 'endswith',
	'întindealineaturi' : 'expandtabs',
	'află' : 'find',
	'îialfanum' : 'isalnum',
	'îialfa' : 'isalpha',
	'îiascii' : 'isascii',
	'îizecimal' : 'isdecimal',
	'îicifră' : 'isdigit',
	'îiidentificator' : 'isidentifier',
	'îiminusculă' : 'islower',
	'îinumeric' : 'isnumeric',
	'îiprintabil' : 'isprintable',
	'îispațiu' : 'isspace',
	'îititlu' : 'istitle',
	'îisuper' : 'isupper',
	'alătură' : 'join',
	'stjustare' : 'ljust',
	'minusculizare' : 'lower',
	'stdecojire' : 'lstrip',
	'fătrans' : 'maketrans',
	'partiție' : 'partition',
	'înlocuie' : 'replace',
	'draflă' : 'rfind',
	'drindex' : 'rindex',
	'drjustare' : 'rjust',
	'drpartiție' : 'rpartition',
	'drdespică' : 'rsplit',
	'drdecojire' : 'rstrip',
	'despică' : 'split',
	'despicălini' : 'splitlines',
	'începecu' : 'startswith',
	'decojire' : 'strip',
	'trocdecaz' : 'swapcase',
	'titlu' : 'title',
	'tradu' : 'translate',
	'superior' : 'upper',
	'zumple' : 'zfill',
	'varble' : 'vars', # vars e prescurtarea de la „variables” tradus ar fi „variabile” abreviat ar fi varble sau vare , acum depinde de 	fiecare dacă dorește prescurtare sau nu 
	'toț' : 'all',
	'orice' : 'any',
	'bitaranjare' : 'bytearray',
	'biți' : 'bytes',
	'apelabil' : 'callable',
	'caract' : 'chr',
	'clasămetodă' : 'classmethod',
	'compilare' : 'compile',
	'ștergeatr' : 'delattr',
	#'dicț' : 'dict',
	'enumeră' : 'enumerate',
	'filtrare' : 'filter',
	'fluct' : 'float', #fluct e abreviere de la ”fluctuant” fiind un numar cu punct mobil/fluctuant, adică orice numar intreg cu zecimale 	ca 1.5/2.35...
	'înghețatset' : 'frozenset',
	'obțineatr' : 'getattr',
	'globale' : 'globals',
	'areatr' : 'hasattr',
	'zăpăcire' : 'hash',  # nu prea e recomandat, deoarece termenul hash e o funcție unică de dispersie, care inlocuiește datele într-un anumit mod, chiar dacă cumva le amestecă sau zăpăcește
	'ajutor' : 'help',
	'introd' : 'input', #de la introducere
	'ţâşnire' : 'output', #Țâșnire e sinonim la ieșire doar că din cauză că există ”exit()”, trebuie folosit alt cuvânt. Ar putea fi creat ”extroducere”
	'ieșire' : 'exit',
	'înt' : 'int',  # int vine de la integer ce înseamnă număr întreg, am schimbat doar prima literă dar poate nu-i nevoie 
	'îiinstanță' : 'isinstance',
	'îisubclasă' : 'issubclass',
	'lungime' : 'len',
	'locale' : 'locals',
	'memorievedere' : 'memoryview',
	'următor' : 'next',
	'obiect' : 'object',
	'deschidere' : 'open',
	'laputere' : 'pow',
	'proprietate' : 'property',
	'gama' : 'range',
	'inversat' : 'reversed',
	'rotunjire' : 'round',
	#'setatr' : 'setattr', sincer e doar un „t” in plus
	'feliare' : 'slice',
	'sortat' : 'sorted',
	'staticămetodă' : 'staticmethod',
	'șrg' : 'str',    #string e un șirag, ca sa intelegi mai clar, imagineazati un sirag de margele unde fiecare margea reprezinta o litera, stringul/siragul fiind un sir de litere formand o informatie scrisa.
	'tuplu' : 'tuple',
	'tipăre' : 'type', # trebuie menționat că uneori type poate însemna tip/tipar alteori tipărire,
	'compr_fermoar' : 'zip', # zip înseamnă fermoar, fiind un tip de compresare lossless combresând prin imbinarea de tupluri de date precum fermoarul.
	'ruperepunct' : 'breakpoint',
	'drepturiautor' : 'copyright',
	'credite' : 'credits',
	'afișaj' : 'display',
	'obț_îpython' : 'get_ipython',
	'licență' : 'license',
	'bazășirag' : 'basestring',
	'aplică' : 'apply',
	'coercire' : 'coerce', #de la coerciție, fiind constrângere
	'execfișier' : 'execfile',
	'lung' : 'long',
	'crud_introd' : 'raw_input',
	'reîncarcă' : 'reload',
	'unicaract' : 'unichr',
	'xgama' : 'xrange',
	
	# de aici încolo avem decoratori
	'îmbroboditor' : 'wrapper',
	'@propietate': '@property', # @property.setter e folosit daca definești o funcție radius schimbi în @radius.setter
	'@clasametodă': '@classmethod',
	'@staticămetodă': '@staticmethod',
	'@funcțieunelte.ambalare': '@functools.wraps',
	'@funcțieunelte.singurădepeșare': '@functools.singledispatch', #depeșare este sinonim cu expedire, și se potrivește la ”dispatch”
	'@f.înregistră': '@f.register()',
	'@funcțieunelte.puținutilizatrecent.cache': '@functools.lru_cache',
	'@funcțieunelte.comparare_la_cheie': '@functools.cmp_to_key',
	'@funcțieunelte.total_ordonare': '@functools.total_ordering',
	'@funcțieunelte.parțială': '@functools.partial',
	'@tipărire.supraîncărcare': '@typing.overload',
	'@clasedate.clasădate': '@dataclasses.dataclass',
	'@laieșire.înregistră': '@atexit.register',
	'@abc.ABCMeta.înregistră': '@abc.ABCMeta.register',
	'@enum.unică': '@enum.unique',
	'@ApelProcedurăDistanțăXML.înregistră_funcție': '@xmlrpc.register_function',
	'@sistem.setareurmă': '@sys.settrace',
	'@corutină': '@coroutine',
	'@regularisire': '@throttle',          #    @throttle(2,1) ,
	'@prinzătorExcepți': '@exceptionCatcher',
	'@măsuriștimp': '@timeit',
	'@asinc_proces': '@async_process',
	'@fireexecutate': '@threaded',
	'@depanare': '@debug',
	'@omite_dacă_mediul': '@skip_if_env',
	'@încuie_sau_șteaptă': '@lock_or_wait',
	'@peticire.simulant.unitatest': '@unittest.mock.patch',
	'@îmbrobodire.peticire_funcție_îmbroboditor': '@wrapt.patch_function_wrapper',
	'@încearcăprinde': '@trycatch',
	'@logare_apeluri': '@log_calls',
	'@decorator_numit': '@named_decorator',
	'@înschimb': '@instead',
	'@înainte': '@before',
	'@clic.opțiune': '@click.option',               #  @click.option("-d")
	'@config_deocrator.setare': '@config_decorator.setting',
	'@ExpresieRegulată_decorator.ascultă': '@regex_decorator.listen',
	'@expune': '@expose',
	'@înregistră': '@register',
	'@urmă': '@trace',
	'@murdar': '@dirty',
	'@mutabil': '@mutable',
	'@la_șirag': '@to_string',
	'@repetă': '@repeat',
	'@DatăAtribuită': '@DataAtrribute',     #  @DataAtrribute("desc") 
	'@currizat': '@curried',       #nu prea poate fi tradus deoarece cuvântul provine de la un concept matematic creat de Haskel Curry, dacă ești curios de etimologia numelui lui nu are legătură cu condimentul curry și mai degrabă cu creșonul.
	'@arg.validare': '@arg.validate',
	'__debază__': '@__main__',
	'@sine': '@self',
	'@reîncearcă': '@retry',	#sau @retrage ,  ar trebui menționat formatul? @retry(times=2)
	
	#urmează avertizările  :   ('Warning')], compact=True) 
	
	'Avertizare': 'Warning',
	'AvertizareBiți': 'BytesWarning',
	'AvertizareDepreciere': 'DeprecationWarning',
	'AvertizareViitor': 'FutureWarning',
	'AvertizareImport': 'ImportWarning',
	'AvertizareDepreciereScontată': 'PendingDeprecationWarning',
	'AvertizareResursă': 'ResourceWarning',
	'AvertizareTimpRulare': 'RuntimeWarning',
	'AvertizareSintaxă': 'SyntaxWarning',
	'AvertizareUnicod': 'UnicodeWarning',
	'AvertizareUtilizator': 'UserWarning',
	'AvertizareDepășire': 'OverflowWarning',
	    
	'Excepție': 'Exception',
	'EroareBlocare': 'BlockingIOError',
	'EroareStandard': 'StandardError',
	'EroareConductăÎntreruptă': 'BrokenPipeError',
	'EroareBuffer': 'BufferError',                     #sau EroareAmortizor
	'EroareProcesorCopil': 'ChildProcessError',
	'EroareConexiuneAvortată': 'ConnectionAbortedError', #sau întreruptă/abandonată în loc de avortat
	'EroareConexiune': 'ConnectionError',
	'EroareConexiuneRefuzată': 'ConnectionRefusedError',
	'EroareConexiuneResetată': 'ConnectionResetError',
	'EroareMediu': 'EnvironmentError',
	'EroareFișierulExistă': 'FileExistsError',
	'EroareFișierNonGăsit': 'FileNotFoundError',
	'EroareIntroducereȚâșnire': 'IOError',
	'EroareĂstaiDirector': 'IsADirectoryError',
	'EroareModulNegăsit': 'ModuleNotFoundError',
	'EroareĂstaNuiDirector': 'NotADirectoryError',
	'EroarePermisiune': 'PermissionError',
	'EroareProcesdeCăutare': 'ProcessLookupError',
	'EroareRecursie': 'RecursionError',
	'EroareÎnafaraTimpului': 'TimeoutError',
	'EroareAritmetica': 'ArithmeticError',
	'EroareImpunere': 'AssertionError',
	'EroareAtribuție': 'AttributeError',
	'EroareSfârșitdeFișier': 'EOFError',
	'EroarePunctFluctuant': 'FloatingPointError',
	'EroareIeșireGenerator': 'GeneratorExit',
	'EroareImport': 'ImportError',
	'EroareIndentare': 'IndentationError',
	'EroareIndex': 'IndexError',
	'EroareCheie': 'KeyError',
	'TastaturăÎntreruptă': 'KeyboardInterrupt',
	'EroareUităteDupă': 'LookupError',
	'EroareMemorie': 'MemoryError',
	'EroareNume': 'NameError',
	'EroareNeImplementat': 'NotImplemented',
	'EroareSistemDeOperare': 'OSError',
	'EroaredeDepășire': 'OverflowError',
	'EroareReferință': 'ReferenceError',
	'EroareTimpDeRulare': 'RuntimeError',
	'StopIterare': 'StopIteration',
	'EroareSintaxă': 'SyntaxError',
	'EroareAlineatTab': 'TabError',
	'EroareSistem': 'SystemError',
	'EroareIeșireSistem': 'SystemExit',
	'EroareTipăr': 'TypeError',
	'EroaredeVariabilăNeatribuită': 'UnboundLocalError',
	'EroareUnicod': 'UnicodeError',
	'EroareCodificareUnicod': 'UnicodeEncodeError',
	'EroareDecodificareUnicod': 'UnicodeDecodeError',
	'EroareTraducereUnicod': 'UnicodeTranslateError',
	'EroareValoare': 'ValueError',
	'EroareDiviziuneCuZero': 'ZeroDivisionError',
	'EroareFereastră': 'WindowError',
}
   
    	# 'def' în română ar fi tot def de la „definește” ,
    	# 'except' în română ar fi tot except de la „exceptă” ,
    	# 'global' în română ar fi tot global,
    	# 'import' importă,
    	# 'lambda' lambda in sine este o functie anonima, ai putea inlocui lambda cu "anonimfunc" sau sa o lasi asa, ea este folosita la creare unei expresii de obicei matematice care nu are nevoie de o denumire.
    	#'nonlocal' nonlocal,
    	# 'or' în română există varianta „sau” & „ori/or” a doua e mai potrivită,modulul fiind mai mult pentru învățare iar pentru programe mai sofisticate trebuie învățată limba engleză., sau poate nu, cine știe.
    	# 'return' tot return de la „returnează” ,
    	
    # abs(xx) e absolut, cam tot aia
	# ascii(xx) folosește cod ascii
	# bin(xx) binar e tot binar
	# bool(xx) boolean e tot boolean
	# complex(xx) la fel
	# dir() dir e dir
	# divmod()  divmod e diviziune mod
	# eval() eval e evaluare
	# exec()  exec e executare
	# hex() hex e hexadecimal
	# id()  id tot id
	# list()   listă
	# map()  mapare sau mapă
	# max() la fel
	# min()  la fel
	# oct()  oct e octal
	# ord() ord e ordine/ordonare
	# print()  printare/printează
	# repr()  e reprezintă
	# set() setare
	# sum()  sumă/suma
	# index() tot index
	# super() super
	# sort() sau sortare() cam tot aia e
	# format() 
	# format_map()
	
		
	#  @contextlib.contextmanager : se traduce la fel
	# @monkeybiz.patch(fn)  :  afacere dinamică/maimuță/năbădăi. peticire(fn) ........... habar n-am
	# @inject(modules…)    
	# @dec.decorator(before=cb,after=cb)
	# @contract({"param":gt(3)})  
	# @attrs
	# @decorator  
	# @decorator_args
	# @arg.validate
	# @intercept, 
	# @pedantic,
	# @Decorator
	# @final, 
	# @auto_obj  
	# @data,  
	
	# trebuie menționat că sunt cuvinte care nu pot fi traduse și să se înțeleagă de la sine precum buffer care ar fi aproape echivalent cu tampon sau amortizor, buffer fiind un loc unde stau temporar anumite date,
	# nu e totuși recomandat de uni programatori folosirea cuvântului amortizor, prin urmare mai ok ar fi să înțelegi ce înseamnă buffer, dacă nu acum nu strică să schimbi înțelesul unui cuvânt românesc.
	# În cazul token ar putea fi înlocuit de jeton/fisă, dar în cazul tokenize ar trebui inventat un nou cuvânt, probabil jetonare, deși există deja cuvântul tokenizare.
	# Sau „script” care vine din latină și înseamnă înscris, dar scriptul poatea avea multe înțelesuri cum ar fi cod, scris, simbol.
	#In unele limbaje de programare se foloseste cuvantul cheie: "by" poate fi oarecum tradus de frantuzescul "via", dar in romana are 4 sensuri anume "de/dupa/prin/spre" pentru ultimele 2 poate fi folosit regionalismul "pre".
	#Totusi in functie de limbaj la "by" se foloseste doar unul din sensurile din romana, spre exemplu in python, la modulul "pandas" exista metoda "groupby()" tradusa ar fi "grupeazadupa".
    

    with open(file, 'rb') as src:
        tokens = []

        for token in tokenize(src.readline):

            if token.string in keys:
                t = (token.type, keys[token.string])
            else:
                t = (token.type, token.string)

            tokens.append(t)

    modified_code = untokenize(tokens).decode('utf-8')
    


    print(type(modified_code))

    for k in keys:
    	modified_code.replace(k[0], k[1])	

    
    exec(modified_code, globals())

    
if __name__ == '__main__':
    run_code(file='code.năps') 
    
     #momentan acesta e inca un prototip
    


   # def execute_code(self, code):
    #    try:
     #       exec(code)
      #  except Exception as e:
       #     print(f"Error: {e}")



# if __name__ == '__main__':
  #  MyInterpreter().cmdloop()
    
    
    
    





















