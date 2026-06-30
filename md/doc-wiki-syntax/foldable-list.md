# Foldable List

> Documentation > Wiki Syntax > Foldable List

The [Foldable List](http://snippets.wikidot.com/code:foldable-list) container is a special class that can be used in a [[div]]. It is useful for creating a navigation menu that folds and unfolds to expose different levels of a list. The following example shows how you can create 3 levels of nesting.

```
[[div class="foldable-list-container"]]
* Links
 * Wikidot
  * [*http://www.wikidot.com/doc Documentation]
  * [*http://www.wikidot.com/doc:wiki-syntax wiki-syntax]
  * [*http://community.wikidot.com/howto:howto-list How-To's]
 * Search Engines
  * [*http://www.google.com Google]
  * [*http://www.yahoo.com Yahoo]
* Main Category 1
 * [# Main 1 - Sub 1]
 * [# Main 1 - Sub 2]
* Main Category 2
 * [# Main 2 - Sub 1]
 * [# Main 2 - Sub 2]
 * [# Main 2 - Sub 3]
* Main Category 3
 * [# Main 3 - Sub 1]
[[/div]]
```

**Update note:**

- it can be used anywhere (no longer associated with `side bar`)
