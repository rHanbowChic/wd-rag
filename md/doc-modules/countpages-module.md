# CountPages Module

> Documentation > Modules > CountPages Module

The CountPages module lets count the number of pages that match various criteria. CountPages is similar to the [ListPages module](/doc-modules:listpages-module) in some ways but does not let you render page data, only a single symbol called %%total%%.

## Selecting pages

Specify one or more of these selectors to refine the set of pages you select. Each selector adds additional constraints:

| Argument | Meaning |
| --- | --- |
| pagetype | Select by type of page |
| category | Select by category |
| tags | Select by tags |
| parent | Select by parent page |
| link_to | Select by outgoing links |
| created_at | Select by date of creation |
| created_by | Select by original author |
| rating | Select by rating |
| offset | Start list after an offset of pages |
| range | Select a range of pages |
| _<data-form-field-name> | Select by a field's value in a data form |

Page type selector:

- "normal" means pages without underscore in name (default)
- "hidden" means pages starting with underscore
- "*" means all pages, with or without underscores

Category selector:

- "." means current category (default)
- "*" means all categories
- else, a list of space/comma delimited categories
- categories are by default additive (category OR category OR category)
- "-category" means exclude pages in this category (AND NOT)

Tags selector:

- "-" means pages with no tags, visible or invisible
- "=" means pages with any of the same visible tags as this page
- "==" means pages with the exact same visible tags as this page
- else, a list of space/comma delimited tags
- tags are by default additive (tag OR tag OR tag)
- "-tag" means pages without the tag (AND NOT)
- "+tag" means pages with the tag (AND)

Parent page selector:

- "-" means pages with no parent page
- "=" means siblings of current page (same parent)
- "-=" means with different parent than current page
- "." means children of current page (parent is this page)
- else specifies a single full page name

Outgoing links selector:

- enter a single full name of an existing page to select pages that link to that page
- while "." means pages that link to current page

Creation date selector:

- "=" means created on same day as current page
- "yyyy" means specified year
- "yyyy.mm" means specified year and month
- optionally prefixed by ">", "<", "=", "<=", ">=", "<>" (default is "=")
- dates are not site-local but currently all UTC (GMT)
- or: "last n unit" where 'n' is a count (defaults to 1) and unit is "hours", "day", "week", or "month"

Author selector:

- "=" means by created by author of current page
- "-=" means by not created by author of current page
- else, a single user name

Rating selector:

- "n" means pages with rating equal to n
- "=" means pages with same rating as current page
- optionally prefixed by ">", "<", "=", "<=", ">=", "<>" (default is "=")

Caution: When listing pages from many categories, where some categories have rating type set to + or +/- and others to "stars" (in Site Manager), selecting and ordering by rating may not funtion properly. The solution is to list and order pages from categories having the same rating mode.

Offset selector:

- "n" means do not show the first n pages (default is 0)

Range selector:

- "." means current page
- "before" means pages up to but not including current (in order after sorting)
- "after" means pages after current page (in order after sorting)
- "others" means pages except current page

Data Form selector:

- Select by a field's value in a data form
- Syntax: `_data-form-field-name="data-form-field-value"`
- Example: `_gender="m"` - select all pages that have 'm' set as the 'gender' field's value in the Data Form

## Example

```
[[module CountPages category="wiki,blog" tags="_closed"]]
%%total%% active pages.
[[/module]]
```

## Notes

- You can put wiki syntax (e.g. for links) into the module body.
- This module (like most) cannot be used inside a ListPages module.
- %%count%% can be used as a synonym for %%total%%.
