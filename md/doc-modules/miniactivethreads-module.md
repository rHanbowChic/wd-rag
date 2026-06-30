# MiniActiveThreads Module

> Documentation > Modules > MiniActiveThreads Module

## Description

Displays the most active threads within the last 7 days in a compact form. Thread title, date started and total number of posts is displayed.

## Attributes

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| limit | no | positive integer | 5 | how many threads to print |

## Examples

The code:

```
+++ Most active topics (last week)

[[module MiniActiveThreads limit="5"]]
```

displays the most active forum threads within last 7 days.
