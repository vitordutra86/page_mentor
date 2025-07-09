
# Delimitadores

## Descrição

Os delimitadores não apenas podem melhorar a análise do prompt, mas também facilitar a separação de contexto, reduzir ambiguidade e promover melhor consistência de saída. 

## Templates (Prompts)

```
Técnica: Uso de delimitadores
### Objetivo
Refatore o prompt a seguir, organizando-o com base nas boas práticas de estruturação de prompts para IA.

### Instruções à IA
Você deverá reestruturar o conteúdo fornecido, utilizando os seguintes **delimitadores padronizados**:

- `###` para seções principais (ex: `### Objetivo`, `### Perfil do Modelo`, `### Tarefas`, `### Saída Esperada`)
- `<Tags>` para marcações contextuais internas, opcionais (ex: `<Exemplo>`, `<Nota>`, `<Orientação Interna>`)
- Colchetes `[ ]` para campos que deverão ser personalizados pelo usuário ou pela IA no uso futuro do prompt
- Blocos de código com **três crases (``` )** para destacar instruções, trechos legais, exemplos ou comandos técnicos

### Restrições
- **Não invente** informações novas no conteúdo original.
- **Não modifique o sentido** do texto do prompt original.
- **Não remova** nenhuma instrução relevante presente no texto.
- Caso alguma parte esteja incompleta, sinalize com `<[INCOMPLETO]>` em colchetes.

### Prompt Original
```markdown
[COLE AQUI O PROMPT ORIGINAL QUE DEVE SER REESTRUTURADO]
```
