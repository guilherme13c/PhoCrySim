# PhoCrySim

Biblioteca para simular circuitos ópticos em Python, permitindo a integração em alto nível de componentes de computação fotônica. Permite cálculo da perda e da potência dos valores de saída, dentre outras informações físicas do circuito.

## Estrutura do projeto

`LumericalValues`: Contém os dados de saída e perda dos componentes, pré-calculados através do simulador fotônico Lumerical.

`components.py`: Biblioteca que define os componentes ópticos.

`main.py`: Exemplo de programa que implementa a simulação de um circuito.

## Como usar

Cada componente importado da biblioteca `components.py` possui seu método `calculate`, que recebe as potências dos seus sinais de entrada, medidas em miliwatts, e retorna a potência do sinal de saída resultante (incluindo o dreno, se houver). Esses valores de saída podem ser, por sua vez, usados como entrada de um novo componente, assim permitindo a criação de qualquer circuito.