# Inline Formatting

> Documentation > Wiki Syntax > Inline Formatting

| what you type | what you get |
| --- | --- |
| //italic text// | italic text |
| **bold text** | bold text |
| //**italic and bold**// | italic and bold |
| __underline text__ | underline text |
| --strikethrough text-- | strikethrough text |
| {{ '{{' }}teletype (monospaced) text}} | teletype (monospaced) text |
| normal^^superscript^^ | normalsuperscript |
| normal,,subscript,, | normalsubscript |
| [!-- invisible comment --] |  |
| [[span style="color:red"]]custom //span// element[[/span]] | customspanelement |
| ##blue\|predefined## or ##44FF88\|custom-code## color | predefinedorcustom-codecolor |

Adding underscore to **span** element **[[span_ ]]** will truncate whitespaces around it which prevents creation of random [new lines and paragraphs](/doc-wiki-syntax:paragraphs-and-newline). It's simplifices creation of complex HTML syntax like [Bootstrap components](http://getbootstrap.com/components/)

You can use user-defined `ID` arguments in **[[span]]...[[/span]]** tags, which is extremely useful building sites using [Bootstrap](http://getbootstrap.com). Please note that every user-defined `ID` will have a `"u-"` prefix added in the output HTML for the security reasons.

To make your source more readable, you can add the `"u-"` prefix yourself. For example, these 2 bits of wiki syntax will output the same HTML:

---

**`"u-"` prefix will be added to `mySpan` automatically when the page is saved**

```
[[span id="mySpan"]]My span element[[/span]]
```

**`"u-"` prefix will not be added to since it already exists**

```
[[span id="u-mySpan"]]My span element[[/span]]
```

**HTML output from both examples**

```
<span id="u-mySpan">My span element</span>
```
