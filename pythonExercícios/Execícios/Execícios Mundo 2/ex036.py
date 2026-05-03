valorCasa = float(input('Qual é o seu preço da casa?: '))
salario = float(input('Qual é o seu salário?: '))
anos = int(input('Em quantos anos você ira pagar?: '))
parcelaMensal = valorCasa/(anos*12)   
if parcelaMensal<=(salario/100)*30:
    print(f"Parabens, seu emprestimo foi aprovado, a parcela do pagamento mensal será {parcelaMensal:.2f}R$.")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
else:
    print(f'Empréstimo não aprovado. Sua parcela seria de R${parcelaMensal:.2f}, mas 30% do seu salário é R${salario * 0.30:.2f}')