import etao
import pycode
asd='''
mel mm melqklnmdsk udklnaapk gm'nrrsllugtn tm spisknaa vc nmn pmhlltsenaamslcplst mcvdnug ns cs cnm ncsgcdsl m an
'''
asd=asd[1:-1].lower()
qwe=asd
lea=len(qwe)
# print(f'String => |\n{asd}|')
print(f'Length => |{lea}|')
def val(a):return(ord(a)-97)
wer='abcdefghijklmnopqrstuvwxyz'
# key='sjqbcgudnvwzmtxeyklaifroph'
key='--------------------------'
cht='etaoinshrldcumfgpwybvkjxzq'
#		 ------.----...-.--...--...

def conv(sd):
	sd0=[]
	for i in sd:
		sd1=[]
		for j in i:
			sd1.append(j if j not in key else cht[key.index(j)].upper())
			# sd1.append('-' if j not in key else cht[key.index(j)])
		sd0.append(''.join(sd1))
	return sd0
def order(sd):
	ert = sorted(sd.keys(),key=lambda a:sd[a],reverse=True)
	# return ert
	return list(zip(ert,conv(ert)))
# print(*sorted([[asd.count(i),i,con(i)] for i in set(asd)],reverse=True),sep='\t',end='\n\n')
print(order(etao.ngram_frequency(asd,1)))
print(order(etao.ngram_frequency(asd,2))[:30])
print(order(etao.ngram_frequency(asd,3))[:30])
print(order(etao.ngram_frequency(asd,4))[:30])
print(order(etao.ngram_frequency(asd,5))[:30])
print(''.join(conv([asd])))
print('Key =>',''.join([key[cht.index(i)] for i in wer]))
