[app]
title = Slayer AdBlocker
package.name = slayeradblocker
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
