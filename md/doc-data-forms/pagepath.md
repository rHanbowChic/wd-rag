# The Pagepath concept

> Documentation > Data Forms > The Pagepath concept

Wikidot data forms have a unique concept, the Page Tree and pagepath, which is a way of organizing data. It creates a page in a specific category for each pagepath entry you enter. Using our band example you could set the *origin* of the band. Band origins form a tree:

- _root
  - USA
    - Chicago
    - Los Angeles
  - Australia
    - Melbourne
    - Sydney
  - Europe
    - UK
      - London
        - - North-London
          - South-London
            - Dulwich
          - East-London
          - West-London
      - Newcastle
      - Glasgow
    - Germany
    - Sweden

Each part of the tree is a wiki page. Imagine this tree is held in a category called **band-origin**. Now we can use parent links to attach Dulwich to South-London to London to UK to Europe, and Chicago to USA etc.

The Wikidot data form system makes it easy to navigate, and edit such a tree. You define a 'pagepath' field and tell it to use the **band-origin:** category, as shown in part of a dataform below:

```
 origin:
   label: Origin
   type: pagepath
   category: band-origin
```

A page tree is always anchored to a page called _root that Wikidot creates automatically when you start using a page tree in forms.

When you and your users are entering data into the dataform, for the pagepath field they will initially see a single dropdown box. If there is already a value in the box they can select it or click on the create new entry in the dropdown and enter the value you want.

![df_pagepath.png](https://www.wdfiles.com/local--files/doc-data-forms:pagepath/df_pagepath.png)
**After entering the value you must press Enter.** That will then add the value you have selected or entered and open the next box. There is no limit to the number of these boxes (and the pages they create) that you can have. However, you can use the **max-level** property to set the maximum number of levels that can be created in the pagepath tree.

```
 origin:
   label: Origin
   type: pagepath
   category: band-origin
   max-level: 4
```

In the layout of your page, above the ==== selector, you use %%form_data{origin}%% and the lowest value in the pagepath list of values will be displayed. So if you have Europe->UK->London, London will be displayed.

The pages that the pagepath creates can list each of the bands who have that value. To do this, create a live template page containing [[module Backlinks]].

A site dedicated to examples of the pagepath concept is at [http://pagepath.wikidot.com/](http://pagepath.wikidot.com/)
