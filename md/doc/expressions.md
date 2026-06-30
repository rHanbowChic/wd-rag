# Expressions

Expressions can be used to create advence structures and applications. It allowes to use mathematic/logic syntax and 3 build in functions (abs, min, max). Expression can be maximum 256 character length.

**[[#if value | display if true | display if false ]]**

Simple true/false checker, it treats first parameter as string and evaluate it to true/false

false is a:

- string false
- string null
- empty string
- 0

everything else is true

**[[#ifexpr expression | display if true | display if false ]]**

This syntax evaluates expression and check if it's true or not.

**[[#expr expression]]**

It evaluates expression and display it.

Examples:

```
[[#expr abs(-100) ]]
[[#expr min(4, 1, -4, 6, -10) ]]
[[#expr max(4, 1, -4, 6, -10) ]]
[[#expr 2*4/12-4+66%2 ]]
[[#ifexpr 2*4/12-4+66%2 < -3.5 | less than -3.5 | greater than -3.5 ]]
[[#expr 2*(2-1) ]]
[[#if true | display if true | display if false ]]
```

> 100
>
> -10
>
> 6
>
> -3.33333333333
>
> greater than -3.5
>
> 2
>
> display if true
