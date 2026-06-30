# Rate Module

> Documentation > Modules > Rate Module

## Description

Displays a widget used to rate pages. Page rating must be enabled in the Site Manager.

## Attributes

No attributes required.

## Examples

```
[[module Rate]]
```

results in:

or displays five-stars rating mode depending on the setting in Site Manager -> Page Ratings -> Type

You can use certain variables when using 5-star type:

| Variable | Description |
| --- | --- |
| %%rating%% | Displays rating number value |
| %%rating_votes%% | Displays number of votes |
| %%rating_percent%% | Displays overall average rating in percent (without the '%' character) |
| %%rating_decimal%% | Displays decimal value of 5-star rating (e.g. 4.7) |

For example:

```
[[module Rate]]
Average Rating %%rating%% from %%rating_votes%% votes
[[/module]]
```

To make this centered use:

```
[[=]]
[[module Rate]]
[[/=]]
```
