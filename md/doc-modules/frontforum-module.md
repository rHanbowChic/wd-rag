# FrontForum Module

> Documentation > Modules > FrontForum Module

## Description

Uses forum discussions to create news system (with comments) to put on the pages. Also can create RSS feeds.

In more details - each new forum thread from selected forum categories is used to create new news item (first post makes the body). Several parameters allow customization.

If RSS feed is created a link will also be put into the document head (feed info should appear in browsers automatically) and below the news items.

## Attributes

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| category | yes | semicolon-separated integers | none | numerical IDs of the forum categories (look at the URL address); multiple categories can be used to create news |
| feed | no | alphanumeric | none | if present - RSS feed will be created with the filename equal to its value |
| feedTitle | no | string | "sitenamefeed" | title of the feed |
| limit | no | number | 20 | how many items should be displayed |
| offset | no | number | 0 | how many items to omit from the beginning? |
| fixRelativeLinks | no | true | none | fixes links for forum posts if you're using categories from external forums, e.g. Wikidot News / Changelog etc. |

**Category IDs** can be found when looking at the URL address of the page which lists the threads in the category. It looks like this:

http://community.wikidot.com/forum/c-**12**/bugs-and-problems

So in this case the category ID is **12**.

## Item format

A custom format for displaying news items can be chosen. To specify a custom format one should use module invocation:

```
[[module FrontForum category="..."]]
<custom format>
[[/module]]
```

where the inner `<custom format>` element is any block of text following the wiki-syntax, where special variables can be used:

| variable | aliases | description |
| --- | --- | --- |
| %%title%% |  | title of the news item |
| %%linked_title%% | %%title_linked%% | title of the news item linking to the original forum thread |
| %%link%% |  | URL pointing to the original forum thread |
| %%author%% |  | prints author of the thread |
| %%date%% |  | prints posting date |
| %%date\|format%% |  | prints posting date with a custom format. Most tokens from php'sstrftimeare accepted. You may findthe howtocontributed by community useful. |
| %%comments%% |  | number of comments = number of threads posts - 1 |
| %%category%% |  | forum category where the thread belongs (linked) |
| %%description%% | %%short%%,%%summary%% | short summary of the item |
| %%content%% | %%text%%,%%long%%,%%body%% | full content of the item (post) |

The default format is:

```
+ %%linked_title%%

by %%author%% %%date|%O ago (%e %b %Y, %H:%M %Z)%%

%%content%%

%%comments%% | category: %%category%%
```

## Examples

The news from the [main Wikidot site](/start) use the following code to produce both the news on the main site and a feed:

```
[[module FrontForum category="8" feed="news" feedTitle="Wikidot site news"]]
++ %%linked_title%%

%%date|%e %b %Y, %H:%M %Z (%O ago)%%

%%content%%

%%comments%% | category: %%category%%
[[/module]]
```

You should change the `category` and `feedTitle` parameters of course to match your own Site.
