# Date

> Documentation > Wiki Syntax > Date

In several places (forum, private messages, last revision date, etc.) Wikidot pages use dates and timestamps that automatically calculate (either when hovering with the mouse or directly in the text) how long ago this was. Examples are

- 15 Mar 2009 16:44 (move the mouse over the date to see the hovering text) or,
- 15 Mar 2009 16:44

If you want dates that *you* type on your pages to also automatically show "how long ago'', here is how you can do it.

## How it works

The syntax needed is:

> `[[date *timestamp* <format="*format*<|agohover>">]]`

where

- < … > denote optional parameters
- `*timestamp*` is the number of seconds between Jan 1, 1970 and the wanted date. To find this number for a specific date, see [Code Wizard](#wizard) below.
- `*format*` is an arbitrary text string that may include *[%modifiers](http://community.wikidot.com/howto:frontforum-date-variable#modifiers)*, which are replaced by an actual (part of the) date or time. If not specified, `*format*` defaults to "%e''.
- `|agohover` when specified displays a "hovering'' text ("*nn* seconds/minutes/hours/days ago") when the mouse is moved over any part of the displayed `*format*` string.

## Code Wizard

To find out what code you should use on your page for a specific date:

Then copy/paste the displayed code into your page.

## Examples

| What you type … | What you get … |
| --- | --- |
| [[date 1216153821]] | 15 Jul 2008 20:30 |
| [[date 1216153821 format="%d. %m. %Y\|agohover"]] | 15 Jul 2008 20:30 |
| [[date 681746400 format="James is %O young"]] | 09 Aug 1991 14:00 |
| +++ Minutes from [[date 1234567890 format="%e %B\|agohover"]] | Minutes from13 Feb 2009 23:31 |

Note: You can use %O also with the future dates as well.

**Author**

created by [![ErichSteinboeck](https://www.wikidot.com/avatar.php?userid=7925&amp;size=small&amp;timestamp=1401117862)](http://www.wikidot.com/user:info/erichsteinboeck)[ErichSteinboeck](http://www.wikidot.com/user:info/erichsteinboeck)
