# Instruções para agentes de assistência (Copilot / AI)

> Resumo rápido: este repositório contém pequenos scripts didáticos em Python (ex.: `FncoesMatematicas.py`, `decisao.py`, `EntradaSaidaDados.py`, `ola_mundo.py`, `repeticao.py`, `repeticaoFor.py`). Todos são programas CLI interativos escritos em português e destinados a execução direta com `python <arquivo>.py` no Windows (PowerShell).

Principais pontos que um agente deve saber
- Arquitetura "big picture": coleção de scripts autônomos (cada arquivo é uma aplicação pequena). Não há pacote, serviços, APIs ou dependências externas — apenas a biblioteca padrão do Python.
- Fluxo de dados comum: entrada via input() (texto em português), conversão direta para `int`/`float`, processamento e saída com `print()` usando f-strings.
- Convenções do projeto: mensagens e nomes em português; arquivos contêm cabeçalho `# -*- coding: utf-8 -*-`. O código assume uso interativo (terminal) e uso de `os.system("cls")` para limpar a tela no Windows.

Padrões e exemplos específicos (copie quando for necessário)
- Função utilitária definida mas não necessariamente invocada (ex.: `FncoesMatematicas.py`):
  - `def raiz_quadrada():` lê um número com `float(input(...))`, valida `num < 0` e usa `math.sqrt(num)`.
- Estrutura de execução principal (quando presente): use o guard `if __name__ == "__main__":` — presente em `ola_mundo.py`.
- Repetição interativa padrão (ex.: `repeticao.py`): loop `while True:` que pergunta `Deseja continuar? (s/n):` e interrompe quando a resposta != 's'. Mantenha essa lógica ao ajustar prompts.
- Repetição por índice (ex.: `repeticaoFor.py`): pede `comeco` e `fim` e usa `for i in range(comeco, fim + 1):` — observe o `+ 1` no fim para incluir o valor final.

Recomendações práticas para alterações por agentes
- Preservar idioma: mantenha prompts e mensagens em português, a menos que o PR peça internacionalização.
- Evitar mudanças não solicitadas no comportamento CLI: se transformar em módulo reutilizável, adicione `if __name__ == "__main__":` para manter compatibilidade com execução direta.
- Limpar imports não usados (ex.: `random` é importado em alguns arquivos mas não usado). Fazer refatorações pequenas localmente e executar o script para validar comportamento interativo.
- Ao automatizar alterações, não remova `os.system("cls")` sem considerar execução em terminal não interativo — documente qualquer mudança que altere a UX.

Como executar e depurar (Windows / PowerShell)
```
python .\FncoesMatematicas.py
python .\decisao.py
python .\repeticao.py
# ou, se estiver instalado, use: py .\<arquivo>.py
```

Para depurar no VS Code: abra o arquivo desejado, coloque breakpoints no código (ex.: antes do `input()`), e inicie a configuração de execução/Debug do Python. O repositório não tem testes automatizados nem CI configurado.

Coisas que o agente não deve presumir
- Não há bancos de dados, APIs externas nem arquivos de configuração. Não adicionar integrações externas sem instruções do autor.
- Não há suíte de testes ou linter configurado — qualquer adição deverá vir acompanhada de instruções de execução.

Arquivos chave para referência rápida
- `FncoesMatematicas.py` — função `raiz_quadrada()`; usa `math.sqrt` e lê `float` do usuário.
- `decisao.py` — exemplo simples de condição (par/ímpar) usando `if/else`.
- `EntradaSaidaDados.py` — exemplo de soma de dois números com `float(input(...))`.
- `ola_mundo.py` — contém `main()` e `if __name__ == "__main__":`.
- `repeticao.py` e `repeticaoFor.py` — exemplos de `while` interativo e `for` com intervalo.

Se algo estiver ambíguo ou você precisar que eu preserve/exclua detalhes (por exemplo: traduzir para inglês, adicionar testes, transformar em pacote), peça instruções específicas antes de executar mudanças maiores.

-- Fim --
