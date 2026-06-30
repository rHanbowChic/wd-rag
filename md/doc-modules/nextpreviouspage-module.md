# NextPreviousPage Module

> Documentation > Modules > NextPreviousPage Module

**This module is deprecated. Use the [ListPages module](/doc:listpages-module) with the tag and category selectors instead.**

The NextPage and PreviousPage modules automatically create links to the next or previous page in the category with several type of sorting.

## Attributes

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| category | no | comma- or space-separated names, * for all categories | current category | the category where next / previous pages are chosen from |
| by | no | title, date | date | changes the way of choosing next / previous page |
| tags | no | comma- or space-separated tag names with+and-modifiers,/or@URL | none | lists tags that are used as a criteria to select pages, the "+" before the tag makes it required, "-" means "without a tag" and tags without modifiers translate to "pages that have any of those tags";/a special tag "=" adds all the tags that are present in the current page |

## Item format

You can define what NextPage / PreviousPage will display as it's result. You can use the format in the same way as in the [ListPages module](/doc:listpages-module).

## Examples

### Example 1

```
[[module NextPage by="title"]]
**Next documentation page:** %%linked_title%%
[[/module]]

[[module PreviousPage by="title"]]
**Previous documentation page:** %%linked_title%%
[[/module]]
```

### Result 1

or you can use this code to place the links on the left and right side of your page (blog-like):

### Example 2

```
[[div style="overflow: hidden"]]

[[div style="overflow: hidden; float: left; clear: left"]]
[[module PreviousPage]]
Previous: %%linked_title%%
[[/module]]
[[/div]]

[[div style="overflow: hidden; float: right"]]
[[module NextPage]]
Next: %%linked_title%%
[[/module]]
[[/div]]

[[/div]]
```

### Result 2
