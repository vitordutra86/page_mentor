
# ReACT

## Descrição

Induz a IA a pensar, agir, observar o seu resultado e ajustar o seu raciocínio. Essa atividade é ideal para pesquisas em fontes de dados externas.

## Templates (Prompts)

```
Técnica: ReACT
### Input ###
Raciocínio inicial: [Inserir a avaliação preliminar]
Ação: [Pesquisa ou consulta de dados/inclua a fonte se possível]
Novo raciocínio com base nos resultados: [Análise refinada]
### Orientações à IA (modelo) ###
* Requisito obrigatório: jamais invente qualquer jurisprudência. 
* Jamais inclua informações que não sejam encontradas na pesquisa sobre jurisprudência. 
* Procure ser o mais fiel possível ao teor dos julgados consultados.
### Output ###
Resposta final:
### Orientação ao usuário ###
* Insira a necessidade de que a IA trabalhe em loop quando assim desejar.
```
