# Private Sites FAQ

> Documentation > Private Sites FAQ

These questions are related to private sites.

### What does it meen that the site is private (non-public)?

It means that only selected Wikidot.com users (of your choice) are able to see it and browse it. You can choose the site to be private either when creating the site or later in your *Site Manager* » *Public or Private* settings.

### So who can view a private site?

There are 2 classes of users that have "view permission":

- site members (invite them or allow them to apply for membership)
- "extra access" users you can define in *Site Manager* » *Public or Private*

"extra access" users will be able to view all the content from your site but will act as "Wikidot.com users" when it comes to site modifying permissions (*SiteManager* » *Permissions*).

In other words — people that are not your site members and you did not give them "extra access" will not be able to browse your site but instead will see the default landing page.

### What can I use the private site for?

For whatever you want provided you comply with our Terms. People use it for personal notepads or workspaces, teachers use it for their classes, some people use it for online collaboration…

I myself ([michal frackowiak](http://www.wikidot.com/user:info/michal-frackowiak)) am using a private site to take notes online, store ideas, keep my "todo" lists, prepare things for my students…

Just think what you need a private space for ;-)

### How many users (members) are allowed for a private Wiki?

At the moment free private Wikis have a limit of **5 members** + 5 extra access permissions. To increase the limit, please upgrade your Account. For more information please refer to the [Plans](http://www.wikidot.com/plans) or [Upgrade's FAQ](http://www.wikidot.com/faq:upgrades).

### Is this really secure?

Yes, the system has been carefully designed and data from your private site should not leak unless someone can steal your password and/or access Wikidot.com as someone who has sufficient permissions.

The system is much better with the SSL encryption. It's available for Pro+ Accounts.

### Although I have specified the default landing page for unauthorized users there are still top- and side-bar menus there that reveal some of my content!

Indeed and this might be a problem when you want to keep your nav:top and nav:side secret. Here is what to do:

- create a landing page within a new category, e.g. `unauthorized:start`
- go to the Site Manager » Appearance » Navigation element
- clear navigational elements for category *unauthorized*.
- go to Site Manager » Public of private and set `unauthorized:start` as a landing page.

Update: now there is an option to disable the nav elements in your Site Manager » Public or Private. However the method described above is visually better (often).

### How do I access RSS feeds from private sites?

All the RSS feeds from private sites are password-protected and only members of the given site are allowed to access them. The authentication mechanism is HTTP Basic Authentication — supported by most of the feed readers.

However due to security reasons the password for accessing the feed is **not the same as your log-in password**. As a user name you should still put your email address but for the password please use the same password you are using for your private feed: please go to [Settings in My Account](http://www.wikidot.com/account:you/start/settings) and click on Notifications to find out the password.
