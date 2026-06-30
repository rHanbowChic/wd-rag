# Html Blocks

> Documentation > Wiki Syntax > Html Blocks

Create HTML blocks by using `[[html]] … [[/html]]` tags (each on its own line). HTML block is a Code Block inserted in the IFRAME. It makes [HTML - scripting](http://community.wikidot.com/howto:use-html-scripting) much easier.

```

[[html]]
<h1>Custom HTML</h1>
<p>Something else</p>
<img src="anything.png" alt="hello ;-)"/>
[[/html]]
```

All wiki syntax inside a html block is treated as literal text and not processed.

You can apply styles (both by means of <style type="text/css">…</style> and <element style="…">) to elements, but styling html and body (that are added transparently to your content if needed) is not supported. If you need any styling done to the top level elements, do this by wrapping the whole content of [[html]] block in div with proper style, for example:

```
[[html]]
<div style="background-color: black; color: lightgreen">
<p>This is a test.</p>
</div>
[[/html]]
```

This renders the whole HTML block black with text color light green:

Each HTML block on a page has a unique URL that lets you access it individually. You can do it by right clicking on the HTML block element on the rendered page and choose "Show only this frame" and check the web address.
