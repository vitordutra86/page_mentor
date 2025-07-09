
# Json

## Descrição

O JSON permite que a IA organize informações em um formato padronizado, hierárquico e prontamente integrável a sistemas, APIs, planilhas, dashboards ou automações.

## Templates (Prompts)

```
Técnica: Estruturação em formato Json
### CONTEXTO ###
[Descreva o cenário, os dados e o papel do modelo.]
### TAREFA ###
Gere a resposta exclusivamente no formato JSON, seguindo esta estrutura:

{
  "titulo": "[Título do documento]",
  "contexto": "[Descrição do contexto]",
  "fundamentacao": {
    "formal": "[Análise formal]",
    "material": ["[Princípio 1]", "[Princípio 2]"]
  },
  "jurisprudencia": [
    {
      "tribunal": "[Tribunal]",
      "ementa": "[Resumo da decisão]"
    }
  ],
  "conclusao": "[Síntese final]"
}

### Orientações ao modelo de IA ###
- Não inclua textos fora da estrutura JSON.
- Utilize apenas dados pertinentes.
- Caso não haja dados para algum campo, retorne null.

### EXECUTE ###
```
