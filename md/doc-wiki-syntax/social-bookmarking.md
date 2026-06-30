# Social Bookmarking

> Documentation > Wiki Syntax > Social Bookmarking

It is easy to add "social bookmarking" buttons to your pages — just write `[[social]]` (without any parameters) and get:

[![BlinkList](https://d3g0gp89917ko0.cloudfront.net/v--7690939296dc/common--images/social/blinklist.png)](http://www.blinklist.com/index.php?Action=Blink/addblink.php&Description=&Url=http%3A%2F%2Fwww.wikidot.com%2Fdoc-wiki-syntax%3Asocial-bookmarking&Title=TITLE)[![blogmarks](https://d3g0gp89917ko0.cloudfront.net/v--7690939296dc/common--images/social/blogmarks.png)](http://blogmarks.net/my/new.php?mini=1&simple=1&url=http%3A%2F%2Fwww.wikidot.com%2Fdoc-wiki-syntax%3Asocial-bookmarking&title=TITLE)[![del.icio.us](https://d3g0gp89917ko0.cloudfront.net/v--7690939296dc/common--images/social/delicious.png)](http://del.icio.us/post?url=http%3A%2F%2Fwww.wikidot.com%2Fdoc-wiki-syntax%3Asocial-bookmarking&title=TITLE)[![digg](https://d3g0gp89917ko0.cloudfront.net/v--7690939296dc/common--images/social/digg.png)](http://digg.com/submit?phase=2&url=http%3A%2F%2Fwww.wikidot.com%2Fdoc-wiki-syntax%3Asocial-bookmarking&title=TITLE)[![Fark](https://d3g0gp89917ko0.cloudfront.net/v--7690939296dc/common--images/social/fark.png)](http://cgi.fark.com/cgi/fark/edit.pl?new_url=http%3A%2F%2Fwww.wikidot.com%2Fdoc-wiki-syntax%3Asocial-bookmarking&new_comment=TITLE&new_comment=Wikidot+-+Free+and+Pro+Wiki+Hosting&linktype=Misc)[![feedmelinks](https://d3g0gp89917ko0.cloudfront.net/v--7690939296dc/common--images/social/feedmelinks.png)](http://feedmelinks.com/categorize?from=toolbar&op=submit&url=http%3A%2F%2Fwww.wikidot.com%2Fdoc-wiki-syntax%3Asocial-bookmarking&name=TITLE)[![Furl](https://d3g0gp89917ko0.cloudfront.net/v--7690939296dc/common--images/social/furl.png)](http://www.furl.net/storeIt.jsp?u=http%3A%2F%2Fwww.wikidot.com%2Fdoc-wiki-syntax%3Asocial-bookmarking&t=TITLE)[![LinkaGoGo](https://d3g0gp89917ko0.cloudfront.net/v--7690939296dc/common--images/social/linkagogo.png)](http://www.linkagogo.com/go/AddNoPopup?url=http%3A%2F%2Fwww.wikidot.com%2Fdoc-wiki-syntax%3Asocial-bookmarking&title=TITLE)[![NewsVine](https://d3g0gp89917ko0.cloudfront.net/v--7690939296dc/common--images/social/newsvine.png)](http://www.newsvine.com/_tools/seed&save?u=http%3A%2F%2Fwww.wikidot.com%2Fdoc-wiki-syntax%3Asocial-bookmarking&h=TITLE)[![Netvouz](https://d3g0gp89917ko0.cloudfront.net/v--7690939296dc/common--images/social/netvouz.png)](http://www.netvouz.com/action/submitBookmark?url=http%3A%2F%2Fwww.wikidot.com%2Fdoc-wiki-syntax%3Asocial-bookmarking&title=TITLE&description=TITLE)[![Reddit](https://d3g0gp89917ko0.cloudfront.net/v--7690939296dc/common--images/social/reddit.png)](http://reddit.com/submit?url=http%3A%2F%2Fwww.wikidot.com%2Fdoc-wiki-syntax%3Asocial-bookmarking&title=TITLE)[![YahooMyWeb](https://d3g0gp89917ko0.cloudfront.net/v--7690939296dc/common--images/social/yahoomyweb.png)](http://myweb2.search.yahoo.com/myresults/bookmarklet?u=http%3A%2F%2Fwww.wikidot.com%2Fdoc-wiki-syntax%3Asocial-bookmarking&=TITLE)[![Facebook](https://d3g0gp89917ko0.cloudfront.net/v--7690939296dc/common--images/social/facebook.gif)](http://www.facebook.com/share.php?u=http%3A%2F%2Fwww.wikidot.com%2Fdoc-wiki-syntax%3Asocial-bookmarking)

//<![CDATA[

            var socialspan = $j("#social95643")[0];
            var els = socialspan.getElementsByTagName("a");
            for (var i=0;i<els.length;i++) {
                els[i].href = els[i].href.replace("TITLE", encodeURIComponent(document.title));
            }
//]]>

This is equivalent to:

```
[[social blinklist,blogmarks,connotea,del.icio.us,digg,fark,feedmelinks,furl,linkagogo,newsvine,netvouz,reddit,simpy,spurl,wists,yahoomyweb,facebook]]
```

You can also choose only selected services, e.g. to show digg, furl, del.icio.us and Facebook use:

```
[[social digg,furl,del.icio.us,facebook]]
```

and get:

[![digg](https://d3g0gp89917ko0.cloudfront.net/v--7690939296dc/common--images/social/digg.png)](http://digg.com/submit?phase=2&url=http%3A%2F%2Fwww.wikidot.com%2Fdoc-wiki-syntax%3Asocial-bookmarking&title=TITLE)[![Furl](https://d3g0gp89917ko0.cloudfront.net/v--7690939296dc/common--images/social/furl.png)](http://www.furl.net/storeIt.jsp?u=http%3A%2F%2Fwww.wikidot.com%2Fdoc-wiki-syntax%3Asocial-bookmarking&t=TITLE)[![del.icio.us](https://d3g0gp89917ko0.cloudfront.net/v--7690939296dc/common--images/social/delicious.png)](http://del.icio.us/post?url=http%3A%2F%2Fwww.wikidot.com%2Fdoc-wiki-syntax%3Asocial-bookmarking&title=TITLE)[![Facebook](https://d3g0gp89917ko0.cloudfront.net/v--7690939296dc/common--images/social/facebook.gif)](http://www.facebook.com/share.php?u=http%3A%2F%2Fwww.wikidot.com%2Fdoc-wiki-syntax%3Asocial-bookmarking)

//<![CDATA[

            var socialspan = $j("#social11249")[0];
            var els = socialspan.getElementsByTagName("a");
            for (var i=0;i<els.length;i++) {
                els[i].href = els[i].href.replace("TITLE", encodeURIComponent(document.title));
            }
//]]>

**Tip:** Use social bookmarking! It is always a good idea to put social shortcuts under an article or inside your side bar.
