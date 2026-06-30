# Footnotes

> Documentation > Wiki Syntax > Footnotes

To make footnotes in the text use `[[footnote]]` block. To force the list of footnotes

to appear not at the end of the page, use `[[footnoteblock]]`.

```
Some text[[footnote]]And a small footnote.[[/footnote]]. Here we go
with another footnote[[footnote]]Content of another footnote.[[/footnote]].

[[footnoteblock]]
```

Some text1. Here we go with another footnote2.

**Footnotes**

1. And a small footnote.
2. Content of another footnote.

If you are not satisfied with the default title ("Footnotes") you can force your own title by using `[[footnoteblock title="Custom title"]]` or even do not use title at all (title="").
