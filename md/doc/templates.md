# Templates

> Documentation > Templates

# Summary

- a template is a special page that defines common items to display on all pages in a category
- templates are easy way to change the layout for all pages in a category in one place
- the name of the special page defining the layout for a category is *category*`:_template` (examples below)

# Details

To create a template for a category you create a page called "_template" in that category. For the default category, the template page is called "_template". For example:

```
_template
category:_template
bugs:_template
proposals:_template
```

Pages that start with an underscore are not listed by other modules and hidden in most cases.

## Create your live template page

Create a page called _template but do not leave it empty: as a minimum you need to add %%content%%. This tells the template to simply display the current content of the page in the category.

> You cannot use the NewPage module to create a hidden page (a page whose name starts with an underscore — "_"). You must append *category:_template* to the URL in the address bar and hit enter to create live template pages. On the feedback site, there is a wish to change it this behavior. If you also feel this way, [rate it up](http://feedback.wikidot.com/wish:404).

The purpose of a template is to define a layout of pages within a category. Here is a simple template that forces the height of the content box.
Here is a typical template,which adds a comments module below the page content:

```
+ Original content of the page below

%%content%%

----------------

[[module Comments]]
```

It is easy to imagine what it really does. When this markup is saved as `some-category:_template`, all pages from the `some-category` will be combined with the template during rendering. **Content of the page will be substituted into the %%content%% tag**. This way we can add headers, side bars, navigation elements, modules and comment boxes to the template and the viewed page will automatically have it.

When you try editing a page from the category, only the "inside content" is editable. Template is applied only when viewing the compiled page.

## Splitting the content

Let us start with an example of a template:

```
[[div style="float:right; width: 200px; border: 1px solid #999; margin: 10px;"]]
%%content{1}%%
[[/div]]

%%content{2}%%

[[table]]
[[row]]
[[column]]
%%content{3}%%
[[/column]]
[[column]]
%%content{4}%%
[[/column]]
[[/row]]
[[/table]]

====

This will be content of the side bar.

====

The main content.

====

This will go into the left cell of the table.

====

And this into the right cell.
```

There are two things described above: splitting content and default page content.

**Splitting** allows you to create sections in the page and manipulate them separately in the template. Sections are separated by a series (4 or more) "equals" characters and are referred to as %%content{X}%% in the template. You can access them in any order within the template.

Using this you can easily create advanced layouts (like multicolumn, multi-navigation etc.) and make editing and maintenance much easier.

## Default content

Also in the template you can provide the **default initial content for newly created pages**. Such content is separated from the template by the '====' tag - the same as for splitting the content. To make it visually different you can make it longer — e.g. 10 characters. When a user wants to start a new page in the category, this content will be placed in the editor.

Also, when default content is defined for the template, there will be no option for selecting templates from the `templates` category (our previous templating mechanism).

## Escaping the ==== tag

Since you might want to use the "====" tag in the content of a page and NOT as a splitter, there is a way to escape the splitter and prevent the default action. Surround the splitter with "@@" like this:

```
@@====@@
```

You can also escape the "====" tag by adding a space. This is the only way to escape it inside a code block. *Note: if you copy/paste code that contains '====', make sure it does not still have a space at the end of the line, or it will not work!*

## Page variables within the _template

The template consists of wiki text mixed with variables specified as `%%variable-name%%`. You can use these variables:

| Property | Meaning |
| --- | --- |
| Page lifecycle |  |
| %%created_at%% | Date page was created |
| %%created_by%% | User who created page |
| %%created_by_unix%% | "Unixified" name of user who created page — to be used for constructing URLs |
| %%created_by_linked%% | Icon and link to user who created page |
| %%updated_at%% | Date page was updated (edited, tagged, parented) |
| %%updated_by%% | User who updated page |
| %%updated_by_unix%% | "Unixified" name of user who updated page — to be used for constructing URLs |
| %%updated_by_linked%% | Icon and link to user who updated page |
| %%commented_at%% | Date of last comment |
| %%commented_by%% | User who made last comment |
| %%commented_by_unix%% | "Unixified" name of user who made last comment — to be used for constructing URLs |
| %%commented_by_linked%% | Icon and link to user who made last comment |
| Page structure |  |
| %%name%% | Page name without category |
| %%category%% | Page category if any |
| %%fullname%% | Page name with category if any |
| %%title%% | Page title |
| %%title_linked%% | Link to page showing title as text |
| %%parent_name%% | Parent page name without category |
| %%parent_category%% | Parent page category if any |
| %%parent_fullname%% | Parent page name with category if any |
| %%parent_title%% | Parent page title |
| %%parent_title_linked%% | Link to Parent page showing title as text |
| %%link%% | URL pointing to page |
| %%content%% | Page content |
| %%content{n}%% | Numbered content section |
| %%summary%% | Summary of content |
| %%first_paragraph%% | The first paragraph of the page |
| %%tags%% | Page visible tags (not starting with underscore) |
| %%tags_linked%% | Page visible tags linked to system:page-tags/tag/{tag} |
| %%tags_linked\|link_prefix%% | Page visible tags linked to link_prefix{tag} |
| %%_tags%% | Page hidden tags (starting with underscore) |
| %%_tags_linked%% | Page hidden tags linked to system:page-tags/tag/{tag} |
| %%_tags_linked\|link_prefix%% | Page hidden tags linked to link_prefix{tag} |
| %%form_data{name}%% | Field value from pagedata formif any |
| %%form_raw{name}%% | For select and pagepath fields, the internal value saved in the page form data. For other field types, empty. |
| %%form_label{name}%% | The label of the field as defined in thedata formif any |
| %%form_hint{name}%% | The hint of the field as defined in thedata formif any |
| Page reporting |  |
| %%children%% | Number of child pages |
| %%comments%% | Number of comments on page |
| %%size%% | Number of characters in page |
| %%rating%% | Page rating value |
| %%rating_votes%% | Number of votes (only for 5-star rating) |
| %%rating_percent%% | Percentage value of rating (only for 5-star rating) |
| %%revisions%% | Number of revisions to page |
| Current context |  |
| %%site_title%% | Title of current site |
| %%site_name%% | Wikidot Unix name for site |
| %%site_domain%% | Active domain name of current site |

Date formatting:

- All _at fields are dates and allow a custom format via the `|*format*` specifier.

Most tokens from PHP's [strftime](http://php.net/manual/en/function.strftime.php) are accepted. You may find [the howto](http://community.wikidot.com/howto:frontforum-date-variable) contributed by community useful.

An example of how these can be used in a blog could be (e.g. in `blog:_template`:

```
by %%created_by%% on %%created_at|%e %B %Y%%
rating: %%rating%%, tags: %%tags%%

%%content%%
```

## Changing the template

When you edit the `_template` page for the given category, all pages from the category will be recompiled to include the changed template.

## Hidden pages

Pages whose name starts with an underscore (like "_start", "_header", etc.) are 'hidden' pages and are not affected by the template.

## Inexisting page templates

If you will go to the address of the page that not exists, you'll a get a note similar to the following:

# The page does not (yet) exist.

The page *james* you want to access does not exist.

- create page

You can use a template which will change the default "non-existing page" message to the custom one. All you need to do is to edit a page:

- [http://site-name.wikidot.com/_404](http://site-name.wikidot.com/_404) — it will change the message for all non-existing pages on your site
- [http://site-name.wikidot.com/category:_404](http://site-name.wikidot.com/category:_404) — it will change the message for all non-existing pages within particular category

Note: Of course, you need to change "site-name" to your Site's address and "category" to your own category.

In the template, you may want to have a link which allow users to create a page which don't exist. To do this, simply use:

```
[[button edit]]
```

You may also want to change the title of _404 page to desired one, e.g. "This site does not exist".

%%404_page_name%% variable puts a name of the page which doesn't exist yet, i.e. if your template looks like this:

```
+ Oops! We can't find the page: //@@%%404_page_name%%@@//

Click [[button edit text="here"]] to create one.
```

And you will go to the page [http://site-name.wikidot.com/a-great-new-page](http://site-name.wikidot.com/a-great-new-page) it will result in:

# Oops! We can't find the page:a great new page

Click here to create one.
