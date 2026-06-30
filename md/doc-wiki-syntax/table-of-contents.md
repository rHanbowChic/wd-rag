# Table Of Contents

> Documentation > Wiki Syntax > Table Of Contents

To create a list of every heading, with a link to that heading, put a table of contents tag on its own line.

```
[[toc]]
[[f>toc]] - right-float table of contents
[[f<toc]] - left-float table of contents
```

Note that the table of contents creates a bookmark called "#toc".

If you want a particular heading NOT to appear in the table of contents, append the pluses with an asterisk, like this:

```
+ This section appears in the TOC
+* And this one does not
++* Neither does this one
```

**TOC example using above code**
---

| FoldUnfoldTable of ContentsThis section appears in the TOC |
| --- |

---

# This section appears in the TOC

# And this one does not

## Neither does this one
