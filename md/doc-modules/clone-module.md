# Clone Module

> Documentation > Modules > Clone Module

## Description

Makes a copy of part of, or all of the current or a specified site. The current logged user (who invokes the clone action) becomes the owner (master administrator) of the specified site.

## Attributes

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| source | no | text string,"." | current site | Specifies the site to clone. If not specified, clones the current site. If the source site is private, the user must be a member of the site. |
| button | no | text string | "Clone this site" | Specifies the text for a button link. |

## How it works

The Clone module creates a button that occupies a line by itself. Clicking on the button shows a pop-up that asks for a destination site (which may not exist). When the clone operation is complete, the Clone module takes the user directly to the destination site.

The clone has all the pages, attached files, and configuration of the original site, however:

- It has only one member, the cloner, who is the new site's master admin
- It is marked as private, even if the template was public

## Examples

On a template site, offer the user the opportunity to copy the site:

```
[[module Clone]]
```

## Notes

Sites, even public ones, are at present clonable by default. This will be switched for Pro users.
