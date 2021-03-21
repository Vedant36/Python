
qwe = list()

def lis(seq, depth = 0):
    global qwe
    if depth == len(seq):
        qwe.append()

    for i in seq:
        if i>seq[depth]:
            return lis(seq, depth+1)

def _lis(seq):
    wer = [1]*len(seq)
    for i in range(1,len(wer)):
        sub = [wer[k] for k in range(i) if seq[k]>seq[i]]
        wer[i] = 1 + max(sub, default=0)
    return wer,max(wer, default=0)

def main():
    import numpy as np
    '''
    n = 10
    seq = np.arange(n)
    np.random.shuffle(seq)
    '''
    # seq = [5,2,8,6,3,6,9,5]
    seq = [3,1,8,2,5]
    # '''
    print(_lis(seq))

if __name__ == '__main__':
    main()