# PagesByTag Module

> Documentation > Modules > PagesByTag Module

**This module is deprecated. Use the [ListPages module](/doc:listpages-module) with the tag and category selectors instead. Specifically:**

```
[[module ListPages tags="@URL" OTHER PARAMETERS]]
MODULE BODY
[[/module]]
```

## Description

This module lists all pages, that are tagged1 with a specific tag. The scope can optionally be restricted to a single category.

## Attributes

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| tag | no | an all-lowercase text string | none | limits displayed pages to the specified tag |
| category | no | valid category name | none | limits displayed pages to the specified page category |

## Notes

If you do not specify a `tag` attribute, *PagesByTag*

- will use a tag that is specified by adding a trailing `/tag*/any-tagl*` to the URL, like `http://*{wiki-name}*.wikidot.com/*{page-name}*/tag/*{any-tag}*`
- will displays nothing if no tag is specified in the URL

If you do not specify a `category` attribute, *PagesByTag*

- will use a category that is specified by adding a trailing `/category*/any-category*` to the URL, like `http://*{wiki-name}*.wikidot.com/*{page-name}*/category/*{any-category}*`
- will displays pages from all categories

If *PagesByTag* is specified without attributes (i. e. [[module PagesByTag]]), it works nicely together with [[[module TagCloud](http://www.wikidot.com/doc:tagcloud-module)]]. If correctly set up (like on a default [system:page-tags](/system:page-tags) page), *TagCloud* generates links of the form …`/tag*/any-tag*`, which *PagesByTag* then uses to list those pages.

## Examples

#### PagesByTag Standalone

*what you get …*

If you don't see any *PagesByTag* output here, try adding `/tag*/any-tag*` to the end of the …`/doc:pagesbytag-module` URL. An example would be [doc:pagesbytag-module/tag/news](http://www.wikidot.com/doc:pagesbytag-module/tag/news#examples)

*what you type …*

```
[[module PagesByTag]]
```

#### PagesByTag with Tag Attribute

*what you get …*

## List of pages tagged with news :

*what you type …*

```
[[module PagesByTag tag="news"]]
```

#### PagesByTag with Tag and Category Attribute

*what you get …*

## List of pages tagged with news from category _default :

([show from all categories](/doc-modules:pagesbytag-module/tag/news))

*what you type …*

```
[[module PagesByTag tag="news" category="_default"]]
```

## Credits

The original text is located at the Wikidot Open Source Edition [documentation pages](http://www.wikidot.org/doc:pagesbytag-module).

**Footnotes**

1. You can tag a page by clicking on the “tags” button at the bottom of a page
