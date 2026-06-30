# Code Blocks

> Documentation > Wiki Syntax > Code Blocks

Create code blocks by using `[[code]]…[[/code]]` tags (each on its own line).

```
This is an example code block!
```

All wiki syntax inside a code block *except* [[include]] tags is treated as literal text and not processed. To prevent an include tag from being processed, put a single space in front of it.

Each code block on a page has a unique URL that lets you access it individually. This is especially useful for code blocks that contain CSS code (type = "css"):

```
http://mysite.wikidot.com/category:page/code
http://mysite.wikidot.com/category:page/code/2  -- second block
```

This way you can extract code blocks defined in the page source itself, without taking any _template into account. To access code blocks form page source combined with _template, use the following URLs:

```
http://mysite.wikidot.com/category:page/code_  -- note the trailing underscore
http://mysite.wikidot.com/category:page/code_/2  -- second block
```

To create PHP blocks that get automatically colorized when you use PHP tags, simply surround the code with `[[code *type="php"*]]…[[/code]]` tags).

To get PHP code colorized you should surround it with <?php.. ?>.

Wikidot.com uses PEAR::Text_Highlighter and supports a number of color schemes. Here is what is supported (allowed type values):

php, html, cpp, css, diff, dtd, java, javascript, perl, python, ruby, xml.

```
[[code type="php"]]
<?php
/* comment */
for($i=0; $i<100; $i++){
echo "number".$i."\n";
}
?>
[[/code]]
```

```

<?php
/* comment */
for($i=0; $i<100; $i++){
echo "number".$i."\n";
}
?>
```
