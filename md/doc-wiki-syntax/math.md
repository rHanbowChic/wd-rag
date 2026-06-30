# Math

> Documentation > Wiki Syntax > Math

Wikidot.com uses [MathJax](http://mathjax.org) to render beautiful LaTeX equations. For those that know LaTeX syntax using wikidot equations should be straightforward.

## Equations

Simply put the equation between `[[math *label*]] … [[/math]]` block tags (the label is optional). The equation is rendered within LaTex `\begin{equation} ... \end{equation}` environment. Please refer to any LaTeX reference manual for details about syntax.

```
[[math label1]]
\rho _{\rm GJ} = -\sigma (r) \left[ (1 - \eta _{\ast }^2 {\kappa \over {\eta ^3}}) \cos \chi \right.
+ \left. {3\over 2} \theta (\eta) H(\eta)
\xi \sin \chi \cos \phi \right]
[[/math]]
```

(1)

To refer to a labeled equation simply use `[[eref *label*]]` to get a raw number or e.g. `Eq. ([[eref *label1*]])` which gives Eq. (1).

You can specify the LaTeX environment in 2 ways, either by passing a `type="<environment>"` parameter, or using `\begin{<environment>}` and `@\end{<environment>}@@` within the equation. E.q. these two are equivalent:

```
[[math type="align"]]
E = mc^2
[[/math]]
```

```
[[math]]
\begin{align}
E = mc^2
\end{align}
[[/math]]
```

The `equation` environment is default. Other supported math environments are: `align`, `alignat`, `aligned`, `alignedat`, `array`, `Bmatrix`, `bmatrix`, `cases`, `eqnarray`, `equation`, `gather`, `gathered`, `matrix`, `multline`, `pmatrix`, `smallmatrix`, `split`, `subarray`, `Vmatrix`, `vmatrix`.

## Inline math

To use math expressions inside text (sentence) use `[[$ ... $]]` block tags.

```
[[$ E = mc^2 $]] is much more popular than
[[$ G_{\mu\nu} - \Lambda g_{\mu\nu} = \kappa T_{\mu\nu} $]]
```

$$E = mc^2$$ is much more popular than $$G_{\mu\nu} - \Lambda g_{\mu\nu} = \kappa T_{\mu\nu}$$
