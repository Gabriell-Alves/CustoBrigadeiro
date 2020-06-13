leiteCondesado  = 3.00
cremeDeLeite    = 2.50
manteiga        = 7.00
forma           = 0.90
chocolate       = 13.00
cocoRalado      = 25.00
leiteCoco       = 3.50
ninho           = 12.00
castanha        = 40.00
pacoca          = 14.00
cacau           = 17.00
nutela          = 20.00
doceLeite       = 14.00
canela          = 3.00

print("Brigadeiro Tradicional")
vt_tradicional = 1.25*(leiteCondesado + 0.02 * manteiga + 0.02*chocolate)
vb_tradicional = vt_tradicional/27
print("Custo da Receita: ", "{:.2f}".format(vt_tradicional))
print("Custo unitário:   ", "{:.2f}".format(vb_tradicional))

print("----------------------------------------------")

print("Beijinho")
vt_beijinho = 1.25 *(leiteCondesado + manteiga*0.02 + cocoRalado*0.1 + leiteCoco*0.2)
vb_beijinho = vt_beijinho/30
print("Custo da Receita: ", "{:.2f}".format(vt_beijinho))
print("Custo unitário:   ", "{:.2f}".format(vb_beijinho))

print("----------------------------------------------")

print("Leite Ninho")
vt_ninho = 1.25*(leiteCondesado + manteiga*0.02 + ninho*0.05)
vb_ninho = vt_ninho /19
print("Custo da Receita: ", "{:.2f}".format(vt_ninho))
print("Custo unitário:   ", "{:.2f}".format(vb_ninho))

print("----------------------------------------------")

print("Castanha de Caju")
vt_castanha = 1.25*(leiteCondesado + manteiga*0.02 + castanha*0.1)
vb_castanha = vt_castanha /35
print("Custo da Receita: ", "{:.2f}".format(vt_castanha))
print("Custo unitário:   ", "{:.2f}".format(vb_castanha))

print("----------------------------------------------")

print("Paçoca")
vt_pacoca = 1.25*(leiteCondesado + manteiga*0.02 + pacoca*0.1)
vb_pacoca = (vt_pacoca /35)+0.06
print("Custo da Receita: ", "{:.2f}".format(vt_pacoca))
print("Custo unitário:   ", "{:.2f}".format(vb_pacoca))

print("----------------------------------------------")

print("100%Cacau")
vt_cacau = 1.25*(leiteCondesado + manteiga*0.02 + cacau*0.04)
vb_cacau = vt_cacau /21
print("Custo da Receita: ", "{:.2f}".format(vt_cacau))
print("Custo unitário:   ", "{:.2f}".format(vb_cacau))

print("----------------------------------------------")

print("Ninho com Nutella")
vt_nutela = 1.25*(leiteCondesado + manteiga*0.02 + ninho*0.05)
vb_nutela = (vt_nutela /24) + nutela*0.006
print("Custo da Receita: ", "{:.2f}".format(vt_nutela))
print("Custo unitário:   ", "{:.2f}".format(vb_nutela))

