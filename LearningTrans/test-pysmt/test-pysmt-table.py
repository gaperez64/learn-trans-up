#Basic definitions - the data structures are horrible. Should be generated later.

alphabet = {"a","b","0"}
real_pref = {"","a","b"}
pref = real_pref
for a in alphabet
	for p in real_pref
	pref.add(real_pref+a)
real_suf = {"","0"}
suf = (real_suf | {"EOF"})

Sa_ = ""
Sb_ = "#"
Sa_0 = "1"
Sb_0 = "1"
Sa0_ = "1"
Sb0_ = "1"
Sa0_0 = "11"
Sb0_0 = "11"
S_ = "bot"
S_0 = "bot"
Saa_ = "bot"
Sba_ = "bot"
Saa_0 = "bot"
Sba_0 = "bot"
Sab_ = "bot"
Sbb_ = "bot"
Sab_0 = "bot"
Sbb_0 = "bot"


elem = {}
for p in pref
	for s in suf
		elem.add(p+"_"+s)

#In what follows every def is associated with its domain and formula.
#This is not exactly the right format to be executed yet.
################ def 8.1

domain81 = {}
for e in elem
	STtable.add((eval("S"+e),eval("T"+e)))

And(
	Implies(
			Not(Equals(String(Selement),String("#"))),
			Equals(String(Selement),String(Telement))
			)
	for Selement,Telement in domain81
	)

################ def 8.2

domain82 = {}
for p1 in pref
	for p2 in pref
		for s1 in suf
			for s2 in suf
				if s1+p1 == s2+p2
					domain82.add(eval("T"+s1+"_"+p1),eval("T"+s2+"_"+p2))

And(
	Equals(String(lefte),String(righte))
	for lefte,righte in domain82
	)

################ def 8.3
#Should be reworked - the lcp has to be a prefix of itself, nothing more

domain83 = {}
for p in real_pref
	for a in alphabet
		for s in suf
		domain83pref.add((eval("T"+p+a+"_"+"EOF"),eval("T"+p+a+"_"+s)))

And(
	And(StrPrefixOf(String(prefixcell),String(othercells)),
		ForAll(String(v),Implies(
								StrPrefixOf(
											StrConcat(String(prefixcell),String(v)),
											othercells)
								Equals(String(v),"")
								)
				)
		)
	for prefixcell,othercells in domain83
	)

################ def 9.1

domain91 = {}
for p1 in pref
	for p2 in pref
		for p3 in pref
			domain91.add((
						eval(p1+"_eq_"+p2),
						eval(p2+"_eq_"+p3),
						eval(p1+"_eq_"+p3),
						eval(p2+"_eq_"+p1),
						eval(p1+"_eq_"+p1),
						))

And(
	And(Implies(And(eq12,eq23),eq13),
		Implies(eq12,eq21)
		eq11
		)
	for eq12,eq23,eq13,eq11 in domain91
	)

################ def 9.2

domain92 = {}
for p1 in real_pref
	for a in alphabet
		domain92.add(p1+a)

And(
	Or(
		eval(borderelem+"_eq_"+real_p)
		for real_p in real_pref
		)
	for borderelem in domain92
	)

################ TODO: remaining def. 
#Since lcp is encoded, equiv_T' should be fine.


