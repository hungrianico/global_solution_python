from datetime import date
from tabulate import tabulate

print(
    """
=========================== INTRODUÇÃO MONITOR DE VALIDADE DE ALIMENTOS ===============================
Problema: muitos alimentos são jogados fora porque passam da validade sem
que ninguém perceba, gerando desperdício e gastos desnecessários.\n

Público: famílias, moradores de casas e apartamentos e pequenos comércios.\n

Objetivo: cadastrar alimentos, ordena-los em uma tabela em ordem de prioridade e sugerir ação\n

ODS 12: Consumo e Produção Responsáveis (meta 12.3, reduzir o desperdício de alimentos).\n

ODS 2: Fome Zero (aproveitar melhor os alimentos disponíveis).
=======================================================================================================
    """
)
alimentos = []


def cadastro():

    sair = 0

    while sair == 0:

        escolha = str(input("Deseja cadastrar um produto?(s/n): ")).strip().lower()
        if escolha == "n":
            sair = 1
        elif escolha == "s":
            nome = str(input("Insira o nome do alimento: ")).strip()
            if nome == "":
                print("O nome está vazio, tente novamente")
                continue
            try:
                dia = int(input("Dia da validade: "))
                mes = int(input("Mes da validade: "))
                ano = int(input("Ano da validade: "))
                validade = date(ano, mes, dia)
            except ValueError:
                print("Data invalida, insira uma data na ordem dia/mes/ano")
            else:
                alimento = {
                    "nome": nome,
                    "validade": validade,
                }

                alimentos.append(alimento)
        else:
            print(
                'Entrada inválida, digite "s" para sim, cadastrar um alimento ou "n" para não cadastrar um alimento '
            )


def prioridade(dias):
    if dias < 0:
        return "Alimento fora da validade"
    elif dias <= 3:
        return "Consumir urgentemente"
    elif dias <= 10:
        return "Consumir em breve"
    else:
        return "Prazo ainda distante"


def tabela():
    alimentos_sortados = []
    vencidos = 0
    urgentes = 0

    if len(alimentos) == 0:
        print("Nenhum alimento registrado")
        return

    for alimento in alimentos:
        alimento["dias"] = (alimento["validade"] - date.today()).days

    for alimento in alimentos:
        if prioridade(alimento["dias"]) == "Alimento fora da validade":
            alimentos_sortados.append(alimento)
            vencidos += 1

    for alimento in alimentos:
        if prioridade(alimento["dias"]) == "Consumir urgentemente":
            alimentos_sortados.append(alimento)
            urgentes += 1

    for alimento in alimentos:
        if prioridade(alimento["dias"]) == "Consumir em breve":
            alimentos_sortados.append(alimento)

    for alimento in alimentos:
        if prioridade(alimento["dias"]) == "Prazo ainda distante":
            alimentos_sortados.append(alimento)

    linhas = []
    for alimento in alimentos_sortados:
        status = prioridade(alimento["dias"])
        coisas = [
            alimento["nome"],
            alimento["validade"].strftime("%d/%m/%Y"),
            alimento["dias"],
            status,
        ]
        linhas.append(coisas)
    print(
        tabulate(
            linhas,
            headers=["nome", "validade", "dias restantes", "prioridade"],
            tablefmt="rounded_grid",
        )
    )
    print(
        f"Você tem {len(alimentos)} alimentos registrados, {urgentes} alimentos de prioridade urgente de consumo e {vencidos} alimentos vencidos."
    )

    if vencidos > 0:
        print("Descarte os alimentos vencidos")
    if urgentes > 0:
        print(
            f"Coma cerca de {(urgentes / 3):.1f} dos alimentos urgentes por dia para consumir a tempo"
        )
    if vencidos == 0 and urgentes == 0:
        print("Pode consumir seus alimentos com calma")


def menu():
    fechar_menu = 0

    while fechar_menu == 0:
        print(
            """
            [1] CADASTRAR ALIMENTOS
            [2] MOSTRAR TABELA
            [3] ENCERRAR
            """
        )
        opcao = str(input("Escolha uma das opções: ")).strip()
        if opcao not in ["1", "2", "3"]:
            print("Opção inválida, tente novamente")
            continue
        elif opcao == "1":
            cadastro()
        elif opcao == "2":
            tabela()
        elif opcao == "3":
            fechar_menu = 1


menu()
