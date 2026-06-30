# CSS Module

> Documentation > Modules > CSS Module

The CSS module lets you insert CSS code into a wiki page. This is particularly useful for cross-site include (CSI) packages that need to use custom styling for their code. When you use the CSS module in a CSI, that CSS code will be included in all pages that use the CSI.

The syntax for the CSS module is:

```
[[module CSS arguments...]]
CSS code
[[/module]]
```

## Example

This example hides the side-bar menu on a single page (on themes with an elastic main-content):

```
[[module CSS]]
#side-bar {
    visibility: hidden;
    width: 0
}
[[/module]]
```

## Arguments

You can render the module's CSS code on the page in a `[[code type="css"]]` block by adding:

- **show="true"**

You can disable the module's CSS code so that it doesn't affect the theme by adding:

- **disable="true"**

## Multiple CSS modules

A single page can contain any number of CSS modules. Their code will be output, in order, in the page's HTML header.
