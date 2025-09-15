# FastMathTeX

A quicker way to input math equations with LaTeX syntax.

## Running

Ensure that you have `pyperclip` installed with:

```shell
python3 -m pip install pyperclip
```

then simply run:

```shell
python3 src/fmtex.py
```

Optionally you can add executable rights to the file and add the `./src/`
directory to your `PATH` (only for UNIX based systems).

## How to use

You are given a prompt where you can input a custom syntax, after you are done
press `[Enter]` and the LaTeX output will be shown. Additionally it is copied to
your clipboard with a dollar sign before and after.

To exit write `'exit` in the prompt.

### FastMath syntax

In FastMathTeX all words longer than one character are treated as commands, no
checking is done to determine wether they are valid command.

Any text inside double quotes is placed inside a `\text{}` block.
`"hello"` becomes `\text{hello}` and `"Dwayne \"The Rock\" Johnson" becomes
`\text{Dwayne "The Rock" Johnson}`.

Any text inside percent signs is treated as raw LaTeX and is left unchanged.
`%\begin{cases}%` becomes `\begin{cases}` and not `\\begin{\cases}`

A number that immediately follows a letter becomes a subscript.

There are shortcuts for many commands:

| FastMath | TeX             | Mnemonic             |
| -------- | --------------- | -------------------- |
| `NN`     | `\mathbb N`     |                      |
| `ZZ`     | `\mathbb Z`     |                      |
| `QQ`     | `\mathbb Q`     |                      |
| `II`     | `\mathbb I`     |                      |
| `RR`     | `\mathbb R`     |                      |
| `CC`     | `\mathbb C`     |                      |
| `ddd`    | `\ldots`        | Dot, dot, dot        |
| `balign` | `\begin{align}` |                      |
| `ealign` | `\end{align}`   |                      |
| `bcases` | `\begin{cases}` |                      |
| `ecases` | `\end{cases}`   |                      |
| `lp`     | `\left(`        | Left paren           |
| `rp`     | `\right)`       | Right paren          |
| `ls`     | `\left[`        | Left square bracket  |
| `rs`     | `\right]`       | Right square bracket |
| `lc`     | `\left{`        | Left curly bracket   |
| `rc`     | `\right}`       | Right curly bracket  |
| `lb`     | `\left\|`       | Left beam            |
| `rb`     | `\right\|`      | Right beam           |
| `al`     | `\alpha`        |                      |
| `bt`     | `\beta`         |                      |
| `gm`     | `\gamma`        |                      |
| `dl`     | `\delta`        |                      |
| `DL`     | `\Delta`        |                      |
| `impl`   | `\implies`      |                      |
### Example

```text
> "Let" \; RR^n = lc (a1, a2, ddd, a_n) | a_i in RR, i = 1, 2, ddd, n rc
\text{Let} \; \mathbb R^n = \left\{ ({a_1}, {a_2}, \ldots, a_n) | a_i \in \mathbb R, i = 1, 2, \ldots, n \right\}
>
```

Rendered output:

$$
\text{Let} \\; \mathbb R^n = \left\\{ (a_1, a_2, \ldots, a_n) | a_i \in \mathbb R, i = 1, 2, \ldots, n \right\\}
$$
