# Searching

> Documentation > Searching

## Basic searching

Every site header shows a search form that lets you find pages in that site. In the search form, type the words you want to search for and press Enter.

- Pages are ranked on how many search terms they match, so to refine your search results, add more words.
- To show *only* pages that contain *elephant*, search for **+elephant**.
- To show pages that have *elephant* in the title, search for **title:elephant**.
- To show pages that have the phrase *grey elephants* in the title, search for **title:"grey elephants"** using double quotes.
- To show pages that contain any word starting with *ele*, search for **ele***.
- To show pages that contain any word starting with *ele* and ending in *ant*, search for **ele*ant**.

## Additional filters

- To restrict the search to category "abc", add the filter **category:abc**.
- To restrict the search to categories "abc" and "def", add the filter **category:abc,def**.
- To restrict the search by date, add either or both of: **since:yyyy-mm-dd** and **till:yyyy-mm-dd**.
- To restrict the search to a specific author, add **user:author-name**, using '-' or '_' instead of spaces in the user name.

## Global searching

You can search all of Wikidot, including private sites that you are allowed to read, at [http://www.wikidot.com/search:all](http://www.wikidot.com/search:all). Global search works like basic searching, with these additional options:

- To show pages in the site elephants.wikidot.com, search for **site:elephants**.
- To show pages in several specific sites, list these with commas after the **site:** keyword.

## Searching on tags

*Note: searching on tags is currently not enabled for performance reasons. When we've solved those, we'll enable tag searching.*

In basic and global searches you can additionally search for pages that have specific tags:

- To show pages that contain the tags "big" and "noisy", search for **tags:big,noisy**.
