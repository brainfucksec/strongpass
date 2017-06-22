#!/usr/bin/env python3

# Program: strongpass.py
# Version: 3.4.2
# Description: Generate strong random passwords 
# 
# Copyright (C) 2015-2017 Brainfuck 

# GNU GENERAL PUBLIC LICENSE
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Yo, infoencrypt.com/safe/ESWBRRv8mePygbN2K la pass è il forum dove abbiamo "iniziato" senza il .net
#
#
""" For generate passwords, used new module 'secrets' instead of random, 
so we have more entropy
https://docs.python.org/3/library/secrets.html
"""
import sys
import argparse
import string
import secrets


# program informations
__program__ = "strongpass.py"
__version__ = "3.4.2"
__author__ = "Brainfuck"


# banner
def banner():
    print("{} {}".format(__program__, __version__))
    print("Generate strong random passwords")
    print("Author: {}\n".format(__author__))


# print version and exit
def print_version():
    banner()
    print("License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>")
    print("This is free software: you are free to change and redistribute it.")
    print("There is NO WARRANTY, to the extent permitted by law.")
    sys.exit(0)


"""Function for check the user input, raise an error if user put one integer 
greather than 254
"""
def check(input_args):
    input_args = int(input_args)
    if input_args > 254:
        raise argparse.ArgumentTypeError("please enter an integer no more bigger than 254")
        sys.exit(1)
    else:
        return input_args


# main function
def main():
    parser = argparse.ArgumentParser(
    formatter_class = argparse.RawDescriptionHelpFormatter)
    # type=check --> recall def check() function above
    parser.add_argument("-l", "--lenght", type=check, 
        help="Lenght of password")
    parser.add_argument("-n", "--number", type=check, 
        help="Number of password to generate")
    parser.add_argument("-a", "--algorithm", choices=['1', '0'], 
        help="\n1 - random password, 0 - pronounceable password")
    parser.add_argument("-v", "--version", action="store_true", 
        help="display program version and exit")

    args = parser.parse_args()
    
    # if no arguments are given, print banner and help
    if len(sys.argv) == 1:
        banner()
        parser.print_help()
        sys.exit(1)

    if args.version:
        print_version()
    
    """ Generate password/s with "secrets", characters excluded: "l0Oo`ìèéòçà°"
    TODO: add option to argparse for do this
    """
    if args.lenght and args.number and args.algorithm:      
        for x in range(args.number):
            # charset parameters
            letters = "abcdefghijkmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ"
            numbers = "123456789"
            special = "|\!$%&/()='?^~[]{}+*@#<>,;.:-_"
            # 1 = random passwords
            if args.algorithm == "1":              
                charset = letters + numbers + special
                password = "".join((secrets.choice(charset)) 
                    for x in range(args.lenght))
                # add more entropy: at least one of all characters available
                if (any((letters) for c in password)
                        and any((numbers) for c in password)
                        and any((special) for c in password)):
                    print(password)
            # 0 = pronounceable passwords
            elif args.algorithm == "0":
                charset = letters
                password = "".join((secrets.choice(charset)) 
                    for x in range(args.lenght))
                print(password)
    else:
        parser.error("""
The following arguments are required: 
-l, --lenght <lenght> | -n, --number <number> | -a --algorithm {1, 0}""")
        sys.exit(1)


if __name__ == "__main__":
    main()
