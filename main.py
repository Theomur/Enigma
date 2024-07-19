import settings

while (True):
    output = 'Here is your code/text - '
    alphabet = "1234567890 -+*/=qwertyuiop[]asdfghjkl;'zxcvbnm,."

    # file reading preparations
    file = open('Enigma_code/launch codes.txt', 'r')
    file_line = 1
    for line in file:
        if file_line == 1:
            rotor_setup = line
            file_line += 1
        else:
            rotor_start_rotation = line
    file.close()

    # rotors set
    rotor_1_counter = 0
    rotor_2_counter = 0
    rotor_3_counter = 0
    rotor_4_counter = 0
    rotor_5_counter = 0

    rotor_list = {
        '1': settings.rotor1,
        '2': settings.rotor2,
        '3': settings.rotor3,
        '4': settings.rotor4,
        '5': settings.rotor5,
        '6': settings.rotor6,
        '7': settings.rotor7,
        '8': settings.rotor8,
        '9': settings.rotor9,
    }

    rotor1 = rotor_list[rotor_setup[0]]
    rotor2 = rotor_list[rotor_setup[1]]
    rotor3 = rotor_list[rotor_setup[2]]
    rotor4 = rotor_list[rotor_setup[3]]
    rotor5 = rotor_list[rotor_setup[4]]

    all_rotors = [rotor1, rotor2, rotor3, rotor4, rotor5]

    invertor = settings.invertor
    plug_board = settings.plug_board

    # rotors shift set
    num_of_rotor = 0
    for key_lett in rotor_start_rotation:
        while (True):
            if all_rotors[num_of_rotor].in_[0] != key_lett:
                all_rotors[num_of_rotor].rotate()
            else:
                num_of_rotor += 1
                break

    rotor1 = all_rotors[0]
    rotor2 = all_rotors[1]
    rotor3 = all_rotors[2]
    rotor4 = all_rotors[3]
    rotor5 = all_rotors[4]

    # input
    while (1):
        inp_good = True
        print("\n\n\n-------------------------------------------------\n\n"
              "(enter 0 to quit, enter 1 "
              "to change settings, enter 2 to check settings)")
        input_s = input("Enter your text/code -   ")
        input_s = input_s.lower()
        for letter in input_s:
            if letter not in alphabet:
                print("------------Wrong input string------------")
                inp_good = False
                break
        if inp_good:
            break

    # coding/decoding
    for letter in input_s:
        # plug board straight
        plug_str_in_element = letter
        plug_str_out_id = plug_board.out_.index(plug_str_in_element)
        # 1 rotor straight
        rotor_1_str_in_element = rotor1.in_[plug_str_out_id]
        rotor_1_str_out_id = rotor1.out_.index(rotor_1_str_in_element)
        # 2 rotor straight
        rotor_2_str_in_element = rotor2.in_[rotor_1_str_out_id]
        rotor_2_str_out_id = rotor2.out_.index(rotor_2_str_in_element)
        # 3 rotor straight
        rotor_3_str_in_element = rotor3.in_[rotor_2_str_out_id]
        rotor_3_str_out_id = rotor3.out_.index(rotor_3_str_in_element)
        # 4 rotor straight
        rotor_4_str_in_element = rotor4.in_[rotor_3_str_out_id]
        rotor_4_str_out_id = rotor4.out_.index(rotor_4_str_in_element)
        # 5 rotor straight
        rotor_5_str_in_element = rotor5.in_[rotor_4_str_out_id]
        rotor_5_str_out_id = rotor5.out_.index(rotor_5_str_in_element)

        # ---------invertor---------
        inv_in_element = invertor.in_[rotor_5_str_out_id]
        inv_out_id = invertor.out_.index(inv_in_element)

        # rotor 5 reverse
        rotor_5_rev_out_element = rotor5.out_[inv_out_id]
        rotor_5_rev_in_id = rotor5.in_.index(rotor_5_rev_out_element)
        # rotor 4 reverse
        rotor_4_rev_out_element = rotor4.out_[rotor_5_rev_in_id]
        rotor_4_rev_in_id = rotor4.in_.index(rotor_4_rev_out_element)
        # rotor 3 reverse
        rotor_3_rev_out_element = rotor3.out_[rotor_4_rev_in_id]
        rotor_3_rev_in_id = rotor3.in_.index(rotor_3_rev_out_element)
        # rotor 2 reverse
        rotor_2_rev_out_element = rotor2.out_[rotor_3_rev_in_id]
        rotor_2_rev_in_id = rotor2.in_.index(rotor_2_rev_out_element)
        # rotor 1 reverse
        rotor_1_rev_out_element = rotor1.out_[rotor_2_rev_in_id]
        rotor_1_rev_in_id = rotor1.in_.index(rotor_1_rev_out_element)
        # plug board reverse
        plug_rev_out_element = plug_board.out_[rotor_1_rev_in_id]

        # rotation
        if rotor_1_counter == 47:
            if rotor_2_counter == 47:
                if rotor_3_counter == 47:
                    if rotor_4_counter == 47:
                        if rotor_5_counter == 47:
                            rotor1.rotate()
                            rotor2.rotate()
                            rotor3.rotate()
                            rotor4.rotate()
                            rotor5.rotate()

                            rotor_1_counter = 0
                            rotor_2_counter = 0
                            rotor_3_counter = 0
                            rotor_4_counter = 0
                            rotor_5_counter = 0
                        else:
                            rotor1.rotate()
                            rotor2.rotate()
                            rotor3.rotate()
                            rotor4.rotate()
                            rotor5.rotate()

                            rotor_1_counter = 0
                            rotor_2_counter = 0
                            rotor_3_counter = 0
                            rotor_4_counter = 0
                            rotor_5_counter += 1
                    else:
                        rotor1.rotate()
                        rotor2.rotate()
                        rotor3.rotate()
                        rotor4.rotate()

                        rotor_1_counter = 0
                        rotor_2_counter = 0
                        rotor_3_counter = 0
                        rotor_4_counter += 1
                else:
                    rotor1.rotate()
                    rotor2.rotate()
                    rotor3.rotate()

                    rotor_1_counter = 0
                    rotor_2_counter = 0
                    rotor_3_counter += 1
            else:
                rotor1.rotate()
                rotor2.rotate()

                rotor_1_counter == 0
                rotor_2_counter += 1
        else:
            rotor1.rotate()

            rotor_1_counter += 1

        # finished
        output_letter = plug_rev_out_element
        output += output_letter

    if input_s != '0' and input_s != '1' and input_s != '2':
        # output
        print("-------------------------------------------------------------")
        print(output)
    elif input_s == '1':
        # Settings change
        while (True):
            # base veriables
            setup_good = True
            numbers = '123456789'

            print("\n\n\n\n0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0\n")
            print("alphabet = 1234567890 -+*/="
                  "qwertyuiop[]asdfghjkl;'zxcvbnm,.\n")

            # input
            rotor_setup = input('(5 numbers from 1 to 9 which stands '
                                'for numbers of exact rotors. Enter 0 '
                                'for default value)'
                                '\nEnter your rotor setup - ')
            rotor_start_rotation = input('\n(any 5 symbols from alphabet. '
                                         'Enter 0 for default value)\n'
                                         'Enter your rotors start position - ')

            # input check 1
            if len(rotor_setup) == 5:
                for num in rotor_setup:
                    if num not in numbers:
                        setup_good = False
                        print('wrong number in rotor setup, try again')
                        break
            else:
                setup_good = False
                if rotor_setup == '0':
                    rotor_setup = '12345'
                    setup_good = True
                else:
                    print('wrong rotor setup length, try again')

            # input check 2
            if len(rotor_start_rotation) == 5:
                for letter in rotor_start_rotation:
                    if letter not in alphabet:
                        setup_good = False
                        print('wrong letter in '
                              'rotors start position, try again')
                        break
            else:
                setup_good = False
                if rotor_start_rotation == '0':
                    rotor_start_rotation = '9883m'
                    setup_good = True
                else:
                    print('wrong rotors start position length, try again')

            # final descigion
            if setup_good:
                file = open("Enigma_code/launch codes.txt", 'w')
                file.writelines([rotor_setup, '\n', rotor_start_rotation])
                file.close()
                print("\n\n\n\n")
                break
    elif input_s == '2':
        print("\n\nRotors setup - " + rotor_setup)
        print("Rotors rotation start - " + rotor_start_rotation)
    elif input_s == '0':
        break
