# The 'static' field type

This shows non-editable text and lets the form designer add text and formatting to the form. Static fields are not stored in the page. Static fields get their value from the 'value' property.

```
[[form]]
fields:
  version:
    type: static
    value: 'Non-storable field with with **bold**, //strike// and __underline__.'
[[/form]]
```

The specific properties you can use on a static field:

- **value**: sets the value of the field

The static field can use most wiki syntax and you can easily add line breaks by using the pipe character (**|**) to start a block of text for the value property. For example, the static field below contains the source code from the **Inline Formatting** documentation section. Formatting your value property this way is easy since all of the code is parsed as-is and you don't have to worry about escaping single quotes or adding line break code.:

```
[[form]]
fields:
  date-1:
    type: date
    hint: 'mm/dd/yyyy'
    label: 'Date 1'
    options:
      showOn: button
      showAnim: slideDown
      duration: 4000
  header-1:
    type: static
    label: 'Inline Formatting Docs'
    value: |
             //italic text//    italic text
             ||~ what you type ||~ what you get ||
             || {{ '{{' }}@@//italic text//@@}} || //italic text// ||
             || {{ '{{' }}@@**bold text**@@}} || **bold text** ||
             || {{ '{{' }}@@//**italic and bold**//@@}} || //**italic and bold**// ||
             || {{ '{{' }}@@__underline text__@@}} || __underline text__ ||
             || {{ '{{' }}@@--strikethrough text--@@}} || --strikethrough text-- ||
             || {{ '{{' }}@@{{ '{{' }}teletype (monospaced) text}}@@}} || {{ '{{' }}teletype (monospaced) text}} ||
             || {{ '{{' }}@@normal^^superscript^^@@}} || normal^^superscript^^ ||
             || {{ '{{' }}@@normal,,subscript,,@@}} || normal,,subscript,, ||
             || {{ '{{' }}@@[!-- invisible comment --]@@}} || [!-- invisible comment --] ||
             || {{ '{{' }}@@[[span style="color:red"]]custom //span// element[[/span]]@@}} || [[span style="color:red"]]custom //span// element[[/span]] ||
             || {{ '{{' }}@@##blue|predefined## or ##44FF88|custom-code## color@@}} || ##blue|predefined## or ##229966|custom-code## color ||

             [[div class="alert alert-info"]]
             You can use user-defined {{ '{{' }}ID}} arguments in **@@[[span]]...[[/span]]@@** tags, which is extremely useful building sites using [http://getbootstrap.com Bootstrap]. Please note that every user-defined {{ '{{' }}ID}} will have a {{ '{{' }}"u-"}} prefix added in the output HTML for the security reasons.
             [[/div]]
[[/form]]
```

The same code can be entered as shown below by wrapping the whole string in double quotes and then using **\n** to indicate where line break should fall. It will render the same result. You can see that the above code is much easier to read and to write.

```
[[form]]
fields:
  date-1:
    type: date
    hint: mm/dd/yyyy
    label: 'Date 1'
    options:
      showOn: button
      showAnim: slideDown
      duration: 4000
  header-1:
    type: static
    label: 'Inline Formatting Docs'
    value: "//italic text//    italic text\n||~ what you type ||~ what you get ||\n|| {{ '{{' }}@@//italic text//@@}} || //italic text// ||\n|| {{ '{{' }}@@**bold text**@@}} || **bold text** ||\n|| {{ '{{' }}@@//**italic and bold**//@@}} || //**italic and bold**// ||\n|| {{ '{{' }}@@__underline text__@@}} || __underline text__ ||\n|| {{ '{{' }}@@--strikethrough text--@@}} || --strikethrough text-- ||\n|| {{ '{{' }}@@{{ '{{' }}teletype (monospaced) text}}@@}} || {{ '{{' }}teletype (monospaced) text}} ||\n|| {{ '{{' }}@@normal^^superscript^^@@}} || normal^^superscript^^ ||\n|| {{ '{{' }}@@normal,,subscript,,@@}} || normal,,subscript,, ||\n|| {{ '{{' }}@@[!-- invisible comment --]@@}} || [!-- invisible comment --] ||\n|| {{ '{{' }}@@[[span style=\"color:'red\"]]custom //span// element[[/span]]@@}} || [[span style=\"color:red\"]]custom //span// element[[/span]] ||'\n|| {{ '{{' }}@@##blue|predefined## or ##44FF88|custom-code## color@@}} || ##blue|predefined## or ##229966|custom-code## color ||\n\n[[div class=\"alert alert-info\"]]\nYou can use user-defined {{ '{{' }}ID}} arguments in **@@[[span]]...[[/span]]@@** tags, which is extremely useful building sites using [http://getbootstrap.com Bootstrap]. Please note that every user-defined {{ '{{' }}ID}} will have a {{ '{{' }}\"u-\"}} prefix added in the output HTML for the security reasons.\n[[/div]]"
[[/form]]
```

Wikidot super guru, Kenneth Tsang ([tsangk](http://www.wikidot.com/user:info/tsangk)), created a great [Wikidot Data Form Fixer](http://convert.wikidot.com/) tool that you can use to check the syntax and formatting of your data forms. It's highly recommend to make sure your code is 100% compliant with the formatting rules.
