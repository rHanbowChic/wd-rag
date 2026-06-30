# Iftags

> Documentation > Wiki Syntax > Iftags

Tags are kind of special labels for a page, manually added in by editors by clicking on the **tags** link at the page options buttons on bottom of a page. Every tag can be max 64 characters long, tags are "space" separated and there is no limit of tags per page. Tags are very useful to label pages and then it's easy to create Tag Cloud, which allow to find interesting pages or topics much faster.

Special tags start with an underline: they are not automatically shown in tag clouds, but they can be used as special limitations in [[iftag]] conditions. Tags can be used in ListPages Module with generic conditions ( +, - ) too.

**Iftag** is a special condition question. You can use it on every page to "react" on tags and set up on the particular page used .

Syntax:

```
[[iftags +tag1 -tag2 tag3]] ... [[/iftags]]
```

where the +/-"tag#" stands for the requested tag-indexes.
- + before a tagname means - this tag must exist, (tag without a modifier works in a same way)
- - before a tagname means - this tag must not exist.

Example:

```
[[iftags +science]]
This page is labeled as: science.

Click here to view more science articles >
[[/iftags]]

[[iftags +bug -fixed]]
This is a bug, but it's not fixed yet.
[[/iftags]]
```
