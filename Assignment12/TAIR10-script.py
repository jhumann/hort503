import re
import numpy
import pandas as pd
import io

text = open('TAIR10_functional_descriptions.txt', 'r')
text2 = text.read()
results = re.sub(r'.*?(^AT[\d+|\w]G\d+\.\d+|IPR\d+|$).*?', r'\1,', text2, count=0, flags=re.MULTILINE)
results_io = io.StringIO(results)
df = pd.read_csv(results_io, header=None, names=range(15))
df.columns = ['Transcript ID', 'IPR1', 'IPR2', 'IPR3', 'IPR4', 'IPR5', 'IPR7', 'IPR8', 'IPR9', 'IPR10', 'IPR11', 'IPR12', 'IPR13', 'IPR14', 'IPR15']
print(f"df shape = {df.shape}")
annots = df.melt(id_vars='Transcript ID', value_name='IPR Term')
annots = annots.drop('variable', axis=1)
annots = annots.dropna()
print(f"annots shape = {annots.shape}")
print("Saving annots to file called TAIR10-IPRterms.txt")
annots.to_csv('TAIR10-IPRterms.txt', sep='\t', index=False)
