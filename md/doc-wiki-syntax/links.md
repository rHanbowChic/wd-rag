# Links

> Documentation > Wiki Syntax > Links

## Internal links

Unlike some other wiki engines Wikidot.com does not process SquashedAndCapitalized words as page links. Instead any link should be marked with 3 nesting square brackets.

If a page address contains disallowed characters the address will be "unixified" to contain only allowed chars. The displayed name however will maintain original form.

| what you type | what you get | comments |
| --- | --- | --- |
| [[[link-to-a-page]]] | link-to-a-page | using raw page name |
| [[[link "TO" a; pagE]]] | link "TO" a; pagE | automatic purification of destination page |
| [[[category: sample page]]] | sample page | linked to a page with category |
| [[[some page\| custom text]]] | custom text | using custom text |
| [[[doc\|Documentation]]] | Documentation | linking to an existing page (different color) |
| [[[some page\|]]] | some-page | using page title as link text |
| [[[doc#toc1\|Section 1]]] | Section 1 | linking to an anchor (first section) |
| [[[doc#toc1]]] | doc | linking to an anchor (first section) |
| [[[/\| Home]]] | Home | links to your home page |

## URLs

| what you type | what you get | comments |
| --- | --- | --- |
| [[[http://www.wikidot.com \| Wikidot]]] | Wikidot | named link (custom anchor) |
| [[[*http://www.wikidot.com \| Wikidot]]] | Wikidot | named link (custom anchor), opened in new window/tab |
| [[[/category:page/option1/option2 \| link text]]] | link text | You can create shorter links to your own site with/parameters without writing whole http link./E.g. you can use/[[[/blog:post/edit/true \| edit this post]]]/instead of/[[[http://site.wikidot.com/ blog:post/edit/true \| edit this post]]] |
| http://www.wikidot.com | http://www.wikidot.com | simple inline link |
| [http://www.wikidot.com wikidot] | wikidot | named link (custom anchor) |
| *http://www.wikidot.com/[*http://www.wikidot.com wikidot] | http://www.wikidot.com/wikidot | opens in a new window |
| [[a href="http://www.wikidot.com"]] Wikidot[[/a]] | Wikidot | You can use classes and data-* parameters |
| [# empty link] | empty link | link withhref="javascript:;"i.e. not leading anywhere. useful when constructing pull-down menus |
| [/category:page/option1/option2 link text] | link text | You can create shorter links to your own site with/parameters without writing whole http link./E.g. you can use/[/blog:post/edit/true edit this post]/instead of/[http://site.wikidot.com/ blog:post/edit/true edit this post] |

Adding underscore to **a** element **[[a_ ]]** will truncate whitespaces around it which prevents creation of random [new lines and paragraphs](/doc-wiki-syntax:paragraphs-and-newline). It's simplifices creation of complex HTML syntax like [Bootstrap components](http://getbootstrap.com/components/)

## Anchors

To place an anchor use `[[# anchor-name]]` syntax. To refer to an anchor (and scroll to it) use `[#anchor-name text to display]`.

## Emails

| what you type | what you get | comments |
| --- | --- | --- |
| support@example.com | moc.elpmaxe\|troppus#moc.elpmaxe\|troppus | simple inline email |
| [support@example.com email me!] | moc.elpmaxe\|troppus#!em liame | custom anchor |

Although we discourage anyone from putting his/her email address on the web, Wikidot engine provides a simple scrambling mechanism to prevent automated bots from reading emails. Each email is scrambled and it is decoded in the client's browser. So it is not 100% spam-safe, but much safer than plain-text emails.

## InterWiki

To link directly to a Wikipedia article you can use a syntax:

| what you type | what you get |
| --- | --- |
| [wikipedia:Albert_Einstein] | Albert_Einstein |
| [wikipedia:Albert_Einstein Albert] | Albert |
| [wikipedia:it:Albert_Einstein Albert] | Albert |

Other links defined by example:

- `[google:free+wiki]` - search google for the "free wiki" term
- `[dictionary:wiki]` - look up definitions of the word *wiki* from dictionary.reference.com

## Magic URIs

Magic URIs (or Magic Links) are the way to control pages within the URL address.

| what you type | what you get | comments |
| --- | --- | --- |
| [http://site-name.wikidot.com/page-name#_editpage Edit] | Edit | Goes to the page with the edit mode already opened |
| [http://site-name.wikidot.com/page-name/title/whatever Edit with title] | Edit with title set | Works only with not existing pages. When you go to edit mode on such page, the title will be set to 'whatever'. May be combined with /edit/true, parentPage/page-name etc. |
| [http://site-name.wikidot.com/page-name/parentPage/parent-page-name Edit with parent page set] | Edit with parent page set | Works only with not existing pages. When you go to edit mode on such page, the parent page will be set to 'page-name'. May be combined with /edit/true, title/whatever etc. |
| [http://site-name.wikidot.com/page-name/noredirect/true Page without redirect] | Page without redirect | Turning off redirection, if theRedirect Moduleis present on the page |
| [http://site-name.wikidot.com/page-name/tags/tag1,tag2 Set tags] | Set tags | Sets tags on the page via URL, comma-delimited |
| [http://site-name.wikidot.com/page-name/norender/true No Render] | No Render | Goes to the page, but does not render it. It allows to change the source of the page when there is a problem with page functionality |

## Hash Magic URIs

`http://site-name.wikidot.com/page-name`**`#_option`**

| what you type | what you get |
| --- | --- |
| #_wantedpages | lists Wanted Pages |
| #_orphanedpages | lists Orphaned Pages |
| #_draftpages | lists Draft Pages on site |
| #_editpage | opens Editor |
| #_edittags | opens Tag Editor |
| #_history | displays History |
| #_files | lists Files attached to the page |
| #_sitetools | opens Site Tools |
