# Block Formatting Elements

> Documentation > Wiki Syntax > Block Formatting Elements

## Left, right, centered and justified

To apply horizontal alignment to a block of text use:

| [[<]]/…/[[/<]] | align left |
| --- | --- |
| [[>]]/…/[[/>]] | align right |
| [[=]]/…/[[/=]] | align center |
| [[==]]/…/[[/==]] | align justified |

E.g.

```
[[=]]
Lorem ipsum dolor sit amet, consectetuer adipiscing elit.\
Aenean a libero. Vestibulum adipiscing, felis ac faucibus \
imperdiet, erat lacus accumsan neque, vitae nonummy lorem \
pede ac elit.

Maecenas in urna. Curabitur hendrerit risus vitae ligula.
[[/=]]
```

Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean a libero. Vestibulum adipiscing, felis ac faucibus imperdiet, erat lacus accumsan neque, vitae nonummy lorem pede ac elit.

Maecenas in urna. Curabitur hendrerit risus vitae ligula.

To center a single line use `=` at the beginning:

```
= Centered line
```

Centered line

**Note:** The block formatting tags must be on their own line with nothing after them, not even a space. For example, [[=]] and [[/=]] must be immediately followed by the return character (press Enter).

## Customdivblocks

To improve the layout you can use `[[div]] ... [[/div]]` elements which transform to html ` <div> ... </div> ` blocks.

Allowed attributes are: `id`, `class`, `style`, `data-` only but this should be more than enough to create desired layout. SPAN elements also allow `class`, `style` and `data-` attributes.

`[[div]]` blocks can be nested. Put the [[div]] and [[/div]] tags on their own lines or the parser will not recognize them.

Below is an example how to create a 2-column layout using div block:

```
[[div style="float:left; width: 45%; padding: 0 2%"]]
left column left column left column left column left column
left column left column left column left column left column
[[/div]]
[[div style="float:left; width: 45%; padding: 0 2%"]]
right column right column right column right column right column
right column right column right column right column right column
[[/div]]

~~~~
```

left column left column left column left column left column left column left column left column left column left column

right column right column right column right column right column right column right column right column right column right column

The `~~~~` element is used to clear floats and translates more or less to `<div style="clear:both"></div>`).

Custom `[[div]]` blocks can be used to create very advanced page layouts.

Adding underscore to **div** element **[[div_ ]]** will truncate whitespaces around it which prevents creation of random [new lines and paragraphs](/doc-wiki-syntax:paragraphs-and-newline). It's simplifices creation of complex HTML syntax like [Bootstrap components](http://getbootstrap.com/components/)

You can use user-defined `ID` arguments in custom DIVs, which is extremely useful building sites using [Bootstrap](http://getbootstrap.com). Please note that every user-defined `ID` will have a `"u-"` prefix added in the output HTML for the security reasons.

To make your source more readable, you can add the `"u-"` prefix yourself. For example, these 2 bits of wiki syntax will output the same HTML:

---

**`"u-"` prefix will be added to `myCarousel` automatically when the page is saved**

```
[[div id="myCarousel" class="carousel slide" data-interval="3000" data-ride="carousel"]]
```

**`"u-"` prefix will not be added to since it already exists**

```
[[div id="u-myCarousel" class="carousel slide" data-interval="3000" data-ride="carousel"]]
```

**HTML output from both examples**

```
<div id="u-myCarousel" class="carousel slide" data-interval="3000" data-ride="carousel">
```
