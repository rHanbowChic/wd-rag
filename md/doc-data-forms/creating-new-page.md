# Creating a new page

> Documentation > Data Forms > Creating a new page

You can create a new page in your data form category in three ways:

1) in your browser address bar, enter the category and pagename after the sitename, for example http://yoursite.wikidot.com/**band:genesis**. Then press Enter.

2) create a [NewPage module](http://www.wikidot.com/doc:newpage-module) button. This method allows you to set the category, parent page, any tags you want when the page is saved and the text of the button. for example:

```
Enter the name of the band and press the button:
[[module NewPage size="30" category="band" parent="bands" tags="rock" button="Add a new rock band"]]
```

3) use the NewPage Button at [http://snippets.wikidot.com/code:newpage-button](http://snippets.wikidot.com/code:newpage-button) which is an excellent snippet created by [![James Kanjo](https://www.wikidot.com/avatar.php?userid=35113&amp;size=small&amp;timestamp=1398764048)](http://www.wikidot.com/user:info/james-kanjo)[James Kanjo](http://www.wikidot.com/user:info/james-kanjo). Using our band example, if you use this you will need to change the name of the band when you edit the form from *Band* to the actual name of the band.

[[include :snippets:newpage-button

|size=30

|category=band

|name=band

|parent=bands

|tags=rock

|button=Add a new band

]]
