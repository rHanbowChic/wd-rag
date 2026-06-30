# Members Module

> Documentation > Modules > Members Module

## Description

This module is used to list members of the site.

## Attributes

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| group | no | "members"/"admins"/"moderators" | "members" | limits the list to the specified group |
| showSince | no | "no" or "false" | "yes" for group="members" | does not show the date joined; valid only for group="members" |
| order | no | "userId", "userIdDesc", "joined", "joinedDesc", "name", "nameDesc" | "joined" | sort Members by name (alphabetically), by user ID or date of joining |

## Examples

List all members of the site:

```
[[module Members]]
```

List only site administrators:

```
[[module Members group="admins"]]
```

List only moderators:

```
[[module Members group="moderators"]]
```
