import sys
from argparse import ArgumentParser, Namespace
from VeryLargeNGram.types import settings
from VeryLargeNGram.utils import validate as v
#from . import count_ngrams

def main() -> None:
    parser = ArgumentParser(prog = 'VeryLargeNGram', description = "NGram counter for large corpuses")
    parser.add_argument('-source', type = v.folder, required = True, help = 'The folder containing TXT files')
    parser.add_argument('-dest', type = v.file, required = True, help = 'The file to store the converted CSV file')
    parser.add_argument('-size', type = v.nonzero_int, default = 1, help = 'The length of the n-gram')
    parser.add_argument('-control', type = v.nonzero_int, default = 1024, help = 'The rough amount of ram (in Mb) used by the control structure')
    parser.add_argument('-include', type = v.file, help = 'Count only values in this CSV list')
    parser.add_argument('-exclude', type = v.file, help = 'Ignore values in this CSV list')
    parser.add_argument('-cutoff', type = v.nonzero_int, default = 2, help = 'The minimum value count to keep')
    parser.add_argument('-top', type = v.nonzero_int, default = 10000, help = 'The number of n-grams to save')    
    parser.add_argument('-keep_case', action = 'store_true', help = 'Keeps the casing as-is before converting to tokens')
    parser.add_argument('-keep_punct', action = 'store_true', help = 'Keeps all punctuation of the before converting to tokens')
    args = parser.parse_args()
    _print_args(args)
    #count_ngrams(args.source, args.dest, args.size, args.control, args.include, args.exclude, args.cutoff, args.top, args.keep_case, args.keep_punct)

def _print_args(args: Namespace) -> None:
    print(f'---------')
    for key in args.__dict__.keys():
        if key not in ['run']:
            print(f'{key}: {args.__dict__[key]}')
    print('---------')

if __name__ == "__main__":
    sys.exit(main())
