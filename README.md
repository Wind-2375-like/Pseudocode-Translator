# Pseudocode Translator

> I pushed the code two years ago with another account and now I have added a readme file and re-organized the project file. This is my first project at XJTU.

This is a simple pseudocode translator combined with dialogue system which helps users translate pseudocode into C codes.

You need to install `ply` first: `pip install ply`.

Then you need to specify input files (default `pcode_sample.txt`) for entering pseudocode and output files (default `output.c`).

Finally a dialogue system will be launched and it will request user to fill in the missing information about the pseudocode.

To run the lexer/tokenizer, just run:

```shell
python pcodelex.py
```

To run the lexer + parser, just run:

```shell
python pcodeparser.py
```
