# Embedding

> Documentation > Embedding

You can safely embed any external HTML code on your pages. To guarantee maximum safety, HTML code is placed in a safe environment (iframe sandbox) to limit the possibility of cross-site scripting attacks.

E.g. to display del.icio.us tag cloud as generated from [http://del.icio.us/help/tagrolls](http://del.icio.us/help/tagrolls) simply wrap the html code in a [[html]]…[[/html]] tags:

```
[[html]]
<script type="text/javascript" src="http://del.icio.us/feeds/js/tags/michal_frackowiak?icon;size=12-35;color=87ceeb-0000ff;title=my%20del.icio.us%20tags"></script>
[[/html]]
```

Note: previously [[html]] tag functionality was partly covered by the [[embed]] tag, which is now deprecated and aliased to [[html]]. This is why you might still find [[embed]] tag here and there.

# Examples of supported media using [[html]] tags:

## Video & Audio

![favicon.ico](http://youtube.com/favicon.ico) [YouTube video](http://www.youtube.com)

![favicon.ico](http://www.google.com/favicon.ico) [Google Video](http://www.video.google.com)

![favicon.ico](http://vimeo.com/favicon.ico) [Vimeo](http://www.vimeo.com/) videos (HD) - [more»](http://snippets.wikidot.com/code:vimeo)

![favicon.ico](http://www.dailymotion.pl/favicon.ico) [DailyMotion](http://dailymotion.com) videos - [more»](http://snippets.wikidot.com/code:dailymotion)

![favicon.ico](http://www.gametrailers.com/favicon.ico) [GameTrailers Video (HD)](http://www.gametrailers.com) - [more»](http://snippets.wikidot.com/code:gametrailers).

![favicon.ico](http://animoto.com/favicon.ico) [Animoto](http://www.animoto.com)

![favicon.ico](http://flickr.com/favicon.ico) [Flickr](http://flickr.com) videos - [more»](http://snippets.wikidot.com/code:flickr-video)

![favicon.ico](http://www.teachertube.com/favicon.ico) [TeacherTube](http://www.teachertube.com) videos - [more»](http://snippets.wikidot.com/code:teachertube)

![favicon.ico](http://www.schooltube.com/favicon.ico) [SchoolTube](http://www.shooltube.com) videos - [more»](http://snippets.wikidot.com/code:schooltube)

![favicon.ico](http://blip.tv/favicon.ico) [Blip.tv](http://blip.tv) videos (HD) - [more»](http://snippets.wikidot.com/code:bliptv)

![favicon.ico](http://www.playlist.com/favicon.ico) [Playlist.com](http://www.playlist.com) music player - [more»](http://snippets.wikidot.com/code:playlist)

![favicon.ico](http://finetune.com/favicon.ico) [FineTune player](http://www.finetune.com/)

## Images

![favicon.ico](http://photobucket.com/favicon.ico) [Photobucket](http://www.photobucket.com) photo widgets - [more»](http://snippets.wikidot.com/code:photobucket-widget)

![favicon.ico](http://picasaweb.google.com/favicon.ico) [Picasa](http://picasaweb.google.pl/home) web albums - [more»](http://snippets.wikidot.com/code:picasaweb)

## Office Tools

![favicon.ico](http://writer.zoho.com/images/favicon.ico) [Zoho Polls](http://zohopolls.com/) - [more»](http://snippets.wikidot.com/code:zohopolls)

![favicon.ico](http://writer.zoho.com/images/favicon.ico) [Zoho Writer](http://zohowriter.com) - [more»](http://snippets.wikidot.com/code:zohowriter)

![favicon.ico](http://writer.zoho.com/images/favicon.ico) [Zoho Show](http://zohoshow.com) - [more»](http://snippets.wikidot.com/code:zohoshow)

![favicon.ico](http://writer.zoho.com/images/favicon.ico) [Zoho Sheet](http://www.zohosheet.com/) - [more»](http://snippets.wikidot.com/code:zohosheet)

![favicon.ico](http://www.editgrid.com/favicon.ico) [EditGrid](http://www.editgrid.com) - [more»](http://snippets.wikidot.com/code:editgrid)

![favicon.ico](http://instacalc.com/favicon.ico) [Instacalc](http://instacalc.com/) - [more»](http://snippets.wikidot.com/code:instacalc)

![favicon.ico](http://quimble.com/favicon.ico) [Quimble](http://quimble.com) polls - [more»](http://snippets.wikidot.com/code:quimble-poll)

## Slideshows & Presentations

![favicon.ico](http://voicethread.com/favicon.ico) [Voicethread](http://voicethread.com/) slideshows - [more»](http://snippets.wikidot.com/code:voicethread)

![favicon.ico](http://www.slideboom.com/images/favicon.ico) [SlideBoom](http://www.slideboom.com/) slideshows and presentations - [more »](http://snippets.wikidot.com/code:slideboom)

## Maps

![favicon.ico](http://www.google.com/favicon.ico) [Google Maps](http://maps.google.com) - [more»](http://snippets.wikidot.com/code:google-maps)

![favicon.ico](http://wikimapia.org/favicon.ico) [Wikimapia](http://wikimapia.org)

![favicon.ico](http://quikmaps.com/favicon.ico) [Quikmaps maps](http://quikmaps.com) - [more»](http://snippets.wikidot.com/code:quikmaps-maps)

![favicon.ico](http://www.everytrail.com/favicon.ico) [EveryTrail](http://everytrail.com/)

![favicon.ico](http://motionbased.com/favicon.ico) [MotionBased](http://motionbased.com)

## Social services

![favicon.ico](http://disqus.com/favicon.ico) **NEW!** [Disqus](http://disqus.com)

![favicon.ico](http://tweetmeme.com//images/favicon.ico) [TweetMeme](http://tweetmeme.com/)

![favicon.ico](http://addthis.com/favicon.ico) [AddThis](http://addthis.com)

![favicon.ico](http://delicious.com/favicon.ico) [del.icio.us tagrolls](http://del.icio.us/help/tagrolls)

![favicon.ico](http://delicious.com/favicon.ico) [del.icio.us linkrolls](http://del.icio.us/help/linkrolls)

![favicon.ico](http://delicious.com/favicon.ico) [del.icio.us tagometer](http://del.icio.us/help/tagometer)

![favicon.ico](http://delicious.com/favicon.ico) [del.icio.us "Save this page"](http://del.icio.us/help/forpublishers) - [more»](http://snippets.wikidot.com/code:social-bookmarking)

![favicon.ico](http://digg.com/favicon.ico) [Digg news](http://www.digg.com/add-digg) - [more»](http://snippets.wikidot.com/code:import-the-digg-feed)

![spreadfirefox_RCS_favicon.png](http://www.spreadfirefox.com/files/spreadfirefox_RCS_favicon.png) [spreadfirefox.com](http://www.spreadfirefox.com/?q=affiliates/homepage) affiliate buttons

![favicon.ico](http://www.ohloh.net/favicon.ico) [Ohloh](http://ohloh.net) snippets - [more»](http://snippets.wikidot.com/code:ohloh)

![favicon.ico](http://www.meebo.com/favicon.ico) [Meebo Me](http://www.meebome.com) IM chat window - [more»](http://snippets.wikidot.com/code:meebome)

![favicon.ico](http://home.gabbly.com/images/favicon.ico) [Gabbly](http://gabbly.com/) multi-user chat - [more»](http://snippets.wikidot.com/code:gabbly)

![favicon.png](http://www.wowdb.com/favicon.png) [WOWDB](http://www.wowdb.com/), [Wowhead](http://www.wowhead.com/), [Thottbot](http://thottbot.com/) tooltips - [more»](http://snippets.wikidot.com/code:wow-tooltips)

![favicon.ico](http://www.mybloglog.com/favicon.ico) [MyBlogLog](http://mybloglog.com) widget - [more»](http://snippets.wikidot.com/code:mybloglog)

## Widgets

![favicon.ico](http://www.google.com/favicon.ico) **[Google Gadgets](http://www.google.com/ig/directory?synd=open)** - [more»](http://snippets.wikidot.com/code:google-gadgets)

![favicon.ico](http://www.google.com/favicon.ico) [Google Calendar](http://www.google.com/calendar) - [more»](http://www.google.com/support/calendar/bin/answer.py?answer=41207)

![favicon.ico](http://www.widgetbox.com/favicon.ico) [Widgetbox](http://www.widgetbox.com) Widgets - [more»](http://snippets.wikidot.com/code:widgetbox-panel)

![favicon.ico](http://js-kit.com/favicon.ico) [JS-Kit ratings](http://js-kit.com/ratings/) - [more»](http://snippets.wikidot.com/code:js-kit-ratings)

![favicon.ico](http://www.labpixies.com/favicon.ico) [Labpixies](http://www.labpixies.com/) gadgets - [more»](http://snippets.wikidot.com/code:pabpixies-gadgets)

## Web Tools

![favicon.ico](http://www.statcounter.com/favicon.ico) [StatCounter](http://www.statcounter.com/) tracking code - [more»](http://community.wikidot.com/howto:site-statistics)

![favicon.ico](http://www.alexa.com/favicon.ico) [Alexa.com](http://www.alexa.com) traffic ratings - [more»](http://snippets.wikidot.com/code:alexa-traffic-ratings)

![favicon.ico](http://www.feedburner.com/fb/images/favicon.ico) [Feedburner](http://www.feedburner.com) - [more»](http://snippets.wikidot.com/code:feedburner)

![favicon.ico](http://feedblitz.com/favicon.ico) [FeedBlitz](http://www.feedblitz.com/)

![favicon.ico](http://babelfish.yahoo.com/favicon.ico) [Babelfish translation](http://babelfish.yahoo.com/free_trans_service) - [more»](http://snippets.wikidot.com/code:babelfish-translation)

![favicon.ico](http://skype.com/favicon.ico) [Skype](http://www.skype.com/share/buttons/index.html) - "call me" buttons

![favicon.ico](http://www.brainyquote.com/favicon.ico) [Brainy Quote](http://www.brainyquote.com/link/index.html) - quote of the day

![favicon.ico](http://cornify.com/favicon.ico)[Cornify](http://www.cornify.com) - don't even ask :) [more»](http://snippets.wikidot.com/code:cornify)

If you want a new service enabled, please write to support@wikidot.com or put your suggestion in our [Community Forum](http://community.wikidot.com/forum/c-11/new-features-and-ideas).
