# Layout Reference

> Documentation > Layout Reference

# Page layout

The tree below represents the structure of pages that is valid for all wikidot-powered sites. This reference should help all these who wish to develop custom CSS themes.

- `div#container`
  - `div#header`
    - `h1`
      - `a`
        - `span` (with the name of the site)
    - `h2` (if subtitle exists)
      - `span` (with the subtitle of the site)
    - `div#top-bar` (if top-bar navigation element exists)
    - `div#login-status`
    - `div#header-extra-div-1` (extra divs for CSS design)
      - `span`
    - `div#header-extra-div-2` (extra divs for CSS design)
      - `span`
    - `div#header-extra-div-3` (extra divs for CSS design)
      - `span`
  - `div#content-wrap`
    - `div#side-bar` (if side-bar navigation element exists)
    - `div#main-content`
      - `div#action-area-top`
      - `div#page-title`
      - `div#breadcrumbs`
      - `div#page-content` (main content of the page)
      - `div#page-info`
      - `div#page-options-bottom.page-options-bottom`
      - `div#page-options-bottom-2.page-options-bottom`
      - `div#action-area`
  - `div#footer`
    - `div.options`
  - `div#license-area`
- `div#extra-div-1` (extra divs for CSS design)
  - `span`
- `div#extra-div-2`
  - `span`
- `div#extra-div-3`
  - `span`
- `div#extra-div-4`
  - `span`
- `div#extra-div-5`
  - `span`
- `div#extra-div-6`

# Custom layout

Users with Pro subscription can create their own custom layout, i.e. HTML structure of the every page on the Wiki inside the `<body> … </body>` tags. In other words, the default layout, which reference is available above, may be altered to fit specific user needs for creating sophisticated and highly custom themes.

For security reasons, user can't use `<body>` tag or `id=""` elements. Within the layout, you may want to use so called Modules (independent from [these modules](http://www.wikidot.com/doc:modules)), i.e. elements which are responsible for rendering vital page and interface elements.

List of available modules:

```
[[module NaviBar]] - Wikidot's branded top bar
[[module FooterBar]] - Wikidot's Interesting Sites
[[module LoginStatus]] - Sign in/Create account button or User logged in
[[module PageOptionsBottom]] - Page options: edit, tags etc.
[[action_area]] - Indicates the position on the page that PageOptionsBottom will use when it needs to display additional content, e.g. a file upload form. It's needed for correct functioning of PageOptionsBottom module

[[module AdModuleAboveContent]] - Ad box for Pro users
[[module AdModuleBelowContent]] - Ad box for Pro users
[[module AdModuleAboveSidebar]] - Ad box for Pro users
[[module AdModuleBelowSidebar]] - Ad box for Pro users
[[module AdModuleBelowFooter]] - Ad box for Pro users
[[module Ad label="custom_location"]] - Ad box for Pro users (custom location support)

[[site_name]] - Site title, former <h1>
[[site_subtitle]] - Site subtitle, former <h2>
[[content]] - It's rather obvious, content of the page
[[search_box]] - Box for searching within a site
[[site_locked]] - Information about a lock on the site
[[page_title]] - Page title
[[breadcrumbs]] - Breadcrumbs elements
[[tags]] - Displays list of tags
[[topbar]] - Top navigation
[[sidebar]] - Side navigation, displayed if enabled
[[ssl_warning]] - Warning about disabled SSL if Pro+ subscription expires
[[page_not_exists]] - Information displayed when page does not exist
[[license_text]] - License text (set up in Admin Panel)
[[footer]] - Inserts footer, default or custom
```

### Possible if statement in layouts

```
[[if name]]
if code ...
[[/if]]

[[if !name]]
if code ...
[[/if]]

[[if name]]
if code ...
[[else]]
else code ...
[[/if]]
```

List of available if statements:

```
[[if site_subtitle]]
[[if site_locked]]
[[if page_title]]
[[if breadcrumbs]]
[[if tags]]
[[if topbar]]
[[if sidebar]]
[[if ssl_warning]]
[[if page_exists]]
[[if license_text]]
[[if custom_footer]]
```

# Forum structure

Forum elements are embedded within the `div#page-content` element. Only elements below this one are listed.

## Forum start view (list of groups and categories)

- `div.forum-start-box`
  - `div.forum-group` - for each of the groups (top-level forum structures)
    - `div.head`
      - `div.title`
      - `div.description`
    - `div`
      - `table`
        - `tr.head` - description of fields
          - `td`
          - `td`
          - `td`
          - `td`
        - `tr` - for each of categories in the group
          - `td.name`
            - `div.title`
            - `div.description`
          - `td.threads`
          - `td.posts`
          - `td.last`

## Category view (list of threads)

## Thread view
