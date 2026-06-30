# Embedding code from other sites

> Documentation > Wiki Syntax > Embedding code from other sites

Sometimes web sites (mainly social-oriented ones) allow you to paste a code block directly into other pages in order to increase your site functionality or embed some content from the original site.

## [[embed]]tag

The `[[embed]]` block tag allows you to do the same with your wiki pages. E.g. to display del.icio.us tag cloud as generated from [http://del.icio.us/help/tagrolls](http://del.icio.us/help/tagrolls) simply wrap the html code:

```
[[embed]]
<script type="text/javascript" src="http://del.icio.us/feeds/js/tags/michal_frackowiak?icon;size=12-35;color=87ceeb-0000ff;title=my%20del.icio.us%20tags"></script>
[[/embed]]
```

For the list of supported services please see the page: [Embedding code from other services](/doc:embedding).

Please note that if the code contains `<script type="text/javascript"…` i.e. just JavaScript, the content will not be fully rendered when you click `preview` while editing the page. It should be there however when you view the page afterwards.

## [[iframe]]element

Using the *iframe* element one can embed content of any other web page. The syntax is

```
[[iframe url-source attributes]]
```

and it translates into HTML tags `<iframe src="url-source" attributes></iframe>`. The allowed attributes are: frameborder (0 or 1 allowed), align (left, right, top, bottom, middle), height (number of pixels or %), width (number of pixels or %), scrolling (yes or no), class, style
