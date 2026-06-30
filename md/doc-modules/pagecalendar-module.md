# PageCalendar Module

> Documentation > Modules > PageCalendar Module

## Description

The PageCalendar module creates a blogger-friendly calendar that displays the number of pages (articles) created per year and month. It also works great with the [ListPages module](/doc:listpages-module) as shown below.

> We are still working on this module so the final syntax and specifications might change.

## Attributes

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| category | no | comma- or space-separated category names or "*" for whole wiki, or @URL | current category | sets the scope of processed pages |
| tags | no | comma- or space-separated tag names with+and-modifiers,/or@URL | none | lists tags that are used as a criteria to select pages, the "+" before the tag makes it required, "-" means "without a tag" and tags without modifiers translate to "pages that have any of those tags";/"@URL" takes the tags from the URL |
| startPageortargetPage | no | any valid wiki page | current page | sets the page that will be displayed when any of the dates is clicked |
| urlAttrPrefix | no | any alphanumeric | none | prefix for the parameters passed via the URL e.g. to theListPages module |

If you are using PageCalendar with ListPages, make sure that the `urlAttrPrefix` has the same value in both modules.

Parameters that accept the `@URL` value, i.e. allow for passing the value in the URL, also allow for default values similar to the [ListPages module](/doc:listpages-module#toc8).

## Examples

List pages in the documentation section grouped by year and month, linked with the ListPages module:

```
[[module PageCalendar category="doc"]]
[[module ListPages category="doc" perPage="7" date="@URL" separate="false" prependLine="||~ Page||~ Date created||~ Created by ||"]]
|| %%linked_title%% || %%date%% || %%author%% ||
[[/module]]
```
