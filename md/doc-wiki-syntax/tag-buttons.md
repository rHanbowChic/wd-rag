# Button for tag update

> Documentation > Wiki Syntax > Button for tag update

You can use `[[button set-tags <tag_alterations> text="<button_text>"]]` to change page tags easily.

<tag_alterations> is one or more of the following (separated by space):

- `+tag` — will add a tag to the page if not already present
- `-tag` — will remove a tag from the page if present
- `-*` — will remove all the visible tags from the page (those not starting from "_")
- `-_*` — will remove all the hidden tags from the page (those starting from "_")

The action will happen when user clicks on the button and has permissions to edit the page. The page will reload afterwards (this is useful if you have some iftags constructions on the page).

Any tag removal will happen before tag addition.

Examples:

| code | creates button that … when clicked |
| --- | --- |
| [[button set-tags +tag1 -tag2 text="Change tags"]] | adds tagtag1and removes tagtag2 |
| [[button set-tags +favorite +_book -_movie text="Change tags"]] | add tagsfavoriteand_bookand removes tag_movie |
| [[button set-tags +favorite -* text="Change tags"]] | add tagsfavoriteand removes other visible tags (tags starting with "_" are kept) |
| [[button set-tags -* -_* text="Change tags"]] | clears all the tags |
| [[button set-tags -* +favorite +_book text="Change tags"]] | adds tag favorite, removes other visible tags and adds tag _book keeping all tags starting with "_" |

Class and style attributes work like for standalone buttons for page actions.
