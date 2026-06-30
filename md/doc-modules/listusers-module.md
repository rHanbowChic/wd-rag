# ListUsers Module

> Documentation > Modules > ListUsers Module

The ListUsers module produces formatted output that lets you report on a set of users working with a site.

The current implementation of the module outputs a block of text for the currently logged user only.

```
[[module ListUsers users="."]]
module body
[[/module]]
```

Module body cannot contain [[code]] or [[html]]. In case it contains those tags, module will not work at all.

| Variable | Description |
| --- | --- |
| number | The current user's ID number |
| title | The current user's title or name |
| name | The current user's name in unix format (lowercase, no spaces) |

# Example:

```
[[module ListUsers users="."]]
**You are user number %%number%%, %%title%% (%%name%%)!**
[[/module]]
```

# In action:

This code prints nothing if user is anonymous.

To comment or discuss on the planned design for this module [please visit the projects forum](http://projects.wikidot.com/thread:129).
