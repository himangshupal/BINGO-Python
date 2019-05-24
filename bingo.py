import random

def build_bingo_data():
    b_list = []
    i_list = []
    n_list = []
    g_list = []
    o_list = []
    data = []
    bingo_dict = {}

    # Create B list
    for i in range(1,16):
        b_list.append(random.randrange(1, 15))

    b_list = set(b_list)
    data = random.sample(b_list,5)
    b_list = data
    #print(b_list)

    # Create I list
    for i in range(16, 31):
        i_list.append(random.randrange(16, 31))

    i_list = set(i_list)
    data = random.sample(i_list,5)
    i_list = data
    #print(i_list)


    # Create N list
    for i in range(16):
        n_list.append(random.randrange(31, 46))

    n_list = set(n_list)
    data = random.sample(n_list,5)
    n_list = data
    #print(n_list)

    # Create G list
    for i in range(16):
        g_list.append(random.randrange(46,61))

    g_list = set(g_list)
    data = random.sample(g_list,5)
    g_list = data
    #print(g_list)

    # Create O list
    for i in range(16):
        o_list.append(random.randrange(61, 76))

    o_list = set(o_list)
    data = random.sample(o_list,5)
    o_list = data
    #print(o_list)

    bingo_dict ={'b':b_list, 'i':i_list, 'n':n_list, 'g':g_list, 'o':o_list}

    #print(bingo_dict)
    return bingo_dict


def display_bingo_table(dict):

    #This function is to display Bingo table.

    table = [""] * 26
    position = 21

    for i in dict['b']:
        table[position] = str(i)
        position -= 5

    position = 22
    for i in dict['i']:
        table[position] = str(i)
        position -= 5

    position = 23
    for i in dict['n']:
        table[position] = str(i)
        position -= 5

    position = 24
    for i in dict['g']:
        table[position] = str(i)
        position -= 5

    position = 25
    for i in dict['o']:
        table[position] = str(i)
        position -= 5

    print("|---------------")
    print("| " + table[21] + "|" + table[22] + "|" + table[23] + "|" + table[24] + "|" + table[25] + "|")
    print("|---------------")
    print("| " + table[16] + "|" + table[17] + "|" + table[18] + "|" + table[19] + "|" + table[20] + "|")
    print("|---------------")
    print("| " + table[11] + "|" + table[12] + "|" + table[13] + "|" + table[14] + "|" + table[15] + "|")
    print("|---------------")
    print("| " + table[6] + "|" + table[7] + "|" + table[8] + "|" + table[9] + "|" + table[10] + "|")
    print("|---------------")
    print("| " + table[1] + "|" + table[2] + "|" + table[3] + "|" + table[4] + "|" + table[5] + "|")
    print("|---------------")




def main():
    print("Let's play BINGO!!!\n")
    data = build_bingo_data()

    print("Here is your BINGO card\n")
    display_bingo_table(data)

main()