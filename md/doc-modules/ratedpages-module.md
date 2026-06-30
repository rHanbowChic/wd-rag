# RatedPages Module

> Documentation > Modules > RatedPages Module

## Description

Displays top-rated pages. Also a category can be specified to limit the results.

> This module is under development and not yet complete.
>
> But should work as described below.

## Attributes

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| category | no | valid category name | none | limits reported pages to a single category |
| order | no | "date-created-asc", "date-created-desc", "rating-asc", "rating-desc" | "rating-desc" |  |
| minRating | no | integer | none | limits the results to the pages having rating equal or above this limit |
| maxRating | no | integer | none | limits the results to the pages having rating equal or below this limit |
| limit | no | positive integer | 10 | limits number of displayed pages |
| comments | no | "true"/"yes" | none | display number of comments too |

## Examples

Display top-rated pages from the category `rateit`

```
[[module RatedPages category="rateit" limit="20" comments="true" minRating="0"]]
```

Display "most hated" pages:

```
[[module RatedPages category="rateit" order="rate-asc" limit="20" comments="true" maxRating="-1"]]
```

Display new submissions:

```
[[module RatedPages category="rateit" order="date-created-desc" limit="20" comments="true"]]
```
