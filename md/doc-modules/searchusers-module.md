# SearchUsers Module

> Documentation > Modules > SearchUsers Module

## Description

The SearchUsers module lets you search all Wikidot users by login id, email address, or full name. You can place the SearchUsers module itself on any page, but your site *must* contain a page called "search:users" that (also) contains the SearchUsers module.

## Attributes

The SearchUsers module does not allow any attributes.

## Example

On your site start page:

```
++ Search all Wikidot users
[[module SearchUsers]]
= (enter email address or nick or real name)
```

On your site's search:users page:

```
[[module SearchUsers]]
```
