def main():
    new_file = open('mod3numlist.txt', 'r')
    try:
        line1 = new_file.readline()
        even_list = []
        odd_list = []

        while line1 != '':
            x = line1.rstrip('\n').split()

            for item in x:
                valid_num = int(item) 
                if (valid_num % 2) == 0:
                    even_list.append(valid_num)
                else:
                    odd_list.append(valid_num)

            line1 = new_file.readline()

        new_file.close()

        create_even(even_list)

        create_odd(odd_list)

    except FileNotFoundError as e:
        print('File name is invalid or does not exist')


def create_even(even_list):
    even_file = open('evennumbers.txt', 'a')
    for num in even_list:
        even_file.write(str(num) + '\n') 
    even_file.close()


def create_odd(odd_list):
    odd_file = open('oddnumbers.txt', 'a')
    for num in odd_list:
        odd_file.write(str(num) + '\n') 
    odd_file.close()


main()
