# Comments Module

> Documentation > Modules > Comments Module

## Description

Inserts page discussion below page contents. A very useful module if you want to comment contents of the page.

By default, if the visitor has enough permissions, the form for comments is already open. This can be changed by setting the `hideForm="true"` attribute.

## Attributes

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| title | no | text string | "" | shows alternate heading for the comments block |
| hide | no | "true" | "false" | hides the discussion and requires user click to show it |
| hideForm | no | "true","yes" | "false" | does not display the open input form by default, just a link to add a comment |
| order | no | "reverse","forwards" | forwards | If set to"reverse", this shows comments in reverse order, newest above oldest |

## Examples

Initially hidden discussion.

```
[[module Comments hide="true"]]
```

Full discussion within a page.

```
[[module Comments]]
```

Make the comments block be listed in [[toc]] (by disabling the default heading and insert a heading manually):

```
+ Comments

[[module Comments]]
```
