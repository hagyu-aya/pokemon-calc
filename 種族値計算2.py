from 種族値計算 import calc, calc_hp

name = input('ポケモン名を入力してください(任意)\n> ')
status = {'H': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'S': 0}
status['H'], status['A'], status['B'], status['C'], status['D'], status['S'] = map(int, input('ステータスを空白区切りで入れてください\n> ').split(' '))
character = input('性格を入れてください (S↑A↓ならSA, 無補正ならAA)\n> ')
level = int(input('レベルを入力してください\n> '))

hosei = {'A': 1.0, 'B': 1.0, 'C': 1.0, 'D': 1.0, 'S': 1.0}
if character[0] != character[1]:
    hosei[character[0]] = 1.1
    hosei[character[1]] = 0.9

l = ['H', 'A', 'B', 'C', 'D', 'S']
pair = {'H': [], 'A': [], 'B': [], 'C': [], 'D': [], 'S': []}

for c in l:
    for sh in range(300):
        for ko in range(32):
            if c == 'H':
                if status['H'] == calc_hp(sh, ko, 0, level):
                    pair['H'].append((sh, ko))
            else:
                if status[c] == calc(sh, ko, 0, level, hosei[c]):
                    pair[c].append((sh, ko))

msg = input('続けますか?(y/n)\n> ')
while msg == 'y':
    status = {'H': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'S': 0}
    status['H'], status['A'], status['B'], status['C'], status['D'], status['S'] = map(int, input('ステータスを空白区切りで入れてください\n> ').split(' '))
    level = int(input('レベルを入力してください\n> '))
    for c in l:
        new_sh = []
        for (sh, ko) in pair[c]:
            if c == 'H':
                if status[c] == calc_hp(sh, ko, 0, level):
                    new_sh.append((sh, ko))
            else:
                if status[c] == calc(sh, ko, 0, level, hosei[c]):
                    new_sh.append((sh, ko))
        pair[c] = new_sh
    msg = input('続けますか?(y/n)\n> ')

if name == "":
    for c in l:
        print(c)
        for (sh, ko) in pair[c]:
            print(sh, end=' ')
        print("")
else:
    with open(name+'2.txt', 'w') as f:
        for c in l:
            f.write(c + '\n')
            for (sh, ko) in pair[c]:
                f.write('(' + str(sh) + ', ' + str(ko) + ')' + ' ')
            f.write('\n')

