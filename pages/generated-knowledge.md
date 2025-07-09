
# Generated Knowledge

## Descrição

Solicita ao modelo para criar um conhecimento de base antes de desenvolver a resposta final, como uma síntese de fatos relevantes, induzindo-o a raciocinar (pensar antes de responder). Em suma, a ideia é que o modelo primeiro pesquise, depois responda. Isso reduz o desperdício de tempo e recursos, já que pode conferir o que a IA irá desenvolver antes de começar a produção final da resposta.

## Templates (Prompts)

```
Técnica: Generated Knowledge
### Input ###
[Descrição do caso/problema]
### Processamento: Geração de Conhecimento ###
1) [Aspectos legais relevantes]
2) [Doutrina e jurisprudência predominante]
3) [Outros]
### Orientações ao usuário ###
* Altere os dados relacionados ao processamento (geração de conhecimento) caso necessário.
### Output ###
Resposta final fundamentada:
```
