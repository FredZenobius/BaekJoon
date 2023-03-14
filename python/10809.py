word = input()
abc_list = {
    'a' : -1, 'b' : -1, 'c' : -1, 'd' : -1, 'e' : -1, 'f' : -1, 'g' : -1, 'h' : -1,
    'i' : -1, 'j' : -1, 'k' : -1, 'l' : -1, 'm' : -1, 'n' : -1, 'o' : -1, 'p' : -1,
    'q' : -1, 'r' : -1, 's' : -1, 't' : -1, 'u' : -1, 'v' : -1, 'w' : -1, 'x' : -1,
    'y' : -1, 'z' : -1
}
for i in range(len(word)):
    if word[i] == 'a' and abc_list['a'] == -1:
        abc_list['a'] = i
    elif word[i] == 'b' and abc_list['b'] == -1:
        abc_list['b'] = i
    elif word[i] == 'c' and abc_list['c'] == -1:
        abc_list['c'] = i
    elif word[i] == 'd' and abc_list['d'] == -1:
        abc_list['d'] = i
    elif word[i] == 'e' and abc_list['e'] == -1:
        abc_list['e'] = i
    elif word[i] == 'f' and abc_list['f'] == -1:
        abc_list['f'] = i
    elif word[i] == 'g' and abc_list['g'] == -1:
        abc_list['g'] = i
    elif word[i] == 'h' and abc_list['h'] == -1:
        abc_list['h'] = i
    elif word[i] == 'i' and abc_list['i'] == -1:
        abc_list['i'] = i
    elif word[i] == 'j' and abc_list['j'] == -1:
        abc_list['j'] = i
    elif word[i] == 'k' and abc_list['k'] == -1:
        abc_list['k'] = i
    elif word[i] == 'l' and abc_list['l'] == -1:
        abc_list['l'] = i
    elif word[i] == 'm' and abc_list['m'] == -1:
        abc_list['m'] = i
    elif word[i] == 'n' and abc_list['n'] == -1:
        abc_list['n'] = i
    elif word[i] == 'o' and abc_list['o'] == -1:
        abc_list['o'] = i
    elif word[i] == 'p' and abc_list['p'] == -1:
        abc_list['p'] = i
    elif word[i] == 'q' and abc_list['q'] == -1:
        abc_list['q'] = i
    elif word[i] == 'r' and abc_list['r'] == -1:
        abc_list['r'] = i
    elif word[i] == 's' and abc_list['s'] == -1:
        abc_list['s'] = i
    elif word[i] == 't' and abc_list['t'] == -1:
        abc_list['t'] = i
    elif word[i] == 'u' and abc_list['u'] == -1:
        abc_list['u'] = i
    elif word[i] == 'v' and abc_list['v'] == -1:
        abc_list['v'] = i
    elif word[i] == 'w' and abc_list['w'] == -1:
        abc_list['w'] = i
    elif word[i] == 'x' and abc_list['x'] == -1:
        abc_list['x'] = i
    elif word[i] == 'y' and abc_list['y'] == -1:
        abc_list['y'] = i
    elif word[i] == 'z' and abc_list['z'] == -1:
        abc_list['z'] = i

for i in abc_list.values() :
    print(i, end=' ')