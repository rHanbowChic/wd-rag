# Redirect Module

> Documentation > Modules > Redirect Module

## Description

The Redirect module performs a "301 Permanently Moved" redirection, i.e. it tells a web browser to request another web page.

## Attributes

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| destination | yes | page-name or URL | none | where to redirect? |

When the `destination` attribute is just an alphanumeric string, e.g. "start", the page which contains the Redirect module will automatically forward the browser to the wiki page called "start". If destination is the whole URL address (e.g. "[http://slashdot.org](http://slashdot.org)"), the browser will be redirected to this external address.

## Mapping

If the `destination` attribute ends with a slash, e.g. destination="start**/**" or destination="http://www.example.com**/**", the current URL will be mapped to the destination in the following way. The code for the module would be:

```
[[module Redirect destination="http://www.example.com/base/"]]
```

Now if the Redirect module is placed on page http://your-wiki.wikidot.com/redir the following mapping will be performed:

| from | to |
| --- | --- |
| http://your-wiki.wikidot.com/redir | http://www.example.com/base/ |
| http://your-wiki.wikidot.com/redir/mapped-path | http://www.example.com/base/mapped-path |
| http://your-wiki.wikidot.com/redir/mapped-path/file1.html | http://www.example.com/base/mapped-path/file1.html |

## Preventing the redirect

If the Redirect module redirected the browser always there would be no way to edit the actual page. The solution is to pass an extra parameter to the module in the URL as follows:

http://your-wiki.wikidot.com/page-with-redirect/**noredirect/true**

There should be an information box where the module is placed.

Working with the Redirect module might not be very convenient but even of you have to do this you will not configure it every day ;-)
