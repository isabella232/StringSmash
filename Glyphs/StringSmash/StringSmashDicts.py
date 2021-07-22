# -*- coding: utf-8 -*-
import collections

presetDict = {}
presetDict = collections.OrderedDict()

presetDictL = {}
presetDictL = collections.OrderedDict()

presetDictR = {}
presetDictR = collections.OrderedDict()

	### START Frauen Script
# Left Glyph (right refers to right side of glyph)
# presetDictL["rightFlat"] = "j g y q".split(" ") 
# presetDictL["rightn"] = "a n u m h i".split(" ")
# presetDictL["rightBottomTail"] = "a n m h u i d l t k x".split(" ")
# presetDictL["rightRound"] = "b p thorn eth v w germandbls".split(" ")
# presetDictL["rightOpen"] = "c e s o k x z t r d l f".split(" ")
# presetDictL["rightLoop"] = "d l".split(" ")
# presetDictL["rightAsc"] = "d l f".split(" ")

# presetDictL["CAPSright"] = "S C E AE L I T J Y U N M G H F B D O Q P Thorn V W A K R X Z".split(" ") # Frauen similar
# presetDictL["lcright"] = presetDictL["rightFlat"] + presetDictL["rightBottomTail"] + presetDictL["rightRound"] + presetDictL["rightOpen"] # Frauen lc-*

# presetDictL["smcpright"] = "h.smcp i.smcp n.smcp u.smcp g.smcp o.smcp q.smcp o.smcp d.smcp b.smcp j.smcp r.smcp p.smcp thorn.smcp ae.smcp a.smcp m.smcp v.smcp w.smcp y.smcp t.smcp x.smcp z.smcp k.smcp r.smcp c.smcp s.smcp l.smcp e.smcp f.smcp p.smcp".split(" ")

# Right Glyph
# presetDictR["leftFlat"] = "h k b l j".split(" ") # left refers to left side of glyph
# presetDictR["leftFlat+"] = presetDictR["leftFlat"] + "n.alt i.alt".split(" ")
# presetDictR["leftTopTail"] = "i r n m u y p v w x z".split(" ")
# presetDictR["leftRound"] = "o c e g q d a".split(" ")
# presetDictR["leftOpen"] = "s v w x z".split(" ")
# presetDictR["leftDesc"] = "g f p q y z".split(" ")
# presetDictR["leftDiacritics"] = "abreve acircumflex adieresis agrave amacron aring atilde ccaron ccircumflex cdotaccent ebreve ecaron ecircumflex edieresis edotaccent egrave emacron gbreve gcircumflex gcommaaccent gdotaccent hbar iacute ibreve icircumflex idieresis idotaccent igrave imacron itilde jcircumflex lcaron ldot lslash nacute ncaron ntilde obreve ocircumflex odieresis ograve ohungarumlaut omacron otilde rcaron scaron scircumflex tbar tcaron ubreve ucircumflex udieresis ugrave umacron uring utilde wgrave ycircumflex ydieresis zcaron zdotaccent".split(" ")
# presetDictR["lcleft"] = presetDictR["leftFlat"] + presetDictR["leftTopTail"] + presetDictR["leftRound"] + "s f t".split(" ")

# presetDictR["lcleft"] = "h k b l f j i r n m i u y n v w x n o c e d eth o a s n t j f o q g d n y p z".split(" ") # Frauen UC-lc

# presetDictR["lc_ascdesc"] = "f germandbls yacute thorn ydieresis gcircumflex gbreve gdotaccent gcommaaccent kcommaaccent ycircumflex zacute zdotaccent zcaron j iogonek ij tcommaaccent".split(" ")
# presetDictR["lcleft_no_asc_desc"] = [x for x in presetDictR['lcleft'] if x not in presetDictR["lc_ascdesc"]]

# presetDictR["smcpleft"] = "b.smcp e.smcp h.smcp i.smcp n.smcp c.smcp o.smcp u.smcp s.smcp a.smcp ae.smcp m.smcp v.smcp w.smcp y.smcp t.smcp x.smcp j.smcp z.smcp s.smcp".split(" ") # Frauen ???

# Both Glyphs
# presetDict["vw"] = "v w".split(" ")
# presetDict["xBar"] = "f t x".split(" ")

# presetDict["CAPSList"] = "I H N M Z Lslash L E F T K X R AE A V W Y P Thorn J U B O D Eth Q C G S".split(" ")
presetDict["CAPS_ABC+"] = "A AE B C D Eth E F G H I J K L Lslash M N O OE P Thorn Q R S T U V W X Y Z".split(" ")
presetDict["CAPS_ABC"] = [x for x in presetDict['CAPS_ABC+'] if x not in "AE Germandbls Dcroat Eth Lslash Thorn".split(" ")]# presetDict["CAPS_ascdesc"] = "E I K L X".split(" ")
# presetDict["CAPS_smcpList"] = "I.alt2 H.alt.tail N M Z.alt2 L Lslash E F.alt.tail T.alt K.alt X.alt R AE A V W Y P Thorn J.alt U B O Dcroat D Oslash Q C G S".split(" ") # Frauen Script

	### END Frauen Script

# Glyphs App divided groups (~sans)
presetDict["CAPS_hori_str"] = "A B P D H I L E F Z T R Thorn OE G".split(" ")
presetDict["CAPS_bot top round"] = "J G C O Q S U OE".split(" ")
presetDict["CAPS_left_str"] = "B D E F H I K L N P R U".split(" ")
presetDict["CAPS_right_str"] = "G H I J N U".split(" ")
presetDict["CAPS_side_round"] = "B P R Thorn G C O Q D S OE".split(" ")
presetDict["CAPS_side_open"] = "A AE E F C G J L P S Y V W K X Z".split(" ")
presetDict["CAPS_diag"] = "A AE K X Z Y V W M N R".split(" ")
presetDict["CAPS_sym"] = "T V Y X W Z A".split(" ")


presetDictL["CAPS_sansL"] = "H M U E F T L Z K X A V W Y P Thorn B R D O Q C G S J".split(" ")
# presetDictL["CAPS_sansL"] = "H M U E F T L Z K X A V W Y P Thorn F H B R D O Q C G O S J".split(" ")

presetDictR["CAPS_sansR"] = "H Lslash U J N M O C G Q S T AE A Y V W X Z".split(" ")
presetDictR["sc_sansR"] = "h.sc lslash.sc u.sc j.sc n.sc m.sc o.sc c.sc g.sc q.sc s.sc t.sc ae.sc a.sc y.sc v.sc w.sc x.sc z.sc".split(" ")


presetDict["lc_abc+"] = "a ae b germandbls c d dcroat eth e f g h i j k l lslash m n o oe p thorn q r s t u v w x y z".split(" ")
presetDict["lc_abc"] = [x for x in presetDict['lc_abc+'] if x not in "ae germandbls dcroat eth lslash thorn".split(" ")]  # Frauen Script
presetDictL["lc_BradfordItalicL"] = "o b p v w y q j n u h m a d i l t o c e s x z k r g t f j ".split(" ")
presetDictR["lc_BradfordItalicR"] = "a d q h k b l m n u r y p j i u o c e g s x z v w f t".split(" ")
presetDictL["lc_SansL"] = "u i j f l t r n a o e c s eth o p b q d g germandbls k x z w v y".split(" ")
presetDictR["lc_SansR"] = "n u l i j s a g eth o e c p h q d f t k x z w v y".split(" ")


# presetDict["lcQuoteList"] = "n r h m u i icircumflex idieresis imacron j f l lslash t s a e c p b o q d dcroat eth g k x z w v y".split(" ")
# presetDict["lcListBasic"] = "s v w x z a r y n y m h u y i j f t l d a e c o p b g q d h b k l j".split(" ") # Frauen Script
# presetDict["lc+"] = "s n r h m u i j f l lslash t a e c o p b q d dcroat eth g k x z w v y germandbls".split(" ") # Frauen Script
# presetDict["lcListBasic"] = [x for x in presetDict['lcList'] if x not in "lslash germandbls dcroat eth".split(" ")]  # Frauen Script

# Glyphs App divided groups (~sans)
presetDict["lc_n"] = "r n m h u".split(" ")
presetDict["lc_round"] = "s eth o c e a b p d q oe ae germandbls g".split(" ")
presetDict["lc_tail"] = "l t f j y".split(" ")
presetDict["lc_diag"] = "k x z y v w".split(" ")
presetDict["lc_hori_str"] = "z t f".split(" ")
presetDict["lc_asc"] = "thorn eth d b t f i j l germandbls g".split(" ")
presetDict["lc_des"] = "thorn q p g j y".split(" ")

presetDict["lc_ordered"] = "s n r h m u i j f l t a e c o p b q d g k x z w v y".split(" ")

presetDict["smcp_abc+"] = "a.smcp ae.smcp b.smcp c.smcp d.smcp eth.smcp e.smcp f.smcp g.smcp h.smcp i.smcp j.smcp k.smcp l.smcp lslash.smcp m.smcp n.smcp o.smcp oe.smcp p.smcp thorn.smcp q.smcp r.smcp s.smcp t.smcp u.smcp v.smcp w.smcp x.smcp y.smcp z.smcp".split(" ")
# presetDict["smcp_all"] = "h.smcp i.smcp n.smcp u.smcp g.smcp o.smcp q.smcp d.smcp b.smcp j.smcp r.smcp p.smcp thorn.smcp ae.smcp a.smcp m.smcp v.smcp w.smcp y.smcp t.smcp x.smcp z.smcp k.smcp r.smcp c.smcp s.smcp l.smcp e.smcp f.smcp".split(" ")# Frauen Script
# presetDict["smcp_group_only"] = "b.smcp e.smcp h.smcp i.smcp u.smcp n.smcp c.smcp o.smcp s.smcp a.smcp m.smcp ae.smcp v.smcp w.smcp y.smcp t.smcp x.smcp j.smcp z.smcp s.smcp".split(" ") # Frauen Script

# presetDict["CAPSList"] = "I H N M Z L Lslash E F T K X R AE A V W Y P Thorn J U Germandbls B O Dcroat D Oslash Q C G S".split(" ")
# presetDict["CAPSListMinimal"] = "I Z L E F T K X R A V W Y P Thorn J U Germandbls B O Oslash Q C G S".split(" ")
# presetDict["CAPSPunctList"] = "questiondown.uc exclamdown.uc bullet.uc periodcentered.uc hyphen.uc endash.uc emdash.uc guilsinglleft.uc guilsinglright.uc guillemetleft.uc guillemetright,.uc parenleft.uc parenright.uc bracketleft.uc bracketright.uc braceleft.uc braceright.uc bar.uc slash.uc backslash.uc at.uc".split(" ")
presetDictL["numL"] = "zero one four seven nine two six five eight three".split(" ")
presetDictR["numR"] = "zero one two three eight nine five six four seven".split(" ")

presetDict["numList"] = "one seven four two five three eight zero nine six".split(" ")
presetDict["numList123"] = "zero one two three four five six seven eight nine".split(" ")

# presetDict["tabNumList"] = ["%s.tf" % l for l in presetDict['numList']]
# presetDict["CAPSnumList"] = presetDict['CAPSList'] + presetDict['numList']

# presetDict["smcpList"] = "uni0122.sc uni0136.sc uni013B.sc uni0145.sc uni0156.sc uni015E.sc uni0218.sc uni0162.sc uni021A.sc a.sc aacute.sc abreve.sc acircumflex.sc adieresis.sc agrave,.sc amacron.sc aogonek.sc aring.sc atilde.sc ae.sc b.sc c.sc cacute.sc ccaron.sc ccedilla.sc d.sc eth.sc dcaron.sc dcroat.sc e.sc eacute.sc ecaron.sc ecircumflex.sc edieresis.sc edotaccent.sc egrave.sc emacron.sc eogonek.sc f.sc g.sc gbreve.sc h.sc i.sc iacute.sc iacute_j.loclNLD.sc icircumflex.sc idieresis.sc idotaccent.sc igrave.sc ij.sc imacron.sc iogonek.sc j.sc k.sc l.sc lacute.sc lcaron.sc lslash.sc m.sc n.sc nacute.sc ncaron.sc ntilde.sc o.sc oacute.sc ocircumflex.sc odieresis.sc ograve.sc ohungarumlaut.sc omacron.sc oslash.sc otilde.sc oe.sc p.sc thorn.sc q.sc r.sc racute.sc rcaron.sc s.sc sacute.sc scaron.sc germandbls.sc ij.ss03.sc iacute_j.loclnld.ss03.sc t.sc tcaron.sc u.sc uacute.sc ucircumflex.sc udieresis.sc ugrave.sc uhungarumlaut.sc umacron.sc uogonek.sc uring.sc v.sc w.sc x.sc y.sc yacute.sc ydieresis.sc z.sc zacute.sc zcaron.sc zdotaccent.sc".split(" ")

# presetDict["smcpMinList"] = "i.sc z.sc l.sc lslash.sc e.sc f.sc t.sc k.sc x.sc r.sc ae.sc a.sc v.sc w.sc y.sc p.sc thorn.sc j.sc u.sc germandbls.sc b.sc o.sc dcroat.sc oslash.sc q.,sc c.sc g.sc s.sc".split(" ")

# presetDict["quoteList"] = "quoteleft quoteright quotedblleft quotedblright quotesinglbase quotedblbase".split(" ")

# presetDict["operatorList"] = "dollar cent Euro sterling yen uni20BA uni20BD florin currency approxequal equal notequal divide minus plus plusminus multiply logicalnot less greater ,lessequal greaterequal numbersign".split(" ")

# presetDict["mathsList"] = "multiply plus minus divide logicalnot equal notequal approxequal less greater lessequal greaterequal plusminus".split(" ")

presetDictL.update(presetDict)
presetDictR.update(presetDict)

# Delimiters
delimDict = {}
delimDict = collections.OrderedDict()
delimDict['H'] = ['H']
delimDict['O'] = ['O']
delimDict['HH'] = ['H', 'H']
delimDict['HO'] = ['H', 'O']
delimDict['OH'] = ['O', 'H']
delimDict['OO'] = ['O', 'O']
delimDict['n'] = ['n']
delimDict['o'] = ['o']
delimDict['nn'] = ['n', 'n']
delimDict['oo'] = ['o', 'o']
delimDict['no'] = ['n', 'o']
delimDict['on'] = ['o', 'n']
delimDict['zero default'] = ['zero']
delimDict['zero tabular'] = ['zero.tab']

guessDelimDict=presetDict
