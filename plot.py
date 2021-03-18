import pandas as pd

df = pd.read_csv('part-r-00000.txt',
				sep="(", header=None)

df = df[24:54]

new = df[0].str.split("\\s", n=1, expand=True)

new.columns = ['Word','freq']

new['Word'] = new['Word'].str.replace('[^\w\s]','')
new['freq'] = new['freq'].fillna(0)
new['freq'] = pd.to_numeric(new['freq'])

new.plot(kind='bar',
		x='Word',
		y='freq',
		color = 'red')
