# Lists

> Documentation > Wiki Syntax > Lists

## Bulleted Lists

Make a list element by starting a line with an asterisk. To increase the indent put extra spaces

before the asterisk.

```
* Bullet 1
* Bullet 2
 * Bullet 2.1
```

- Bullet 1
- Bullet 2
  - Bullet 2.1

If you need to put more than one line in the bullet list, please use _ (underscore) at the end of the line you want to break (after one space). Remember not to insert any character after the underscore.

```
* Bullet 1 _
 another line
* Bullet 2
 * Bullet 2.1
```

- Bullet 1

  another line
- Bullet 2
  - Bullet 2.1

## Numbered Lists

Similarly, you can create numbered lists by starting a paragraph with one or more hashes.

```
# Item 1
# Item 2
 # Item 2.1
```

1. Item 1
2. Item 2
   1. Item 2.1

If you need to put more than one line in the numbered list, please use _ (underscore) at the end of the line you want to break (after one space). Remember not to insert any character after the underscore.

```
# Item 1 _
 another line
# Item 2
 # Item 2.1
```

1. Item 1

   another line
2. Item 2
   1. Item 2.1

You can mix bulleted lists and number lists.

## Advanced Lists

You can use [[ul]] / [[ol]] and [[li]] tags to create advanced lists. It's especially useful when using a Boostrap-based theme. Every [[ul]] / [[ol]] and [[li]] can contain *id*, *class*, *data-* and *style* arguments. Lists can be nested.

```
[[ul]]
 [[li class="item1" data-toggle="data1"]]Item1[[/li]]
 [[li style="color: red;"]]Item 2
  [[ol]]
    [[li]]Item 2.1[[/li]]
    [[li]]Item 2.2[[/li]]
  [[/ol]]
 [[/li]]
[[/ul]]
```

- Item1
- Item 2

  1. Item 2.1
  2. Item 2.2

Adding underscore to **ul/ol** element **[[ul_/ol_ ]]** will truncate whitespaces around it which prevents creation of random [new lines and paragraphs](/doc-wiki-syntax:paragraphs-and-newline). It's simplifices creation of complex HTML syntax like [Bootstrap components](http://getbootstrap.com/components/)

You can use user-defined `ID` arguments in advanced lists, which is extremely useful building sites using [Bootstrap](http://getbootstrap.com). Please note that every user-defined `ID` will have a `"u-"` prefix added in the output HTML for the security reasons.

To make your source more readable, you can add the `"u-"` prefix yourself. For example, these 2 bits of wiki syntax will output the same HTML:

---

**`"u-"` prefix will be added to `myAdvancedList` automatically when the page is saved**

```
[[ul id="myAdvancedList"]]
```

**`"u-"` prefix will not be added to since it already exists**

```
[[ul id="u-myAdvancedList"]]
```

**HTML output from both examples**

```
<ul id="u-myAdvancedList">
```
