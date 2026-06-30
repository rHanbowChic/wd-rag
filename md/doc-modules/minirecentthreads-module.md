# MiniRecentThreads Module

> Documentation > Modules > MiniRecentThreads Module

## Description

Displays most recent forum threads in a forum suitable to be included e.g. within the welcome page. The list items contain thread title, date started and number of posts.

## Attributes

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| limit | no | positive integer | 5 | how many items to display? |

## Examples

```
++ Most recent forum threads

[[module MiniRecentThreads limit="3"]]
```

simply displays 3 most recent forum threads.
