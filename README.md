# Very Large NGram Counter

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![MIT license](https://img.shields.io/badge/License-MIT-green.svg)
![Last Updated](https://img.shields.io/badge/Last%20Updated-2022.12.27-success.svg)

NGram counter for large corpuses

# Operation

## Install

You can install the package using the following steps:

`pip` install using an _admin_ prompt.

```{ps1}
pip uninstall VLNGramCounter -y
python -OO -m pip install -v git+https://github.com/TextCorpusLabs/VLNGramCounter.git
```

or if you have the code local

```{ps1}
pip uninstall VLNGramCounter -y
python -OO -m pip install -v c:/repos/TextCorpusLabs/VLNGramCounter
```

## Run

Counts the n-grams contained in a folder of TXT files.

```{ps1}
VLNGramCounter -source d:/data/corpus -dest d:/data/corpus.ngrams.csv
```

The following are required parameters:

* `source` is the folder containing the TXT files.
* `dest` is the CSV file used to store the ngram results.

The following are optional parameters:

* `length` is the length of the n-gram.
  The default is 1.
* `chunk_size` is the amount of items in used by the control structure before chunking.
  Higher values use more ram, but compute the overall value faster.
  The default is 1M.
* `include` count only values in this CSV list.
  The default is count everything.
* `exclude` ignore values in this CSV list.
  The default is exclude nothing.
  **Note**: due to the order of operations, it only makes seance to `exclude` single tokens.
* `cutoff` is the minimum value count to keep.
  The default is 2.
* `top` is the number of n-grams to save.
  The default is to keep 10K.
* `keep_case` (flag) keeps the casing as-is before converting to tokens for counting.
  The default is to upper case everything.
* `keep_punct` (flag) keeps all punctuation as-is before converting to tokens for counting.
  The default is to remove all tokens that are only punctuation.

**NOTE**: The order of operations for complex counting is as follows:

1. Transformation (`keep_case`)
2. Exclusion (`keep_punct` > `exclude`)
3. Inclusion (`include`)
4. Filter (`cutoff` > `top`)

## Debug/Test

The code in this repo is setup as a module.
[Debugging](https://code.visualstudio.com/docs/python/debugging#_module) and [testing](https://code.visualstudio.com/docs/python/testing) are based on the assumption that the module is already installed.
In order to debug (F5) or run the tests (Ctrl + ; Crtl + A), make sure to install the module as editable (see below).

```{ps1}
pip uninstall VLNGramCounter -y
python -m pip install -e c:/repos/TextCorpusLabs/VLNGramCounter
```

When debugging in VSCode for the first time, consider adding the below config to the _launch.json_ file.

```{json}
"args" : [
    "-source", "d:/data/corpus",
    "-dest", "d:/data/corpus.ngrams.csv",
    "-length", "1"]
```