# SiteGrid Module

> Documentation > Modules > SiteGrid Module

## Description

SiteGrid module gives you a possibility to create a grid of thumbnails of sites on Wikidot with a descriptions and some details in a form of pop-up when you move your mouse cursor over thumbnail.

SiteGrid module is sorting thumbnails randomly. It's used on the main Wikidot page to list featured sites.

Inside the module you have to put a list either of the names of sites, i.e. **community** (if the address is *community.wikidot.com*) or full address, i.e. **community.wikidot.com** or **www.digistan.org** (if a site has a custom domain).

## Attributes

| Attribute | Required | Allowed values | Default | Description |
| --- | --- | --- | --- | --- |
| limit | no | any integer | none | Limiting the number of displayed thumbnails from the predefined list |

## Examples

```
[[module SiteGrid limit="20"]]
wikipiano
michal
wikiwealth
quake
fretsonfire
squark
istorijska-biblioteka
angels
string-theory
fifa360
liquidrescale
qttabbar
osx86
moonworld
wiihd
wherearethejoneses
sniki.org
wow-unity
heroesmush
bvswiki.com
scp-wiki
www.digistan.org
mechanics
aeldaria
coffeetime
f-g
thehurl
arch1k
comicbooks
karmalab
scmapdb
tibasicdev
gamedesign
herald-tips-tricks
swib
skyscraper-en
terrasdeportugal
scmapdb
l4dmapdb
[[/module]]
```

Which transfers to…


//<![CDATA[
	OZONE.dom.onDomReady(function(){
		var els = YAHOO.util.Dom.getElementsByClassName('featured-site-hovertip', 'div', 'special9387423');
		for(var i=0; i<els.length; i++){
			els[i].id = els[i].id.replace(/0$/, '');
		}
		var els = YAHOO.util.Dom.getElementsByClassName('thumbnail', 'img', 'special9387423');
		for(var i=0; i<els.length; i++){
			els[i].alt = '';
		}
		OZONE.dialog.hovertip.dominit("special9387423", {delay: 100, noCursorHelp: true});
	}, "dummy-ondomready-block");
//]]>



This is a long list of featured sites, but only 20 are displayed in a random order.
