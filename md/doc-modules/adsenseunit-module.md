# AdSenseUnit Module

> Documentation > Modules > AdSenseUnit Module

> This module was **deprecated** when Wikidot's AdSense integration was removed on 6 April 2010, in favour of a more flexible system.
>
>
> Paying users are now able to use a much larger variety of advertisement providers - and are no longer limited to just Google AdSense.
>
>
> You can read the [official announcement](http://blog.wikidot.com/blog:advertising) if you'd like to know more.

The AdSenseUnit module lets you insert Google AdSense ads into a wiki page. You must have enabled AdSense on your wiki for this module to work. Normally, Wikidot will provide the code for you and you do not need to create your own code to use the AdSenseUnit module.

The syntax for the AdSenseUnit module is:

```
[[module AdSenseUnit arguments...]]
```

## Example

This example shows two left-aligned blocks of adverts:

```
[[div style="margin-left:auto; margin-right:auto; padding: 10px; margin:0 0em 1em 2em; text-align: center; background-color: transparent; float:left; border: none; width: 15%;"]]
[[module AdSenseUnit label="your add"]]
[[module AdSenseUnit label="your add"]]
[[/div]]
```

## Arguments

The **label** argument specifies the label to show, and is mandatory.
