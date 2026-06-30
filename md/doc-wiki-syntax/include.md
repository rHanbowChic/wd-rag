# Include

> Documentation > Wiki Syntax > Include

If you want to include contents of another page use:

```
[[include pagename]]
```

or

```
[[include :sitename:pagename]]
```

The *include* tag should start and end with a newline. [[include]] tags are parsed *inside* code blocks. To prevent an [[include]] tag from being parsed, put a space in front of it. This does make copy/paste of example code that contains [[include]] tags a problem.

The sitename can be a Wikidot subdomain (e.g. :www) or a full name, including a custom domain.

The `[[include]]` tag can also take parameters and substitute variables in the included source. To denote variables in the included page use:

```
{$var1}, {$number_books}, {$title}, {$variable_name}, {$variableName}
```

and in the including page use:

```
 [[include pagename
|var1=value1
|number_books=43
|title=Best Wiki Ever
|variable_name=just a variable
|variableName=another variable
]]
```

As you can see you can split variable definitions over several lines for cleaner code.

**NOTE: includes and images/files**: The `[[include]]` works just by inserting the page source at a given place. If you have any images or files attached in the included page and you refer to them as [[image filename.jpg]] in the included page, please rather use the image/file source with the name of the page too, e.g. [[image **included-page/**filename.jpg]]

Includes across sites are called *cross-site includes* or CSIs. CSIs are a powerful way to link page templates and code from other sites.
