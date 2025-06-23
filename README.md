# ibovespa-stocks

O comando: print ( df.loc [ df [ 'ticker' ] == 'BBAS3', 'close'].mean ( ) )

faz o seguinte:

* Filtra o DataFrame `df` para linhas onde a coluna `'ticker'` é igual a `'BBAS3'`.
* Seleciona a coluna `'close'` dessas linhas filtradas.
* Calcula a média (`mean()`) dos valores selecionados.
* Imprime o resultado.
