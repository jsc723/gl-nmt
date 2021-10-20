import subprocess
import os
import time

class KyteaTokenizer(object):
    def __init__(self, kytea_root, model_path):
        exe = os.path.abspath(os.path.join(kytea_root, 'kytea.exe')) if kytea_root else 'kytea'
        args = [exe, '-notags']
        if kytea_root:
            print('kytea exe path:' + exe)
        if model_path:
            print('kytea model path:' + os.path.abspath(model_path))
            args.extend(['-model', os.path.abspath(model_path)])
        self.p = subprocess.Popen(args,
                    stdin=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf-8')

        
    def tokenize(self, text):
        self.p.stdin.write(text + '\n')
        self.p.stdin.flush()
        self.p.stdout.flush()
        res = self.p.stdout.readline()
        return res
    
    def detokenize(self, sequence):
        print(sequence)
        return ''.join(sequence)

if __name__ == '__main__':
    kytea = KyteaTokenizer('../../available_models/kytea-win-0.4.2', '../../available_models/kytea-win-0.4.2/model.bin')
    print(kytea.tokenize('地域振興の完全なる失敗例としてアニメ史に名を\\n刻むことになったわけだが、お偉いさんはその事実を\\n知らないのか、それとも認めたくないのか。'))
    print(kytea.tokenize('この過程を調べる中で，著者らは家庭間の違いに焦点を合わせた。'))
