# Layout elements

> Documentation > Wiki Syntax > Layout elements

## Tab view

Tab view is a container that creates some clickable tabs that allow to switch between content to show.

**NOTE: TabView breaks TOCs, anchor links and back button**

- you can't link to anchor inside of a tab
- TOC won't link properly to any header inside of a tab
- if you click a link from within a tab and go back, you will be always shown the first tab

To generate a *tabview*, i.e. a set of tabs, the following syntax can be used:

```
[[tabview]]
[[tab Title of Tab No. 1]]
Content of Tab No. 1.
[[/tab]]
[[tab Title of Tab No. 2]]
Content of Tab No. 2.
[[/tab]]
[[tab Title of Tab No. 3]]
Content of Tab No. 3.
[[/tab]]
[[/tabview]]
```

This will produce the following tabset:

//<![CDATA[
OZONE.dom.onDomReady(function(){
        var tabView3cb819bc1abfbfbe85cb069d950237c1 = new YAHOO.widget.TabView('wiki-tabview-3cb819bc1abfbfbe85cb069d950237c1');
                }, "dummy-ondomready-block");

//]]>

Tabs will accept any content, but at the moment it is not possible to nest tabviews.

Another example of `tabview` can be found at our Snippets Wiki at [http://snippets.wikidot.com/code:tabs](http://snippets.wikidot.com/code:tabs)
