# Tables

> Documentation > Wiki Syntax > Tables

## Simple tables

You can create simple tables using pairs of vertical bars:

```
||~ head 1 ||~ head 2 ||~ head 3 ||
|| cell 1 || cell 2 || cell 3 ||
|||| long cell 4 || cell 5 ||
||cell 6 |||| long cell 7 ||
|||||| looong cell 8||
```

| head 1 | head 2 | head 3 |
| --- | --- | --- |
| cell 1 | cell 2 | cell 3 |
| long cell 4 | cell 5 |
| cell 6 | long cell 7 |
| looong cell 8 |

```
|| lines must start and end || with double vertical bars || nothing ||
|| cells are separated by || double vertical bars || nothing ||
|||| you can span multiple columns by || starting each cell ||
|| with extra cell |||| separators ||
|||||| but perhaps an example is _
the easiest way to see ||
```

| lines must start and end | with double vertical bars | nothing |
| --- | --- | --- |
| cells are separated by | double vertical bars | nothing |
| you can span multiple columns by | starting each cell |
| with extra cell | separators |
| but perhaps an example is/the easiest way to see |

For a new line inside the table cell use _ (underscore) at the end of the line (see the example above).

## Advanced (custom) tables

To create more advanced tables, special tags can be used that can accept `class` and `style` attributes for managing appearance. To create an advanced table use the following syntax:

```
[[table]]
[[row]]
[[hcell style="border: 1px solid silver; background-color: yellow;"]]
header cell 0.0
[[/hcell]]
[[hcell style="border: 1px solid silver"]]
header cell 0.1
[[/hcell]]
[[hcell style="border: 1px solid silver" ]]
header cell 0.2
[[/hcell]]
[[/row]]
[[row]]
[[cell style="border: 1px solid silver" colspan="2"]]
cell 1.0
[[/cell]]
[[cell style="border: 1px solid silver; background-color: yellow;"]]
cell 1.2
[[/cell]]
[[/row]]
[[row]]
[[cell style="border: 1px solid silver" rowspan="2"]]
cell 2.0
[[/cell]]
[[cell style="border: 1px solid silver"]]
cell 2.1
[[/cell]]
[[cell style="border: 1px solid silver"]]
cell 2.2
[[/cell]]
[[/row]]
[[row]]
[[cell style="border: 1px solid silver"]]
cell 3.1
[[/cell]]
[[cell style="border: 1px solid silver"]]
cell 3.2
[[/cell]]
[[/row]]
[[/table]]
```

transforms to…

| header cell 0.0 | header cell 0.1 | header cell 0.2 |
| --- | --- | --- |
| cell 1.0 | cell 1.2 |
| cell 2.0 | cell 2.1 | cell 2.2 |
| cell 3.1 | cell 3.2 |

Each of elements [[table]], [[row]], [[cell]] and [[hcell]] can accept attributes `style` and `class` and they are transformed to (X)HTML tags: `<table>`, `<tr>` and `<td>`. Cells also accept **colspan** and **rowspan** variables.

If you wish to remove the spacing between cells in the above example, change the first line to `[[table style="border-collapse:collapse;"]]`.

An example of using tables for page layout can be found on our Snippets Wiki at: [http://snippets.wikidot.com/code:layout-with-tables](http://snippets.wikidot.com/code:layout-with-tables) .

Tables can be nested.
