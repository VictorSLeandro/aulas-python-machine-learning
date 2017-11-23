arq = open('arquivo.txt','w')
arq.write('machine learning')
arq.write('\naprendendo python')
text = '''
\nAprendendo python
python e muito legal
machine learning
'''
arq.write(text)
arq.close()
