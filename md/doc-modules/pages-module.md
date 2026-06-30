# Pages Module

> Documentation > Modules > Pages Module

**This module is deprecated. Use the [ListPages module](/doc:listpages-module) instead.**

## Description

The *Pages* module is able to list pages within a site or within a category.

## Attributes

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| category | no | name of an existing category | none | limits the listing to the specified category |
| details | no | "true" | none | print extra information about pages |
| preview | no | "true" | none | prints a short preview of the page(This parameter is temporarily ignored due to performance reasons. It will come back soon) |
| order | no | dateCreatedDesc/dateCreatedAsc/dateEditedDesc/dateEditedAsc/titleDesc/titleAsc | titleAsc | selects ordering of the pages |
| limit | no | any positive integer | none | how many pages to return; if you omit this all pages will be listed |

## Examples

Print only pages from the *_default* category with details:

```
[[module Pages category="_default" details="true"]]
```

Print all pages with details and preview:

```
[[module Pages details="true" preview="true"]]
```

10 most recently edited pages

```
[[module Pages order="dateEditedDesc" limit="10"]]
```

10 most recently created pages

```
[[module Pages order="dateCreatedDesc" limit="10"]]
```
