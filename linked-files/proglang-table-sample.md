# Sample Proglang Table

```txt
|  | compile | enter interpreter | exit interpreter | print |
| --- | --- | --- | --- | --- |
| C | $ gcc file.c OR gcc -o <execname> <file>.c | NA | NA |  |
|  | $ ./execname OR ./a.out IF NO EXECNAME SPECIFIED |  |  |  |
|  |  |  |  |  |
| C++ | $ gcc file.cpp OR g++ -o <execname> <file>.cpp | NA | NA |  |
|  | $ ./execname OR ./a.out IF NO EXECNAME SPECIFIED | (Jupyter Notebook) |  |  |
|  | Code::Blocks, XCode, NetBeans |  |  |  |
| Julia | $ julia <filename>.jl | $ julia | exit() | println("string") |
|  |  | exit() |  | print("string") |
|  |  | JuliaPro (Juno in Atom), Jupyter Notebook |  |  |
| Python | $ python <filename>.py | $ python | exit() | print('string') |
|  | $ py <filename>.py | exit() |  | print("string") |
|  |  | Spyder, Jupyter Notebook, Atom |  |  |
| R | $ R <file>.r | R Studio | NA | print("string") |
|  |  | R App |  | print('string') |
|  |  | Jupyter Notebook |  |  |
| Scala | $ scala <filename>.scala | $ scala | :q | println("Hello, world!") |
|  |  | Jupyter Notebook |  |  |
|  |  |  |  |  |
| Java | $ javac <filename>.java | NA | NA | System.out.println("string") |
|  | $ java <filename> | (Jupyter Notebook for SciJava) |  |  |
|  | Eclipse, NetBeans, IntelliJIdea, XCode |  |  |  |
| Scheme | $ scheme --load <file>.scm | $ scheme | (exit) | (begin (display "Hello, World!") (newline)) |
|  |  |  |  | (display "Hello, World!") |
|  |  |  |  |  |
| Racket | $ racket file.rkt | $ racket | (exit) | "Hello, world!" |
|  |  | $ drracket |  |  |
|  |  |  |  |  |
| Haskell | $ ghc -o objname file.hs | $ haskell | :quit | putStrLn "Hello World!" |
| [cheatsheet.codeslower.com/CheatSheet.pdf](https://cheatsheet.codeslower.com/CheatSheet.pdf) | $ ./ objname | $ ghci |  | main = putStrLn "Hello World!" |
| [github.s3.amazonaws.com/downloads/jsoffer/cheatsheet/CheatSheetEs.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAISTNZFOVBIJMK3TQ%2F20191213%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20191213T171655Z&X-Amz-Expires=300&X-Amz-SignedHeaders=host&X-Amz-Signature=3e018e451f290bb18731aad39af27d0ef52bb1357d937734d4d77acd8217b9f4](https://github.s3.amazonaws.com/downloads/jsoffer/cheatsheet/CheatSheetEs.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAISTNZFOVBIJMK3TQ%2F20191213%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20191213T171655Z&X-Amz-Expires=300&X-Amz-SignedHeaders=host&X-Amz-Signature=3e018e451f290bb18731aad39af27d0ef52bb1357d937734d4d77acd8217b9f4) |  |  |  |  |
| Prolog | $ prolog -q -l <filename>.pl OR <filename>.pro | $ prolog | halt. | write('string'), nl. |
|  | $ swipl -q -l <filename>.pl OR <filename>.pro | $ swipl |  |  |
|  |  |  |  |  |
| Octave | $ octave <file>.m | $ octave | exit |  |
|  |  | Octave GUI / Jupyter Notebook |  |  |
|  |  |  |  |  |
| Perl | $ perl <filename>.pl | $ perl6 | exit |  |
|  | $ perl5 <filename>.p6 |  |  |  |
|  |  |  |  |  |
| Lua | $ lua <filename>.lua | $ lua | os.exit() |  |
|  |  |  |  |  |
|  |  |  |  |  |
| Bash | $ ./<filename> | $ bash | NA |  |
|  |  |  |  |  |
|  |  |  |  |  |
| NASM (Linux x86_64) | $ nasm -felf64 <filename>.asm && ld hello.o && ./a.out | NA | NA |  |
|  |  |  |  |  |
|  |  |  |  |  |
| NASM (OSX x86_64) | $ nasm -fmacho64 <filename>.asm && ld hello.o && ./a.out | NA | NA |  |
|  |  |  |  |  |
|  |  |  |  |  |
| HLA | $ hla <filename>.hla ==>CREATES <filename>.o and <filename> executable | NA | NA |  |
|  | $ ./<filename> |  |  |  |
|  |  |  |  |  |
| Rust | $ rustc <filename>.rs | NA | NA |  |
|  | $ ./<filename> |  |  |  |
|  |  |  |  |  |
| Ruby | $ ruby <filename>.rb | $ irb | exit |  |
|  |  |  |  |  |
|  |  |  |  |  |
| Nim | $ nim c -r --verbosity:0 <file>.nim | NA | NA |  |
|  |  | (Jupyter Notebook) |  |  |
|  |  |  |  |  |
| JavaScript | NA | NA | NA |  |
```
