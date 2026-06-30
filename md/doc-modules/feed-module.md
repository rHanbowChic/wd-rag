# Feed Module

> Documentation > Modules > Feed Module

## Description

The *Feed* module can import RSS or Atom feeds from (almost) any web location and display them in a customizable way. It can also combine feeds from multiple sources.

## Attributes

| attribute | required | allowed values | default | description |
| --- | --- | --- | --- | --- |
| src | yes | single URL address or semicolon-separated list of URL addresses | none | points to the location of source RSS or Atom feed(s) |
| limit | no | any reasonable number | none | limits the number of news items |
| offset | no | any reasonable number | 0 | which item number to start from |

## Display format

If no format is specified all the news items are displayed using the default format. To specify a custom format one should use module invocation:

```
[[module Feed src="somesource"]]
<custom format>
[[/module]]
```

where the inner `<custom format>` element is any block of text following the wiki-syntax, where special variables can be used:

| variable | aliases | description |
| --- | --- | --- |
| %%title%% |  | title of the news item |
| %%linked_title%% | %%title_linked%% | title of the news item linking to the original web page |
| %%channel_title%% |  | title of the news channel (useful when combining multiple feed sources) |
| %%linked_channel_title%% | %%channel_title_linked%% | title of the channel linking to the feed source page |
| %%link%% |  | URL address to the original news item |
| %%description%% | %%short%%,%%summary%% | short summary of the item |
| %%content%% | %%long%%,%%body%% | full content of the item (only when available; falls back todescriptionif not) |
| %%date%% |  | date of the item publication |
| %%date\|format%% |  | prints date with a custom format. Most tokens from php'sstrftimeare accepted. You may find thehowtocontributed by community useful. |
| %%custom%% |  | gives access to any field in the feed (see below) |

The default format is:

```
++ %%linked_title%%

%%date%%

%%description%%
```

## How to use %%custom%%

To access any field in the feed environment, use

```
%%custom <pointer>%%
```

where pointer is a path to the requested element. It is easier to learn this by example:

Look at fragment of an item from [Digg](http://www.digg.com):

```

<item>
    <title>UFO gathering draws believers and belittlers</title>
    <link>
        http://digg.com/space/UFO_gathering_draws_believers_and_belittlers
    </link>
    <description>
        The 37th annual Mutual UFO Network symposium is being held this weekend in Denver,
        attracting throngs of believers and the downright curious — as well as upright skeptics
        and debunkers.
    </description>
    <pubDate>Sat, 15 Jul 2006 15:32:45 GMT</pubDate>
    <guid isPermaLink="true">
        http://digg.com/space/UFO_gathering_draws_believers_and_belittlers
    </guid>
    <digg:diggCount>72</digg:diggCount>
    <digg:submitter>
        <digg:username>capn_caveman</digg:username>
        <digg:userimage>http://digg.com/userimages/capn_caveman/medium.jpg</digg:userimage>
    </digg:submitter>
    <digg:category>Space</digg:category>
    <digg:commentCount>13</digg:commentCount>
</item>
```

To access the `<digg:diggCount>` and display it use:

```
digg counts: %%custom digg:diggCount%%
```

To access a nested element `<digg:username>` use:

```
submitted by %%custom digg:submitter/digg:username%%
```

Now to access any element starting from the root feed element: look at the fragment of the digg feed code again:

```

<rss version="2.0">
    <channel>
        <title>digg</title>
        <language>en-us</language>
        <link>http://digg.com/</link>
        <description>digg</description>
        ...
```

To access the channel tittle element use:

```
%%custom feed/channel/title%%
```

It is important to start with the `feed` word. Ater that the full path to the element follows.
You can also use `%%custom%%` inside `[[image ...]]` and some other places. In some cases however a space character must be replaced with an underscore not to confuse the parser, e.g. to display user submitter image from the digg feed you can use:

```
[[image %%custom_digg:submitter_userimage%%]]
```

## Examples

### CombineSlashdotandDigg technologyfeeds

URL for the feeds are:

- [http://rss.slashdot.org/Slashdot/slashdot](http://rss.slashdot.org/Slashdot/slashdot)
- [http://digg.com/rss/containertechnology.xml](http://digg.com/rss/containertechnology.xml)

Simply do:

```
[[module Feed src="http://rss.slashdot.org/Slashdot/slashdot;http://digg.com/rss/containertechnology.xml"]]
```

More advanced example:

```
[[module Feed src="http://rss.slashdot.org/Slashdot/slashdot;http://digg.com/rss/containertechnology.xml" limit="20"]]
++ %%linked_title%% (%%linked_channel_title%%)

%%date%%, submitted by %%custom digg:submitter_username%% %%custom dc:creator%%

%%description%%
[[/module]]

[[module Feed src="http://rss.slashdot.org/Slashdot/slashdot;http://digg.com/rss/containertechnology.xml" offset="20" limit="20"]]
**%%linked_title%%** (%%linked_channel_title%%, %%date%% by %%custom digg:submitter_username%% %%custom dc:creator%%)
[[/module]]
```

which displays first 20 items in detail and next 20 items just printing the title, channel title, date and submitter.

BTW: a very nice digg feed import is presented at our [snippets code repository here](http://snippets.wikidot.com/code:import-the-digg-feed).
