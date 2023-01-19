import pathlib
import sys
from argparse import ArgumentParser, Namespace
from .dtypes import settings
from .NGramCounter import NGramCounter
from . import __version__

def main() -> None:
    parser = ArgumentParser(prog = 'VLNGramCounter', description = "NGram counter for large corpuses")
    parser.add_argument('-source', type = pathlib.Path, required = True, help = 'The folder containing the TXT files')
    parser.add_argument('-dest', type = pathlib.Path, required = True, help = 'The CSV file used to store the ngram results')
    parser.add_argument('-length', type = int, default = 1, help = 'The length of the n-gram')
    parser.add_argument('-max_ram', type = int, default = 1024, help = 'The rough cap to the amount of ram (in Mb) used by the control structure')
    parser.add_argument('-include', type = pathlib.Path, help = 'Count only values in this CSV list')
    parser.add_argument('-exclude', type = pathlib.Path, help = 'Ignore values in this CSV list')
    parser.add_argument('-cutoff', type = int, default = 2, help = 'The minimum value count to keep')
    parser.add_argument('-top', type = int, default = 10000, help = 'The number of n-grams to save')    
    parser.add_argument('-keep_case', action = 'store_true', help = 'Keeps the casing as-is before converting to tokens')
    parser.add_argument('-keep_punct', action = 'store_true', help = 'Keeps all punctuation of the before converting to tokens')
    args = parser.parse_args()
    _print_args(args)
    set = settings(args.source, args.dest, args.length, 1024 * 1024 * args.max_ram, args.include, args.exclude, args.cutoff, args.top, args.keep_case, args.keep_punct)
    counter = NGramCounter(set)
    counter.init()
    counter.count()

def _print_args(args: Namespace) -> None:
    print(f'--- {__version__} ---')
    for key in args.__dict__.keys():
        if key not in ['run']:
            print(f'{key}: {args.__dict__[key]}')
    print('---------')

if __name__ == "__main__":
    sys.exit(main())
