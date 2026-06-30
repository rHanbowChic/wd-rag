# Standalone buttons for page options

> Documentation > Wiki Syntax > Standalone buttons for page options

Sometimes it might be convenient to hide the default page options and present only selected buttons to the users. The syntax for accomplishing this is:

`[[button *type* *options*]]`

Where the *type* is: `edit`, `edit-append`, `edit-sections`, `history`, `print`, `files`, `tags`, `source` (view page source), `backlinks`, `talk` (works similar as in MediaWiki/Wikipedia), `delete`, `rename`, `site-tools`, `edit-meta`, `watchers`, `parent` and `lock-page`.

Possible attributes are:

- text — alternative text to be displayed
- class — CSS class of the A element
- style — CSS style definition

For some nice "view source" and "print" buttons with icons you can use the following code:

```
[[>]]
[[button source style="background-image: url(http://www.wikidot.com/local--files/files/view-source.png); background-repeat: no-repeat; background-position: bottom right; padding-right: 20px; color: #444"]]
[[button print style="background-image: url(http://www.wikidot.com/local--files/files/document-print.png); background-repeat: no-repeat; background-position: bottom right; padding-right: 20px;color: #444"]]
[[/>]]
```

to get:

view source

print
