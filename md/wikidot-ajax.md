# Wikidot AJAX 接口逆向文档

基于 Wikidot 开源代码 (gabrys/wikidot) 和实际抓包整理。

## 概述

### 端点

所有 AJAX 请求发送到同一个地址：

```
POST https://{site}.wikidot.com/ajax-module-connector.php
```

### 请求格式

- Content-Type: `application/x-www-form-urlencoded; charset=UTF-8`
- 必须携带 Header: `X-Requested-With: XMLHttpRequest`
- 请求体为 URL 编码的键值对

### 通用参数

| 参数 | 说明 |
|------|------|
| `moduleName` | 要调用的模块路径（查询类请求必填） |
| `action` | 要调用的 Action 名称（写入类请求必填） |
| `event` | Action 下的具体事件名 |
| `wikidot_token7` | CSRF Token，从 cookie 或页面 JS 中获取 |
| `callbackIndex` | 请求序号（递增整数，可选） |

### 响应格式

JSON 对象：

```json
{
    "status": "ok",
    "body": "<html>...</html>",
    "message": "可选的消息",
    "CURRENT_TIMESTAMP": 1234567890
}
```

错误时：

```json
{
    "status": "wrong_token7",
    "message": "错误描述"
}
```

### 认证方式

- **无需登录的公开数据**：`wikidot_token7=123456`（伪造即可）
- **需要登录的操作**：需要真实的 session cookie（`WIKIDOT_SESSION_ID`）+ 对应的 `wikidot_token7`

---

## Modules（只读查询类）

模块请求用 `moduleName` 参数指定，返回的 `body` 字段为 HTML 片段，需要自行解析。

### viewsource/ViewSourceModule

获取页面的 Wikidot 源代码。

```
moduleName=viewsource/ViewSourceModule
page_id={pageId}
wikidot_token7=123456
```

**响应 body 结构**：包含 `.page-source` 元素，内部为原始 wiki 语法。

---

### pagerate/WhoRatedPageModule

获取页面的所有投票记录（谁投了 +1 或 -1）。

```
moduleName=pagerate/WhoRatedPageModule
pageId={pageId}
page_id={pageId}
wikidot_token7=123456
```

**响应 body 结构**：包含 `.printuser` 元素列表，每个用户旁边有 `+` 或 `-` 标记。

---

### pagerate/PageRateModule

获取页面评分组件（当前总分和投票按钮）。

```
moduleName=pagerate/PageRateModule
pageId={pageId}
wikidot_token7=123456
```

---

### history/PageRevisionListModule

获取页面的修订历史列表。

```
moduleName=history/PageRevisionListModule
page_id={pageId}
page={页码，从1开始}
perpage={每页条数，默认20，最大100}
wikidot_token7=123456
options={"all":true}
```

**响应 body 结构**：HTML 表格，每行包含修订号、编辑者（`.printuser`）、时间戳、修改说明。

---

### edit/PageEditModule

获取页面编辑界面（源码 + 编辑锁）。需要登录。

```
moduleName=edit/PageEditModule
page_id={pageId}
mode=page
wikidot_token7={真实token}
```

`mode` 可选值：
- `page` — 编辑整个页面
- `append` — 追加模式
- `section` — 编辑指定段落（需配合 `range_start` / `range_end`）

**响应 body 结构**：包含页面源码、lock_id、lock_secret、revision_id 等隐藏字段。

---

### forum/ForumViewThreadModule

查看论坛帖子内容。

```
moduleName=forum/ForumViewThreadModule
t={threadId}
pageNo={页码}
wikidot_token7=123456
```

---

### forum/ForumStartModule

获取论坛首页（分类列表）。

```
moduleName=forum/ForumStartModule
hidden=true
wikidot_token7=123456
```

---

### forum/ForumViewCategoryModule

查看论坛分类下的帖子列表。

```
moduleName=forum/ForumViewCategoryModule
c={categoryId}
p={页码}
wikidot_token7=123456
```

---

### forum/ForumRecentPostsModule

获取论坛最近发帖。

```
moduleName=forum/ForumRecentPostsModule
limit={数量}
wikidot_token7=123456
```

---

### forum/ForumNewThreadModule

获取发帖表单界面。

```
moduleName=forum/ForumNewThreadModule
c={categoryId}
wikidot_token7={真实token}
```

---

### list/ListPagesModule

Wikidot 最强大的模块，按条件列出页面。

```
moduleName=list/ListPagesModule
category={分类名，如 "_default"}
tags={标签筛选，如 "+scp +safe"}
order={排序，如 "rating desc"}
limit={数量限制}
perPage={每页数量}
separate=no
wikidot_token7=123456
```

常用 `order` 值：
- `created_at desc` — 最新创建
- `rating desc` — 最高评分
- `title` — 按标题排序
- `random` — 随机

---

### search/SearchModule

站内搜索。

```
moduleName=search/SearchModule
query={搜索关键词}
area=site
wikidot_token7=123456
```

---

### userinfo/UserInfoModule

获取用户信息弹窗。

```
moduleName=userinfo/UserInfoModule
user_id={userId}
wikidot_token7=123456
```

**响应 body 结构**：包含用户头像、注册时间、Karma 等级等信息。

---

### files/FileModule (推测模块名)

获取页面附件列表。

```
moduleName=files/FileModule
page_id={pageId}
wikidot_token7=123456
```

---

### membership/MembershipApplyModule

获取站点申请加入表单。

```
moduleName=membership/MembershipApplyModule
wikidot_token7={真实token}
```

---

## Actions（写入操作类）

Action 请求用 `action` + `event` 参数指定。大部分需要登录（真实 session cookie）。

### WikiPageAction

页面相关的所有写入操作。

#### savePage — 保存页面

```
action=WikiPageAction
event=savePage
wiki_page={页面unix名}
page_id={pageId，新页面不填}
title={页面标题}
source={Wikidot源码}
comments={修订说明，最长210字符}
mode=page
lock_id={编辑锁ID}
lock_secret={编辑锁密钥}
revision_id={当前修订ID，用于冲突检测}
wikidot_token7={真实token}
```

`mode` 可选值：
- `page` — 保存整个页面
- `append` — 追加内容到页面末尾
- `section` — 保存指定段落（需 `range_start` / `range_end`）

#### renamePage — 重命名页面

```
action=WikiPageAction
event=renamePage
page_id={pageId}
new_name={新的unix名}
fixdeps={是否修复依赖链接}
wikidot_token7={真实token}
```

#### deletePage — 删除页面（推测）

```
action=WikiPageAction
event=deletePage
page_id={pageId}
wikidot_token7={真实token}
```

#### saveTagsEvent — 设置页面标签（推测）

```
action=WikiPageAction
event=saveTags
pageId={pageId}
tags={空格分隔的标签}
wikidot_token7={真实token}
```

#### setParentPage — 设置父页面（推测）

```
action=WikiPageAction
event=setParentPage
pageId={pageId}
parentName={父页面unix名}
wikidot_token7={真实token}
```

#### removePageEditLock — 释放编辑锁

```
action=WikiPageAction
event=removePageEditLock
lock_id={锁ID}
lock_secret={锁密钥}
wikidot_token7={真实token}
```

---

### ForumAction

论坛相关写入操作。

#### savePost — 发帖/回复

```
action=ForumAction
event=savePost
threadId={帖子ID}
parentId={父帖ID，顶层回复留空}
title={标题，可留空}
source={帖子内容，Wikidot语法}
wikidot_token7={真实token}
```

#### newThread — 创建新帖

```
action=ForumAction
event=newThread
category_id={论坛分类ID}
title={帖子标题}
description={帖子描述}
source={首楼内容}
wikidot_token7={真实token}
```

#### saveEditPost — 编辑已有帖子

```
action=ForumAction
event=saveEditPost
postId={帖子ID}
threadId={所在帖子ID}
title={标题}
source={新内容}
currentRevisionId={当前修订ID}
wikidot_token7={真实token}
```

#### deletePost — 删除帖子

```
action=ForumAction
event=deletePost
postId={帖子ID}
wikidot_token7={真实token}
```

#### moveThread — 移动帖子到其他分类

```
action=ForumAction
event=moveThread
threadId={帖子ID}
categoryId={目标分类ID}
wikidot_token7={真实token}
```

#### saveSticky — 置顶/取消置顶

```
action=ForumAction
event=saveSticky
threadId={帖子ID}
sticky={true/false}
wikidot_token7={真实token}
```

#### saveBlock — 锁定/解锁帖子

```
action=ForumAction
event=saveBlock
threadId={帖子ID}
block={true/false}
wikidot_token7={真实token}
```

#### saveThreadMeta — 修改帖子标题和描述

```
action=ForumAction
event=saveThreadMeta
threadId={帖子ID}
title={新标题}
description={新描述}
wikidot_token7={真实token}
```

#### createPageDiscussionThread — 为页面创建讨论帖

```
action=ForumAction
event=createPageDiscussionThread
page_id={pageId}
wikidot_token7={真实token}
```

---

### RateAction

页面投票操作。

#### ratePage — 投票

```
action=RateAction
event=ratePage
pageId={pageId}
points={1 或 -1}
force={可选，覆盖已有投票}
wikidot_token7={真实token}
```

#### cancelVote — 取消投票

```
action=RateAction
event=cancelVote
pageId={pageId}
wikidot_token7={真实token}
```

---

### FileAction

文件/附件操作。

#### uploadFile — 上传文件

```
action=FileAction
event=uploadFile
page_id={pageId}
（文件通过 multipart/form-data 上传）
wikidot_token7={真实token}
```

#### renameFile — 重命名文件

```
action=FileAction
event=renameFile
page_id={pageId}
file_id={文件ID}
new_name={新文件名}
wikidot_token7={真实token}
```

#### moveFile — 移动文件到其他页面

```
action=FileAction
event=moveFile
file_id={文件ID}
destination_page_id={目标页面ID}
wikidot_token7={真实token}
```

#### deleteFile — 删除文件

```
action=FileAction
event=deleteFile
page_id={pageId}
file_id={文件ID}
wikidot_token7={真实token}
```

---

### PMAction

私信操作。

#### send — 发送私信

```
action=PMAction
event=send
to_user_id={目标用户ID}
subject={主题}
source={内容，Wikidot语法}
wikidot_token7={真实token}
```

#### saveDraft — 保存草稿

```
action=PMAction
event=saveDraft
to_user_id={目标用户ID}
subject={主题}
source={内容}
wikidot_token7={真实token}
```

#### removeSelectedInbox — 批量删除收件箱消息

```
action=PMAction
event=removeSelectedInbox
selected={JSON数组，如 [1,2,3]}
wikidot_token7={真实token}
```

#### removeInboxMessage — 删除单条收件箱消息

```
action=PMAction
event=removeInboxMessage
message_id={消息ID}
wikidot_token7={真实token}
```

---

### MembershipApplyAction

站点成员申请。

#### apply — 提交加入申请

```
action=MembershipApplyAction
event=apply
comment={申请理由}
wikidot_token7={真实token}
```

#### applyByPassword — 通过密码加入

```
action=MembershipApplyAction
event=applyByPassword
password={站点设置的密码}
wikidot_token7={真实token}
```

---

### WatchAction

关注/取消关注。

#### watchPage — 关注页面

```
action=WatchAction
event=watchPage
pageId={pageId}
wikidot_token7={真实token}
```

#### removeWatchedPage — 取消关注页面

```
action=WatchAction
event=removeWatchedPage
pageId={pageId}
wikidot_token7={真实token}
```

#### watchThread — 关注论坛帖子

```
action=WatchAction
event=watchThread
threadId={threadId}
wikidot_token7={真实token}
```

#### removeWatchedThread — 取消关注帖子

```
action=WatchAction
event=removeWatchedThread
threadId={threadId}
wikidot_token7={真实token}
```

---

## 认证流程

### 获取 Session Cookie

登录端点：

```
POST https://www.wikidot.com/default--flow/login__LoginPopupScreen
Content-Type: application/x-www-form-urlencoded

login={用户名或邮箱}
password={密码}
action=Login2Action
event=login
wikidot_token7=123456
```

成功后响应会 Set-Cookie 返回 `WIKIDOT_SESSION_ID`。

### 使用认证

后续请求携带：

```
Cookie: WIKIDOT_SESSION_ID={session值}; wikidot_token7=123456
```

请求体中也要带 `wikidot_token7=123456`。

---

## 获取 page_id

大部分模块需要 `page_id`（数字ID），获取方式：

1. **从页面 HTML 中提取**：页面源码中有 `WIKIREQUEST.info.pageId = 12345;`
2. **从 Wikit API 获取**：通过 GraphQL 查询
3. **从 ListPages 模块获取**：返回的 HTML 中包含 page_id

---

## 注意事项

### 速率限制

- Wikidot 官方 XML-RPC API 限制为 240 请求/分钟
- AJAX 接口没有明确的公开限制，但高频请求会被临时封禁 IP
- 建议控制在 1-2 请求/秒

### 常见错误状态

| status | 含义 |
|--------|------|
| `ok` | 成功 |
| `wrong_token7` | CSRF token 无效 |
| `no_permission` | 无权限 |
| `not_ok` | 通用错误，看 message 字段 |
| `try_again` | 服务器繁忙，稍后重试 |

### 其他已知模块路径（未详细文档化）

```
account/AccountModule
backlinks/BacklinksModule
changes/SiteChangesModule
createsite/CreateSiteModule
login/LoginModule
misc/SiteBlockModule
pageblock/PageBlockModule
pagetags/PageTagsModule
parent/ParentPageModule
rename/RenamePageModule
report/FlagPageModule
simpletodo/SimpleToDoModule
sitetools/SiteToolsModule
users/MembersListModule
wiki/WikiModule
```

---

## 参考来源

- [Wikidot 开源代码 (gabrys/wikidot)](https://github.com/gabrys/wikidot) — PHP 源码，包含所有模块和 Action 的实现
- [SCPython 文档](https://scpython.readthedocs.io/en/latest/_modules/scpython/client.html) — Python 客户端实现参考
- [pyscp](https://github.com/anqxyr/pyscp) — SCP Wiki 的 Python 工具库
- [SCP Sandbox Wiki - bluesoul](http://scpsandboxwiki.wikidot.com/bluesoul) — 社区整理的接口说明
