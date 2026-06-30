# ListPages Module

> Documentation > Modules > ListPages Module

The ListPages module is a general-purpose and widely-used tool that selects and display pages within a site.

To use ListPages, you decide some or all of:

- what pages to select (from the site, from categories, by parent, by tags, by date, etc.)
- how to order the pages (ascending, descending)
- how to break the output into blocks (pagination)
- how to display the results as Wikidot text (templating in module body)
- how to export the results as an RSS feed

The general syntax for ListPages is:

```
[[module ListPages arguments...]]
module body
[[/module]]
```

By default, ListPages will show all visible pages in the current category, from newest to oldest.

Module body cannot contain [[code]] or [[html]]. In case it contains those tags, module will not work at all.

## Example

This example lists the pages in the current category, along with details of who created the page, and when:

```
[[module ListPages separate="no" limit="5"]]
%%title_linked%% - [[user %%created_by%%]] - %%created_at%%
[[/module]]
```

In action:

## Naming conventions

Older argument names are `inMixedCase`. Newer argument names are `in_lower_case`, and this style will be used more systematically in Wikidot. Dates are always `*something*_at` and user names are always `*someone*_by`. Linked fields are always `*somefield*_linked`.

## Selecting pages

Specify one or more of these selectors to refine the set of pages you select. Each selector adds additional constraints:

| Argument | Meaning |
| --- | --- |
| pagetype | Select by type of page |
| category | Select by category |
| tags | Select by tags |
| parent | Select by parent page |
| link_to | Select by outgoing links |
| created_at | Select by date of creation |
| updated_at | Select by date of update |
| created_by | Select by original author |
| rating | Select by rating |
| votes | Select by number of votes |
| offset | Start list after an offset of pages |
| range | Select a range of pages |
| name | Select by page name |
| fullname | Select by fullname |
| _<data-form-field-name> | Select by a field's value in a data form |

Page type selector:

- "normal" means pages without underscore in name (default)
- "hidden" means pages starting with underscore
- "*" means all pages, with or without underscores

Category selector:

- "." means current category (default)
- "*" means all categories
- else, a list of space/comma delimited categories
- categories are by default additive (category OR category OR category)
- "-category" means exclude pages in this category (AND NOT)
- "%%category%%" means the same category as the current page ( if used on a _template page)

Tags selector:

- "-" means pages with no tags, visible or invisible
- "=" means pages with any of the same visible tags as this page
- "==" means pages with the exact same visible tags as this page
- else, a list of space/comma delimited tags
- tags are by default additive (tag OR tag OR tag)
- "-tag" means pages without the tag (AND NOT)
- "+tag" means pages with the tag (AND)

Parent page selector:

- "-" means pages with no parent page
- "=" means siblings of current page (same parent)
- "-=" means with different parent than current page
- "." means children of current page (parent is this page)
- else specifies a single full page name

Outgoing links selector:

- enter a single full name of an existing page to select pages that link to that page
- while "." means pages that link to current page

Creation date selector:

- "=" means created on same day as current page
- "yyyy" means specified year
- "yyyy.mm" means specified year and month
- optionally prefixed by ">", "<", "=", "<=", ">=", "<>" (default is "=")
- dates are not site-local but currently all UTC (GMT)
- "last n unit" or "older than n unit" where 'n' is a count (defaults to 1) and unit is "hours", "day", "week", or "month"

Update date selector:

- dates are not site-local but currently all UTC (GMT)
- "last n unit" or "older than n unit" where 'n' is a count (defaults to 1) and unit is "hours", "day", "week", or "month"

Author selector:

- "=" means by created by author of current page
- "-=" means by not created by author of current page
- else, a single user name

Rating selector:

- "n" means pages with rating equal to n
- "=" means pages with same rating as current page
- optionally prefixed by ">", "<", "=", "<=", ">=", "<>" (default is "=")

**Caution:** When listing pages from many categories, where some categories have rating type set to + or +/- and others to "stars" (in Site Manager), selecting and ordering by rating may not funtion properly. The solution is to list and order pages from categories having the same rating mode.

Votes selector:

- "n" means pages with votes equal to n
- "=" means pages with same number of votes as current page
- optionally prefixed by ">", "<", "=", "<=", ">=", "<>" (default is "=")

Offset selector:

- "n" means do not show the first n pages (default is 0)

Range selector:

- "." means current page
- "before" means pages up to but not including current (in order after sorting)
- "after" means pages after current page (in order after sorting)
- "others" means pages except current page

Name selector:

- enter a single name (means the name part without the category!) of an existing page to select exact this page of a given category - or pages of different categories if also selected. You can use a dataform field of the current page
- "=" means pages that have exact the same name as the current page ( makes sence only with other selected categories)
- "s%" means all pages starting with given character "s" or
- "s*" means all pages starting with given character "s"

Fullname selector:

- enter a single fullname of an existing page to select exact this one page (you can use a dataform field of the current page)

Data Form selector:

- Select by a field's value in a data form
- Syntax: `_data-form-field-name="data-form-field-value"`
- Example: `_gender="m"` - select all pages that have 'm' set as the 'gender' field's value in the Data Form

## Ordering pages

To order the pages, use:

| Argument | Meaning |
| --- | --- |
| order | Specify order criteria |

Order criteria:

- "*property*" means "ascending by this property"
- optionally followed by " desc" meaning "descending"
- optionally followed by " desc desc" meaning "ascending", which makes "desc" safe to add after any sort order
- default is "created_at desc"

| Property | Meaning |
| --- | --- |
| name | Order by page name |
| fullname | Order by category and page name |
| title | Order by page title |
| created_by | Order by author screen name |
| created_at | Order by date created |
| updated_at | Order by date updated |
| size | Order by number of characters in page |
| rating | Order by rating |
| votes | Order by number of votes |
| revisions | Order by number of revisions |
| comments | Order by number of comments |
| random | Order randomly, cached for 60 seconds |
| _data-form-field-name | Order by a field in a data form |

For example to order by rating in descending order:

```
order="rating desc"
```

Caution: When listing pages from many categories, where some categories have rating type set to + or +/- and others to "stars" (in Site Manager), selecting and ordering by rating may not funtion properly. The solution is to list and order pages from categories having the same rating mode.

This example shows how to order pages using a data form field. Note that you must prefix the data form field name with an underscore. This lists all pages from the *dictionary* category and sorts them by the data form's *mainword* field (a wiki field type in this example). The body of the module then lists the contents of the *mainword* field and creates a link to the page.

```
[!--
Note: Use %%form_raw{fieldname}%% for wiki field types,
         %%form_data{fieldname}%% for other field types
--]
[[module ListPages category="dictionary" order="_mainword"]]
%%form_raw{mainword}%%@<&nbsp;>@@<&nbsp;>@([/%%fullname%% see dictionary entry])
[[/module]]
```

Note that "*property* asc" is not allowed and unknown order criteria give you the default order, which is "created_at desc".

**Type casting** for [Data Forms](/doc:data-forms) fields:

Default order method is sort by text. You can enforce numerical sorting.

```
[[module ListPages category="band" order="_albums::integer desc"]]
...
[[/module]]
```

## Pagination

To control how many items (wiki pages) will be shown in total, and how these are paginated (confusingly, also into 'pages'), use any of:

| Argument | Meaning |
| --- | --- |
| limit | Limit total items |
| perPage | Limit per pagination |
| reverse | Show pages in reversed order |

Total limit:

- "number" - means limit the total number of selected pages.
- by default all pages matching criteria are listed

Pagination limit:

- "number" - means limit the number of page items shown on per pagination.
- default is 20, maximum is 250.

Reversed display:

- "yes" - means show wiki pages from last to first on given page.

## Module body

The body of the module allows you to specify how page properties and content is formatted. To control this formatting, you can use these module arguments:

| Argument | Meaning |
| --- | --- |
| separate | Separation specifier |
| wrapper | Wrapper specifier |
| prependLine | Header specifier |
| appendLine | Footer specifier |

Separation specifier:

- "yes" means place each page item into a separate container (divs).
- "no" means put all items into one container, so they can become a single list, for example.
- default is "yes".

With `separate` set to true, each of the page is compiled (converted from wiki source to HTML) separately. While it is false, wiki compiler is invoked only once on a combined source from all selected pages.

As a result, some page-specific variables and constructs such as `iftags` can generate different results. `iftags`, with `separate="yes"`, will be aware of tags of individual pages, while with `separate="no"` it will read tags of the main page that holds the ListPages module.

Also [[image :first ...]] will only work with `separate="yes"`.

Wrapper specifier:

- "yes" means place all items into container (div).
- "no" means do not place all items into container (div).
- default is "yes".

Header specifier:

- "text" means output this text at the start of the list of pages, *only* if the separation specifier is false.

Footer specifier:

- "text" means output this text at the end of the list of pages, *only* if the separation specifier is false.

### Sections head/body/foot

Additionally you can use **[[head]]**, **[[body]]**, **[[foot]]** sections, which simply replaces prependLine and appendLine. It allows you to create more complex header and footer for ListPages. This is particularly usable with complex table and list creation.

Example of sections usage

```
[[module ListPages category="carousel" wrapper="no" separate="no" _active="yes"]]
  [[head]]
    [[ul id="u-myList" class="..."]]
  [[/head]]

  [[body]]
    [[li class="list-item"]]%%title_linked%% by (%%created_by%%)[[/li]]
  [[/body]]

  [[foot]]
    [[/ul]]
  [[/foot]]
[[/module]]
```

(also works for custom domains)
The template consists of wiki text mixed with variables specified as `%%variable-name%%`. You can use these page properties:

| Property | Meaning |
| --- | --- |
| Page lifecycle |  |
| %%created_at%% | Date page was created |
| %%created_by%% | User who created page |
| %%created_by_unix%% | "Unixified" name of user who created page — to be used for constructing URLs |
| %%created_by_id%% | "ID" number of user who created page — to be used for constructing URLs |
| %%created_by_linked%% | Icon and link to user who created page |
| %%updated_at%% | Date page was updated (edited, tagged, parented) |
| %%updated_by%% | User who updated page |
| %%updated_by_unix%% | "Unixified" name of user who updated page — to be used for constructing URLs |
| %%updated_by_id%% | "ID" number of user who updated page — to be used for constructing URLs |
| %%updated_by_linked%% | Icon and link to user who updated page |
| %%commented_at%% | Date of last comment |
| %%commented_by%% | User who made last comment |
| %%commented_by_unix%% | "Unixified" name of user who made last comment — to be used for constructing URLs |
| %%commented_by_id%% | "ID" number of user who made last comment — to be used for constructing URLs |
| %%commented_by_linked%% | Icon and link to user who made last comment |
| Page structure |  |
| %%name%% | Page name without category |
| %%category%% | Page category if any |
| %%fullname%% | Page name with category if any |
| %%title%% | Page title |
| %%title_linked%% | Link to page showing title as text (works also for custom domain) |
| %%parent_name%% | Parent page name without category |
| %%parent_category%% | Parent page category if any |
| %%parent_fullname%% | Parent page name with category if any |
| %%parent_title%% | Parent page title |
| %%parent_title_linked%% | Link to Parent page showing title as text |
| %%link%% | URL pointing to page (not working for custom domains!) |
| %%content%% | Page content |
| %%content{n}%% | Numbered content section |
| %%preview%% | First 200 characters of the page |
| %%preview(n)%% | Firstncharacters of the page |
| %%summary%% | Summary of content |
| %%first_paragraph%% | The first paragraph of the page |
| %%tags%% | Page visible tags (not starting with underscore) |
| %%tags_linked%% | Page visible tags linked to system:page-tags/tag/{tag} |
| %%tags_linked\|link_prefix%% | Page visible tags linked to link_prefix{tag} |
| %%_tags%% | Page hidden tags (starting with underscore) |
| %%_tags_linked%% | Page hidden tags linked to system:page-tags/tag/{tag} |
| %%_tags_linked\|link_prefix%% | Page hidden tags linked to link_prefix{tag} |
| %%form_data{name}%% | Field value from pagedata formif any |
| %%form_raw{name}%% | For select fields, the internal value saved in the page form data, if any |
| %%form_label{name}%% | The label of the field as defined in thedata formif any |
| %%form_hint{name}%% | The hint of the field as defined in thedata formif any |
| Page reporting |  |
| %%children%% | Number of child pages |
| %%comments%% | Number of comments on page |
| %%size%% | Number of characters in page |
| %%rating%% | Page rating value (number or stars depending on Rating settings in Site Manager |
| %%rating_votes%% | Number of votes |
| %%rating_percent%% | Percent value of 5-star rating only |
| %%revisions%% | Number of revisions to page |
| %%index%% | Page index in ListPages output + offset (1 to %%total%%) |
| %%total%% | Total number of pages ignoring limit (may be higher than %%limit%%) |
| %%limit%% | Limit passed to ListPages (empty if not passed) |
| %%total_or_limit%% | Total number of pages in ListPages output (highest %%index%%)./If limit is passed to the module, %%total_or_limit%% is %%total%% or %%limit%% whichever is smaller |
| Current context |  |
| %%site_title%% | Title of current site |
| %%site_name%% | Wikidot Unix name for site |
| %%site_domain%% | Active domain name of current site |

Date formatting:

- All _at fields are dates and allow a custom format via the `|*format*` specifier.

Most tokens from PHP's [strftime](http://php.net/manual/en/function.strftime.php) are accepted. You may find [the howto](http://community.wikidot.com/howto:frontforum-date-variable) contributed by community useful.

> Editor's note: this section needs expanding with the most useful formatting options.

Tag linking:

- If no link_prefix is specified, tags link to system:page-tags/tag/name-of-tag
- If link_prefix is specified, tags link to link_prefixname-of-tag (colors irrelevant)
- if link_prefix is empty but the pipe is present, %%tags_linked|%% generates links to pages with names corresponding to tags
- Examples

| if syntax is: | "shiny" tag will link to: |
| --- | --- |
| %%tags_linked%% | /system:page-tags/tag/shiny |
| %%tags_linked\|system:page-tags/tag/%% | /system:page-tags/tag/shiny |
| %%tags_linked\|interesting-list/category/%% | /interesting-list/category/shiny |
| %%tags_linked\|player:%% | /player:shiny |
| %%tags_linked\|very_%% | /very_shiny |
| %%tags_linked\|http://myothersite.wikidot.com/see-also/tag/%% | http://myothersite.wikidot.com/see-also/tag/shiny |
| %%tags_linked\|%% | /shiny |

## Advanced Use

This section describes additional functionality that will be useful for advanced users.

### RSS feeds

You can export any ListPages result as an RSS feed. Use these arguments to control the RSS feed generation:

| Argument | Meaning |
| --- | --- |
| rss | feed title |
| rssDescription | feed description |
| rssHome | feed homepage |
| rssLimit | feed limit |
| rssOnly | only show feed link |

Feed title:

- "text" means use this text for the RSS feed title.
- Default is to not generate any RSS feed.

Feed description:

- "text" means use this text for the RSS feed description.

Feed homepage:

- "*pagename*" means tell RSS clients this is the home page for the feed.
- Default is `http://your-site.wikidot.com`
- Setting value to "blog:_start" actually means `http://your-site.wikidot.com/blog:_start`

Feed limit:

- sets limit for RSS feed, and can be different to the ListPages limit
- Default RSS limit inherits lower value from limit and perPage arguments

Feed only:

- "true" or "yes" displays the RSS feed link without showing ListPages results

**Important**: RSS feed ignores "`created_at`" selector.

### Passing arguments via URL

ListPages lets you create variations of a single list using specially constructed links, consisting of the page URL (link) followed by arguments and values. These are mainly useful to invoke new selectors, and change the ordering or display.

You can pass any arguments in the URL by specifying `argument="@URL|default-value"` as the argument value and then appending "/`name`/`value`" to the URL used to invoke the page. If the URL does not contain a value for the argument, the default is used. Arguments that do not have @URL in their value cannot be set via the URL. The default value is optional: if you use only `argument="@URL"` and do not provide a value on the URL, then the argument behaves as if it was not set.

The two main ways of using arguments-by-URL are (a) to create links to a page explicitly, on another page and (b) to generate links within the ListPages itself, so it will reshow itself with different configurations. Here is a simple example:

```
[[module ListPages category="@URL|design"]]
%%name%% in category %%category%%
[[/module]]
```

Another example shows how to select blog entries by created_at date:

```
[[module ListPages category="blog" created_at="@URL"]]
```

and the module will read the `created_at` argument from the properly-constructed URL, e.g.

```
http://www.wikidot.com/blog/created_at/2008.07
```

You can specify multiple arguments like this:

```
http://www.wikidot.com/blog/created_at/2008.07/order/rating desc/limit/3
```

To pass tags with (+/-) "+" need to be encoded with "%2b"

`+apple,-banana`

```
http://www.wikidot.com/blog/tags/%2bapple,-banana
```

You can create the URLs manually or within ListPages itself. Some modules also generate compatible URLs.

> Editor's note: list of modules that produce compatible URLs should be documented here.

### More than one module in the page

Since some of the arguments can be passed in the URL of the request there might be conflict when more than one ListPages module is present in the page. One most likely conflict can occur when both modules use pagination — clicking "next" on one of them would also affect the other.

To prevent such conflicts use the `urlAttrPrefix` argument. This prepends a text (unique for each of the modules) to the argument names in the URL. So the …/created_at/2008.7 would become …/prefix_created_at/2008.07. If you can set unique prefixes for each of the ListPages instances you would avoid any conflicts.

## Deprecated functionality

These arguments and variables can still be used but are disrecommended. You should when possible use the modern replacements. At some future date, deprecated functionality may be removed.

| Instead of this | Use this |
| --- | --- |
| skipCurrent="yes" | range="others" |
| categories= | category= |
| tag= | tags= |
| tagTarget="pagename" | %%tags_linked\|/pagename/tag/%% |
| date= | created_at= |
| order="dateCreatedAsc" | order="created_at" |
| order="dateCreatedDesc" | order="created_at desc" |
| order="dateEditedAsc" | order="updated_at" |
| order="dateEditedDesc" | order="updated_at desc" |
| order="titleAsc" | order="title" |
| order="titleDesc" | order="title desc" |
| order="ratingAsc" | order="rating" |
| order="ratingDesc" | order="rating desc" |
| order="pageLengthAsc" | order="size" |
| order="pageLengthDesc" | order="size desc" |
| rssTitle= | rss= |
| %%linked_title%% | %%title_linked%% |
| %%page_unix_name%% | %%fullname%% |
| %%full_page_name%% | %%fullname%% |
| %%page_name%% | %%name%% |
| %%author%% | %%created_by%% |
| %%author_edited%% | %%updated_by%% |
| %%user_edited | %%updated_by%% |
| %%date%% | %%created_at%% |
| %%date_edited%% | %%updated_at%% |
| %%description%% | %%summary%% |
| %%short%% | %%summary%% |
| %%text%% | %%content%% |
| %%long%% | %%content%% |
| %%body%% | %%content%% |

ListPages supports a 'default format', where you do not specify any module body and no `[[/module]]`. This functionality is deprecated and you should avoid using it.
