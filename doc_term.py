import pandas as pd
import textmining
tdm = textmining.TermDocumentMatrix()

sentence1 = "I love football"
sentence2 = "Messi is a great football player"
sentence3 = "Messi has won seven Ballon d’Or awards "
for i in range(1,1401):
    file_path = str(i) + '.txt'
    print('Reading ' + file_path)
    with open(file_path) as f:

        lines = f.read()   
        tdm.add_doc(lines)
    f.close()
tdm=tdm.to_df(cutoff=0)
tdm.to_csv(r'C:\Users\T440S01\CS431\export_dataframe.csv', index = False, header=True)
print(tdm)