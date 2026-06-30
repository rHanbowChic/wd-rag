# Site Structure

> Documentation > Site Structure

This document covers the layout (structure) of a any Site provided by wikidot.com network.

| FoldUnfoldTable of ContentsSitesContent pagesDirect links between pagesPage inclusionsCategories (namespaces)TagsParent pagesForumCategory groupsForum categoriesForum threadsPosts and posts layoutInteraction of Pages and Forum |
| --- |

# Sites

Each Site powered by WikiDot.com resides in a unique subdomain of wikidot.com:

`http://*site-unix-name*.wikidot.com`

where the `site-unix-name` consists of only alphanumeric characters (0..9, 'a'..'z') and ('-').

Each site is independent from other sites but all the sites share User accounts, but can have different appearance, permission system, block-list etc. In this context the wikidot.com service only provides hosting for the sites.

From the functional point of view any site can consist of two (somehow overlapping) parts: content pages and forum section.

# Content pages

Content pages are… just pages you browse on any of our sites. Each of the pages is uniquely identified by its *unix name* - i.e. a string that consists of only alphanumeric characters (0..9, 'a'..'z'), dash ('-') and colon (':').

All the pages reside in a *flat structure* which means there are no directories, subdirectories etc. Any page is accessible via its URL address:

`http://*site-unix-name*.wikidot.com/*page-unix-name*`

## Direct links between pages

All the pages within a Site are somehow "linked". The most basic link is just a *direct link*.

The pages are linked from other places by inserting a link, i.e. `[[[*page-unix-name*]]]` or even `[[[Page Unix name!!!]]]`. In the second case the string is internally *unixified* and both cases render to a link [page unix name](/page-unix-name). If a link is red - page does not exist and can be created by following the link. This is the safest way of creating new pages.

## Page inclusions

One page can include contents of another page. This is useful e.g. when you want to maintain some sort of summaries or separate column on the main page, but want to edit the individual units somewhere else. To include a page simply use `[[include *page-unix-name*]]`.

## Categories (namespaces)

Although all the pages reside in the *flat structure*, pages can belong to different *categories* (*namespaces*). This allows:

- easier page management and structure,
- separate appearance settings, permissions, license for each category (see [ManageSite module](/doc:managesite-module)),
- easier listing (see [Pages module](/doc:pages-module))

Categories are uniquely identified by their *unix names*. Each page belongs to a certain category based on its *page unix name* which can have the form:

*category-unix-name*:*the-rest*

Everything that precedes the colon (':') in the *page unix name* is treated as a category name.

Categories are created (when a page with a new category name is created) and automatically deleted (when no more pages contain category name).

## Tags

Each page can have multiple *tags* (labels). If you use such services as [del.icio.us](http://del.icio.us) you should be familiar with the concept of tags. Also Wikipedia has entries for [tags](http://en.wikipedia.org/wiki/Tags) and [tag cloud](http://en.wikipedia.org/wiki/Tag_cloud).

In your Site tags can relate to… anything. A tag cloud is automatically generated for all your tagged pages.

Tags have no affect on other functions and features of the Site contrary to categories.

## Parent pages

*Parent* relations allow to introduce page structure (like in site maps). The results of setting a parent page are:

- breadcrumbs navigation appear at the top of the page,
- easier to come back to the parent page,
- easier listing (see [ChildPages module](/doc:childpages-module) and [PageTree module](/doc:pagetree-module))

These documentation pages use parent relations. Just see how it works and how it makes the navigation easier.

# Forum

Forum layout is easy. It consists of 3 elements: category groups, categories and threads.

## Category groups

Category groups are just container for forum categories for easier logical layout. This layout is visible on the forum main page, e.g. on our [Community Forums](http://community.wikidot.com/forum/start). Groups are the top-most containers.

## Forum categories

Forum categories are containers for forum *threads* (also known as *topics*). Forum categories can have individual permissions and posts layout.

## Forum threads

Threads cover individual discussion subject and contain individual posts. Simply if anyone wants to talk about something new, a new thread is created.

## Posts and posts layout

Posts are smallest units here. They are just what people say. Posts can be edited after they are posted.

Posts layout can be set using the [ManageSite module](/doc:managesite-module) and can be:

- flat/linear - posts appear one after another; it is not possible to reply to the post that is not the last post,
- nested - the tree-like structure, any post can be replied and new posts not necessarily appear at the end of the discussion but under the post that is being replied; *max nest level* determines number of possible levels and defaults to 2

Example of flat structure:

- post 1
- post 2
- post 3
- post 4
- …

Nested structure:

- post 1
  - reply to post 1
  - another reply to post 1
- post 2
  - reply
    - reply
    - …

Flat/nested choice often determines the way people discuss. In the flat layout there is only one "path" - that is why this is called "linear".

Nested layout offers more freedom, more digressions and more paths in the discussion but it is more difficult to spot new posts (unless you use RSS feed or watch a thread).

The default layout is: nested with max_nest_level = 2.

# Interaction of Pages and Forum

Forum infrastructure can be used to discuss pages (by creating a relation between apage and a forum thread) or even to add forum elements to content pages.

To enable the "discuss" button at the bottom of a page the [ManageSite module](/doc:managesite-module) should be use and option *Forum & discussion* -> *Per page discussion*.

When enabled, a button "discuss" will be visible at the bottom page options bar which will lead to a unique forum thread just for commenting this particular page.

Another way is to use the [Comments module](/doc:comments-module) and embed it in the page. This will bring the whole discussion just below the page content. Such a solution could be used e.g. when one creates an article and wants other people to discuss it or comment.
