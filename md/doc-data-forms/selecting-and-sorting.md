# Selecting & Sorting by Data Form fields

> Documentation > Data Forms > Selecting & Sorting by Data Form fields

Using the ListPages module you can select data from a field in the data form and you can also sort by the values within a data form field.

### Selecting

Add a field to your data form or use an existing. With our band example we have added a field to note whether the band will visit Scotland on their next tour:

```
 scotland:
  label: Next tour will visit Scotland
  type: select
  values:
     info: No Info
     visit: "Yes"
     novisit: "No"
```

To list those where the value is "Yes" use a ListPages module and add a new parameter starting with an underscore then the fieldname, in this case *_scotland* followed by an = sign and the property of the field you want: *_scotland="visit"*

```
[[module ListPages category="band"  _scotland="visit" perPage="10" order="name"  separate="false" prependLine="||~ Band||~ Type ||" appendLine="||||||~ ||"]]
|| %%title_linked%% || %%form_data{type}%% ||
[[/module]]
```

That produces a list of just 2 bands:

![df_scotland.png](https://www.wdfiles.com/local--files/doc-data-forms:selecting-and-sorting/df_scotland.png)
You can combine several data form selection fields to narrow down your search. For example if we wanted to just select folk bands that will tour Scotland we would use the *_scotland="visit"* selection criteria and the *_type="2"* selection criteria (because type is the data form feld for the music type, and 2 is the property of the folk value).

```
 type:
   label: Music type
   type: select
   values:
     0: Classical
     1: Country
     2: Folk
     3: Indie
     4: Jazz
     5: Pop
     6: Rock
   default: 6
```

Combining different selection criteria uses the AND operator, so the result must match both of these criteria. The resulting ListPages code would look like this:

```
[[module ListPages category="band"  _scotland="visit" _type="2" perPage="10" order="name"  separate="false" prependLine="||~ Band||~ Type ||" appendLine="||||||~ ||"]]
|| %%title_linked%% || %%form_data{type}%% ||
[[/module]]
```

and the table that is produced is:

![df_filter.png](https://www.wdfiles.com/local--files/doc-data-forms:selecting-and-sorting/df_filter.png)
You can search for pages where a particular field is empty by using **_field=""**

### Sorting

You can also sort by data form field properties. In our band example we have created a field to store the number of albums/CDs released by the band:

```
 albums:
    label: Albums/CDs released
    type: select
    values:
      "00": 0
      "01": 1
      "02": 2
      "03": 3
      "04": 4
      "05": 5
      "06": 6
      "07": 7
      "08": 8
      "09": 9
..
```

To sort the number of albums into descending order, use a Listpages module with the *order=*parameter followed by an underscore then the name of the field then the *desc* attribute: order="_albums desc"

```
[[module ListPages category="band"  perPage="10" order="_albums desc" separate="false" prependLine="||~ Band||~ Albums ||" appendLine="||||||~ ||"]]
|| %%title_linked%% || %%form_data{albums}%% ||
[[/module]]
```

In order for the sort to work correctly, numbers below 10 must have a property of 01, 02, 03 etc. although the value can still be 1, 2, 3 etc as in the example data form field above. It is the value that is displayed in the ListPages module, as shown below. As (01, 02, 03, …) are treated as octal numbers you need to enclose them by semicolons ("01", "02", "03", …) because there is no 08 and 09 in octal and they both will be 0.

![df_albums.png](https://www.wdfiles.com/local--files/doc-data-forms:selecting-and-sorting/df_albums.png)
