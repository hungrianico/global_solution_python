# Monitor de Validade de Alimentos

## Integrantes
- **RM 576186:** Matheus Regis Kabakian Albano
- **RM 574606:** Nico Hungria Santos
- **RM 575140:** Hilda Bonnibel de Oliveira Sousa Dias
## Video pitch


https://github.com/user-attachments/assets/9f3a6297-a50a-4645-82d0-fd7a6cf59fa4


## Problema escolhido
Desperdício de alimentos  
Público beneficiado: [famílias, pequenos comércios etc.].

## ODS relacionados
- ODS 12 - Consumo e Produção Responsáveis
- ODS 2 - Fome Zero

## Como executar
1. Instale o Python 3.
2. No terminal de sua IDE ou de seu computador instale o tabulate, o modulo datetime já é nativo do python então não é necessária a instalação
``` pip install tabulate ```
3. Execute o arquvio GS_PYTHON_1CCPB.py
4. Use o menu para cadastrar um alimento, mostrar a tabela com sugestões de ação ou encerrar o programa

## Regras de classificação
Calculada pelos dias restantes até a validade:
- Menos de 0 dias: Alimento fora da validade
- De 0 a 3 dias: Consumir urgentemente
- De 4 a 10 dias: Consumir em breve
- Mais de 10 dias: Prazo ainda distante

## O que o programa faz
- Cadastra alimentos (nome e data de validade)
- Mostra uma tabela ordenada da mais grave para a menos grave.
- Indicadores: total de alimentos, quantidade de urgentes e de vencidos.
- Recomenda ação como por ex: descarte dos alimentos vencidos, consumo por dia dos alimentos de consumo urgente ou sugere consumir com calma

## Exemplo de teste
Entrada: leite (vence amanhã), macarrão (vence em 33 dias), iogurte (já vencido).  
Resultado:  
| nome     | validade   |   dias restantes | prioridade                |
|----------|------------|------------------|---------------------------|
| iogurte  | 10/11/2026 |               -7 | Alimento fora da validade |
| leite    | 18/11/2026 |                1 | Consumir urgentemente     |
| Macarrao | 20/12/2026 |               33 | Prazo ainda distante      |  

Você tem 3 alimentos registrados, 1 alimentos de prioridade urgente de consumo e 1 alimentos vencidos.
Descarte os alimentos vencidos

## Limitações
Os dados ficam só em memória e se perdem ao encerrar o programa.
