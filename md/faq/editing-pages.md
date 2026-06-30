# Editing Pages FAQ

> Documentation > Editing Pages FAQ

### How do I edit a page?

Created by: [![samoore](https://www.wikidot.com/avatar.php?userid=53495&amp;size=small&amp;timestamp=1482843329)](http://www.wikidot.com/user:info/samoore)[samoore](http://www.wikidot.com/user:info/samoore)

### What is the "Wiki Syntax"?

Wiki syntax (also known as Wiki markup, Wiki language, Wiki text) is a markup language as a simple alternative to HTML code that allows quick content creation. There is no common Wiki syntax but each Wiki engine (such as MediaWiki (Wikipedia), MoinMoin, TWiki and others) have their own specific syntax. In our (Wikidot) syntax e.g. to create link to a different website you simply write `[http://www.example.com visit this!]` instead of HTML:

`<a href="http://www.example.com">visit this!</a>`

To learn more about the Wiki Syntax go to our [Wiki Syntax documentation](/doc:wiki-syntax).

### So I have edited a page. Is the previous content lost?

Not at all. All pages have "history" which consists of a series of revisions. Each change (title, content, rename, file upload etc.) creates a new revision. By clicking the *history* button at the bottom of a page you can browse the list of all revisions of a page.

In principle the rule is **no content is lost**. This applies perfectly to pages - pages have history.

The rule does not apply to uploaded files due to limited file storage size. So Users (who have permission) can replace/delete files.

### Why are there 3 modes of editing a page?

For convenience. It works fine when your pages are very long and editing the whole content is not always the best solution.

So the modes are:

- whole page edit
- section edit
- append

Each of these modes introduces a page edit lock such that no Users can both edit a page at the same time of their locks conflict. But as you might expect different users can edit non-overlapping sections of the same page at the same time. Or edit a section and append. These locks do not conflict.

Anyway - with long pages it is much easier to use the section mode or append mode than editing the whole long page.

### Why is there no WYSIWYG editor?

WYSIWYG editor (What You See Is What You Get, such as [TinyMCE](http://tinymce.moxiecode.com/) or [FCKeditor](http://www.fckeditor.net/)) are still not very suitable for editing Wiki content. Although we would like to have an intuitive content editor the available ones do not meet our requirements since it is very difficult to produce well-structured documents with such tools.

So what we ended with is "aided editing" - you still edit the raw source (which is a great advantage - produces clean, structured code) but the editor provides numerous buttons and wizards to make things a lot easier.

### Why the buttons above the text input area do not work for me?

Probably you use a non-standard browser. At the moment the interactive editor works with all major browsers, i.e. Mozilla Firefox, Opera and Internet Explorer.

**Remember the buttons are only for your convenience and you can edit and save the content even if the buttons do not work!**
