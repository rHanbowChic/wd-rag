# Universal Escaping

> Documentation > Wiki Syntax > Universal Escaping

If you want to put arbitrary characters or HTML entities (including Unicode entities) into your text, use @< … >@. Inside this sequence, convert each "&" to "&amp;", each "<" to "&lt;" and each ">" to "&gt;".

The escape sequence will decode HTML entities like &lt; including:

- entities such as &copy; (©)
- numeric entities like &#252; (ü)
- Unicode entities like &#8212; (—) or &auml; (ä)

## Live example

```
HTML entities: @<U umlaut: &#252;>@
@<[[code]]>@
@<Hello world @@ !!!!>@
@<Something **not** bold>@
@<[[module ListPages]]>@
@<Copyright sign: &copy;>@
@<[[/code]]>@
Or, @<@&lt;>@ and @<&gt;@>@
```

Which gives:

HTML entities: U umlaut: ü

[[code]]

Hello world @@ !!!!

Something **not** bold

[[module ListPages]]

Copyright sign: ©

[[/code]]

Or, @< and >@
