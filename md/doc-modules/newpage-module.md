# NewPage Module

> Documentation > Modules > NewPage Module

## Description

Displays a form that allows easier creation of new pages.

## Attributes

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| category | no | name of a page category | none | forces the given page category by prepending the page name by thecategoryname:/Note: Cannot use_defaultcategory for this. |
| template | no | name of a template page | none | a page (or comma-separated list of pages) to be used as a template for the new page |
| size | no | any positive integer | 30 | size of the displayed input field |
| button | no | any string | "create page" | text displayed within thecreate pagebutton |
| format | no | any valid regular expression | none | forces the input value to match the required format |
| tags | no | space-separated list of tags | none | automatically adds given tags to created pages |
| parent | no | name of apageorcategory:page | none | automatically adds parent page to created pages |

### Attributes for AutoSave function

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| mode | no | edit,save-and-refresh,save-and-go | edit | "edit" takes you to an editor. "save-and-refresh" saves the page and refreshes the current page. "save-and-go" saves the page and goes to it (without editor) unlessgoToattribute is passed |
| goTo | no | valid page name | none | specifies which page to go to after automatically saving a page |

Any page that would be used as a template (passed via the `template` attribute) must belong to the `template` category, i.e. its name should contain the `template:` prefix, e.g. `template:pagename`. And must already exist.

If you choose several templates (names separated by a comma) an additional field will be displayed asking to choose a template for the page that a user wishes to create.

If you want new pages to fit match a given pattern, you can use the `format` attribute. To learn more about regular expressions you can see the [Pattern Syntax description](http://pl2.php.net/manual/en/reference.pcre.pattern.syntax.php) at the PHP main page.

Anyway, you could do:

`format="/^[0-9]{5}$/"` — page names would consist of exactly 5 numbers

`format="/^[\d]{4}[- \/.](0[1-9]|1[012])[- \/.](0[1-9]|[12][0-9]|3[01])$/"` — a simple expression to match a valid date (not 100% accurate, assumes all months have 31 days)

etc.

> You cannot use NewPage module to create a hidden page (i.e. page whose name starts with an underscore — "_"). On the feedback site, there is a wish to change it. If you also feel this way, [rate it up](http://feedback.wikidot.com/wish:404).

## Examples

To make creating pages within the *doc* category:

```
[[module NewPage category="doc"]]
```

Results in:

(you will not be able to create a page in the documentation section - this is just for demonstration purposes).

To use a template:

```
[[module NewPage template="template:module"]]
```

To use several templates to choose from:

```
[[module NewPage template="template:module,template:howto"]]
```

And now a perfect module to insert into you side-bar for easier page creation:

```
+++ Add a new page
[[module NewPage size="15" button="new page"]]
```

### Add a new page
