# AppFlowy

* ( ) [appflowy-io/appflowy/issues/3125](https://github.com/AppFlowy-IO/AppFlowy/issues/3125)
* ( ) Which conversions are necessary?
* ( ) Which modules do I need to write? How can I minimize redundancies while maintaining flexibility and extensibility?
* ( ) Which off-the-shelf solutions exist already?
* ( ) rofi integration
* ( ) polybar integration
* ( ) What will be the APIs of the modules?
* ( ) Which programming languages will I use for each module?
* ( ) try to run signald in a docker container
* ( ) read semaphore docs and read through examples
* ( ) → eventually add neorg - anki interface
* ( ) Add purity checks (i.e. no side effects) to tests
* ( ) Improve serialization for copying
* ( ) a.to_{x}() and a.from_{x}() should be perfect inverses → add to tests
* ( ) figure out how to add norg support to a fork of AppFlowy
* ( ) How to connect flutter app to backend? → Look at AppFlowy & its Private Cloud when it is released soon
* ( ) How to make planager server for AppFlowy?
* ( ) Django or Flask (or FastAPI) for first iteration?
* ( ) dead tree Rust book in German → roadmaps
* ( ) → Implement scheduling module in polyglot-projects, also corresponding visualizer
* ( ) TRACKING: manually via neorg, or via semaphore. One file per metric for easy tracking; move dates more than 30 days old to the old store (more efficient format?)
* ( ) [packaging.python.org/en/latest/guides/creating-and-discovering-plugins](https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/)

AppFlowy is a web application, which means that you can use it on any device that has a web browser. To host it so that you can use it on your Android device and desktop, there are a few options:

1. Host it on a server and access it through a web browser on your desktop and Android device: You can host AppFlowy on a server and access it through a web browser on your desktop or Android device. This way, you can use AppFlowy on any device that has a web browser.
2. Install a local server on your desktop and access it through a web browser on your desktop and Android device: You can install a local server on your desktop and access AppFlowy through a web browser on your desktop or Android device. This way, you can use AppFlowy on your desktop without an internet connection, and access it on your Android device through a local network.
3. Use a cloud-based service that allows you to host web applications: There are several cloud-based services, such as AWS, DigitalOcean, and Heroku, that allow you to host web applications. You can host AppFlowy on one of these services and access it through a web browser on your desktop or Android device. This way, you can use AppFlowy on any device that has a web browser, and you don't need to worry about managing a server.

Regardless of which option you choose, it's important to make sure that you keep your AppFlowy account secure by using a strong and unique password, and enabling two-factor authentication if possible.

search “hosting” [discord.com/channels/903549834160635914/903553722804748309](https://discord.com/channels/903549834160635914/903553722804748309)
