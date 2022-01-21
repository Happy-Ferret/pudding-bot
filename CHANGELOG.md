# Change Log

All notable changes to [@PuddingBot](https://t.me/puddingbot) will be documented in this file.

## [0.0.6-**a5b15fb**] - 2022-01-21

### Added
* Display intro text when @PuddingBot is added to a group.
* Command list specific to @PuddingBot DMs and for group owners.

### Changed
* Improved admin command list.

### Fixed
* [CVE-2022-21669](https://nvd.nist.gov/vuln/detail/CVE-2022-21669)

## [0.0.6-**b933652**] - 2022-01-04

#### Fixed
* /admins displays `@none` when admin has no username.
   - Use usermention instead.

## [0.0.6-**bf84218**] - 2022-01-04

#### Added
* /sticker display sticker ID and stickerset on reply.

## [0.0.5-**b52d58f**] - 2022-01-04

#### Added
* /del delete message on reply.

#### Fixed
* /id
    > This feature is not implemented, yet

thrown when replying to a message.


## [0.0.5-**e87c7d0**] - 2021-12-29

#### Initial release
* Starting at 0.0.5, because why not? 😺
* Initial build with the following feature set:
    - /id on reply.
    - /mute indefinitely on reply.
    - /ban indefinitely on reply.
    - /unmute on reply.
    - /unban on reply.
    - /dog post random dog photo.
    - /cat post random cat photo.
    - /chat display group chat information.
    - /about display information about this bot.
    - /uptime display current bot uptime.
    - /pin pin a message.
    - /perms display group chat user permissions.
    - /admins return list of group chat admins.

    - When @PuddingBot is shut down for
       maintenance or due to an error,
       post a message to a designated
       channel.

    #### Known Bugs:

    - /unban kicks a user when used on non-banned user already in group.
    - /pin is admin-only, currently.
       Not technically a bug.
       Just an oversight.
    - Bot doesn't yet check whether a user is
       already muted/unmuted/banned, so
       running the command repeatedly
       will always return a bot response.
    - Lots of missing error handling and corner cases.