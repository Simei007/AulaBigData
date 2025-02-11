# para fazer o commit para o github
# git commit -m "Adicionando código do projeto AulaBigData"
# para fazer o push para o github
# git push origin main
import pandas as pd
df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'], 'value': [1, 2, 3, 5]})
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'], 'value': [5, 6, 7, 8]})
df1.merge(df2, left_on='lkey', right_on='rkey')
