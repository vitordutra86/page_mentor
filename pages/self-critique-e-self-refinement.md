
# Self-critique e Self-refinement

## Descrição

Simula a metacognição (capacidade de pensar sobre o próprio pensamento). Conduz a IA a refletir sobre a sua própria resposta e depois reproduzir algo mais qualificado. Com o self-critique a IA realiza um diagnóstico, apontando falhas, lacunas e oportunidades de melhoria. Com o self-refinement, a IA aperfeiçoa a resposta iterativamente (refinamento), na implementação das soluções. As duas técnicas devem ser combinadas na sequência em que foram expostas.

## Templates (Prompts)

```
Técnica: Self-critique
### Input ###
Resposta inicial: [Descrição do caso/problema/argumentos]
### Self-Critique ###:
- Erros identificados: [Listagem dos erros]
- Fragilidades ou omissões: [Pontos frágeis ou omissos]
- Sugestões de melhoria: [Propostas de aperfeiçoamento]
### Output ###
Conclusão da crítica:

Técnica: Self-refinement
### Input ###
Resposta original revisada (self-critique): [Pontos para correção identificados]
### Etapas de refinamento iterativo ###:
1ª versão ajustada: [Alterações aplicadas]
2ª versão ajustada: [Novas melhorias após segunda revisão]
### Output ###
Resposta final aperfeiçoada:
```
