# FeaturedSite Module

> Documentation > Modules > FeaturedSite Module

## Description

FeaturedSite module is very similar to SiteGrid, but it's displaying **only one** wiki site thumbnail and the thumbnail is much bigger.

This module has no attributes.

## Example

```
[[module FeaturedSite]]
community.wikidot.com
[[/module]]
```

Which transfers to…


//<![CDATA[
	OZONE.dom.onDomReady(function(){
		var els = YAHOO.util.Dom.getElementsByClassName('featured-site-hovertip', 'div', 'special9387424');
		for(var i=0; i<els.length; i++){
			els[i].id = els[i].id.replace(/1$/, '');
		}
		var els = YAHOO.util.Dom.getElementsByClassName('thumbnail', 'img', 'special9387424');
		for(var i=0; i<els.length; i++){
			els[i].alt = '';
		}
		OZONE.dialog.hovertip.dominit("special9387424", {delay: 100, noCursorHelp: true});
	}, "dummy-ondomready-block");
//]]>
