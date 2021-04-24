import etao
import pycipher as pc

def caesar_scorer(string): 
	qwe=[] 
	for i in range(26): 
			qwe.append(etao.scorers.NgramFrequencyScorer().score(etao.CaesarCipher(i).encrypt(string))) 
	return 26-qwe.index(max(qwe))

def main():
	with open('data.txt') as file:
		asd = file.read()
	length = len(asd)
	# asd = "BELOSZ"
	## Keylength finder
	for i in range(1,20):
		print(i, sum(pc.util.ic(asd[j::i]) for j in range(i))/i)
	wide = 9
	## Decoder
	# _key = ''.join([etao.num_to_letter((caesar_scorer(asd[i::wide])+1)%26+1) for i in range(wide)])
	# print("Key =", _key)
	# key = "keylength"
	# ans = pc.Vigenere(_key).decipher(asd)
	# print(ans)
	# BELOS Z

if __name__ == '__main__':
	main()
	string="mel mm melqklnmdsk udklnaapk gm'nrrsllugtn tm spisknaa vc nmn pmhlltsenaamslcplst mcvdnug ns cs cnm ncsgcdsl m an"
	caesar_scorer(string)