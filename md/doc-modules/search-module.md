# Search Module

> Documentation > Modules > Search Module

## Description

The Search module lets your users search the current site. You can place the Search module itself on any page, but your site *must* contain a page called "*search:site*" that (also) contains the Search module.

## Attributes

The Search module allows these attributes:

- mini="true" - shows a simpler search box, hiding the radio button search options.

## Example

On your site's *start* page:

```
++ Search this site
[[module Search]]
= ([http://www.wikidot.com/doc:searching Search tips])
```

On your site's *search:site* page:

```
[[module Search]]
```

## Advanced Settings for search:site Page

This option only works on your site's *search:site* page in conjunction with the default search box (normally located near the top navigation bar).

The default source of this page is:

```
[[module Search]]

[!-- please do not remove or change this page if you want to keep the search function working --]
```

You can edit the parameters of the Search module using the following options.
- a="p" sets the default search mode to pages only (default).
- a="f" sets the default search to forum only.
- a="pf" sets the default search to pages and forum.

Used in tandem with *mini="true"* you can hide the radio button options displaying a simpler interface and controlling the type of search done on your site.

## Advanced Example

To limit searching to forums only and hide the search radio button options, edit your *search:site* page so it looks like this:

```
[[module Search a="f" mini="true"]]

[!-- please do not remove or change this page if you want to keep the search function working --]
```
