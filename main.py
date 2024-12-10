import difflib
from hashlib import sha1
from colorama import Fore, Style


def content_hasher(content: bytes):
    return sha1(content).hexdigest()


def file_comparer(file_address1: str, file_address2: str):
    with open(r"{}".format(file_address1), 'rb') as file1, open(r"{}".format(file_address2), 'rb') as file2:
        li1 = file1.readline()
        li2 = file2.readline()
        counter = 1
        equal = True
        while li1 or li2:
            hash_li1 = content_hasher(li1)
            hash_li2 = content_hasher(li2)
            matcher = difflib.SequenceMatcher(None, hash_li1, hash_li2)
            line_equal = True
            for tag, i1, i2, j1, j2 in matcher.get_opcodes():
                if tag == "delete":
                    line_equal = False
                    equal = False
                print(f'{tag} {hash_li1[i1:i2]} {hash_li2[j1:j2]}')
            if not line_equal:
                print(Fore.YELLOW + f'in line {counter} The sentences are not equal.' + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"in line {counter} The sentences are equal." + Style.RESET_ALL)

            li1 = file1.readline()
            li2 = file2.readline()
            counter += 1
        else:
            if equal:
                print(Fore.GREEN + 'The two files match.' + Style.RESET_ALL)
            else:
                print(Fore.RED + "The two files doesn't match." + Style.RESET_ALL)


f1 = input('please enter first file address: ')
f2 = input('please enter second file address: ')

file_comparer(f1, f2)
