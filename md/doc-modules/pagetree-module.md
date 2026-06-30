# PageTree Module

> Documentation > Modules > PageTree Module

## Description

This module can visualize the structure of pages connected by *parenthood* - i.e. the page tree is constructed by the fact that a page can have a *parent page*. This can be set by accessing page *+options* and clicking on *parent*.

Parenthood also affects navigation since it produces a breadcrumb navigation element at the top of the page which is quite useful.

## Attributes

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| root | no | page name string | current page | top element of the tree |
| showRoot | no | "true" | "false" | should the root element be displayed on the top of the list? |
| depth | no | integern > 0 | none | limits maximum depth of the list;n = "1"displays only child pages of the root page,n = "2"displays child pages and their child pages etc. |

## Examples

Display page tree of the documentation:

```
[[module PageTree root="doc" showRoot="true"]]
```

- [Doc](/doc)
