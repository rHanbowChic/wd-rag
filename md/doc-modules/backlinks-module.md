# Backlinks Module

> Documentation > Modules > Backlinks Module

## Description

This module simply lists all the pages from the given wiki that contain links to the current page.

## Attributes

No attributes.

## Appearance

If you want to change the appearance of the list you should define (within your custom theme) the following class definition:

```
div.backlinks-module-box{
    [your definition]
}
```

## Examples

```
[[module Backlinks]]
```

and this produces backlinks for this page:

**Tip:** You can use the Backlinks module to make *soft categories* — simply create pages in the namespace `category:`, e.g.

- `category:cars`
- `category:bikes`
- etc…

Each of these pages could have a description of the category and the `[[module Backlinks]]` that would list the pages…

And within the pages you want to add to specific categories you would put links to these categories, e.g. at the bottom:

```
++ Categories:

[[[category:cars]]], [[[category:bikes]]]
```

Moreover if all your category pages, i.e. `category:cars`, `category:bikes` etc. include a link to a page called `category:all` — it is a quick way to put the module in the `category:all` too and have a list of all categories.
