# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 

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