import math

def calc_hp(shuzokuchi, kotaichi, doryokuchi, level):
    return (shuzokuchi * 2 + kotaichi + doryokuchi // 4) * level // 100 + level + 10

def calc(shuzokuchi, kotaichi, doryokuchi, level, seikaku):
    return math.floor(((shuzokuchi * 2 + kotaichi + doryokuchi // 4) * level // 100 + 5) * seikaku)

def main():
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
                        pair['H'].append(sh)
                        break
                else:
                    if status[c] == calc(sh, ko, 0, level, hosei[c]):
                        pair[c].append(sh)
                        break

    msg = input('続けますか?(y/n)\n> ')
    while(msg == 'y'):
        status = {'H': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'S': 0}
        status['H'], status['A'], status['B'], status['C'], status['D'], status['S'] = map(int, input('ステータスを空白区切りで入れてください\n> ').split(' '))
        character = input('性格を入れてください (S↑A↓ならSA, 無補正ならAA)\n> ')
        level = int(input('レベルを入力してください\n> '))
        hosei = {'A': 1.0, 'B': 1.0, 'C': 1.0, 'D': 1.0, 'S': 1.0}
        if character[0] != character[1]:
            hosei[character[0]] = 1.1
            hosei[character[1]] = 0.9
        for c in l:
            new_sh = []
            for sh in pair[c]:
                for ko in range(32):
                    if c == 'H':
                        if status[c] == calc_hp(sh, ko, 0, level):
                            new_sh.append(sh)
                            break
                    else:
                        if status[c] == calc(sh, ko, 0, level, hosei[c]):
                            new_sh.append(sh)
                            break
            pair[c] = new_sh
        msg = input('続けますか?(y/n)\n> ')

    if name == "":
        for c in l:
            print(c)
            for sh in pair[c]:
                print(sh, end=' ')
            print("")
    else:
        with open(name+'.txt', 'w') as f:
            for c in l:
                f.write(c + '\n')
                for sh in pair[c]:
                    f.write(str(sh) + ' ')
                f.write('\n')

if __name__ == '__main__':
    main()