# Using the data in ListPages modules

> Documentation > Data Forms > Using the data in ListPages modules

The data that is produced by data forms can be used in the ListPages module ([http://www.wikidot.com/doc:listpages-module](http://www.wikidot.com/doc:listpages-module)). With the band example, a ListPages module could look like this:

```
[[module ListPages category="band" order="name"  separate="false" prependLine="||~ Band||~ Type ||~ Current ||" appendLine="||||||||~ ||"]]
|| %%title_linked%% || %%form_data{type}%% || %%form_data{current}%% ||
[[/module]]
```

![df_bandlist.jpg](https://www.wdfiles.com/local--files/doc-data-forms:dataforms-and-listpages/df_bandlist.jpg)
