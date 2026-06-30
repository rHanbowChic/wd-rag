# Join Module

> Documentation > Modules > Join Module

The `Join` module provides an action button that has the same functionality as the "Join this site" action on the top toolbar shown on free sites. When a user clicks the button, the Join module first ensures that the user has an account (and asks anonymous users to create an account) and then attempts to make the user a member of the site.

The Join module has these arguments:

- **button="text string"** — specifies the text for the button, which is "Join this site" by default.
- **class="css-class"** — specifies CSS class for the `div` element containing the button, allowing custom styling

The precise behavior of the Join module depends on the access policy of the site:

- On open sites, the user becomes a member instantly.
- On closed and private sites, the user must provide a password or apply to join the site, depending on the access policy configuration.

---

**Note:**

When you create the join module on your site you will not see the join button when you save the page, and you might think it hasn't worked. The button doesn't display because you are already a member of your site and the module does not display the button for those that are already a member of your site. This is because they don't need to join the site again.

There are two ways to check to see how the button looks when non-members visit your site:

- You can edit the page containing [[module Join]] and then *preview* the page.
- You can sign out of your site. After the page refreshes, you will then see the button. You can then sign in again to carry on working on your site (and you won't see the button).

---

Here is the simplest example of use:

```
[[module Join]]
```

Here is an example that specifies the button text:

```
[[module Join button="Join this site, it is cool!"]]
```

Join button with custom styling:

```
[[module Join class="my-join-button"]]
```

If you use custom styling, remember to define the class in your custom CSS. The default class for the join box is ".join-box" and you can style this using custom CSS like this:

```

.join-box {
    background-image: url(yourimage.png)
}
```
