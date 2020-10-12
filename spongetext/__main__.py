"""Handles input and starts the spongetext generator."""
import argparse
from spongetext.spongestring import SpongeString
import pyperclip


parser = argparse.ArgumentParser(
    description='creATE teXT WIth rAnDomLY CApitALIZed LettERs.'
)

parser.add_argument('string',
                    help='The string to transform.')
parser.add_argument('-s', '--spongeness',
                    help='The amount of spongeness to apply 10 = allcaps.',
                    choices=[str(i) for i in range(1, 11)],
                    default=6)
parser.add_argument('-c', '--copy',
                    help='Copy output to clipboard.',
                    action="store_true")

args = parser.parse_args()

output = SpongeString(args.string, args.spongeness)

print(output)

if args.copy:
    pyperclip.copy(str(output))
    print('Output has been copied to clipboard.')
