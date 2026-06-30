# ListDrafts Module

> Documentation > Modules > ListDrafts Module

This module lists all pages on Site where there is a draft included. You can choose if you want to display all draft or only for existing/non-existing pages.

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| pageType | no | exists, notexists | - | when not defined, all drafts are listed |

Example:

```
[[module ListDrafts pageType="exists"]]
```
