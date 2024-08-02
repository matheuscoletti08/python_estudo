# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação. 

anumber = 8000;
aprcntg = 3;
bnumber = 200000;
bprcntg = 1.5;
anos = 0;
while (anumber <= bnumber):
    anumber = anumber + (anumber * aprcntg / 100);
    bnumber = bnumber + (bnumber * bprcntg / 100);
    anos = anos + 1;
print(f"a quantidade de anos é: " + str(anos) + " anos")