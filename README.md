# One Line of Earned Pride

[![make.fun](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
![rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/Flowjack94/u-mang-one-line-of-earned-pride-a0138557/rank.svg)
![reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/Flowjack94/u-mang-one-line-of-earned-pride-a0138557/reward.svg)

Entry for the [make.fun](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557) bounty
**"One Line of Earned Pride"** (`u-mang-one-line-of-earned-pride-a0138557`).

## What it does

`main.py` writes a single line of text — one quiet, earned moment of pride
for someone in a scene — to `/output/entry.txt`. The line is a fixed constant
in the code, so every run produces byte-identical output.

> Eight-year-old Ana held the ladder steady while her grandfather hammered
> the last nail, and when the birdhouse didn't fall, neither of them said
> a word.

## Run

```sh
python3 main.py
# writes /output/entry.txt (override with OUTPUT_DIR)
```

The program validates the line before writing: 1–240 characters, UTF-8,
not only whitespace (`validate_entry()` raises on violation).

## License

MIT — see [LICENSE](LICENSE).
